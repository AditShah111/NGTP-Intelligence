const { Pool } = require('pg');
const fs = require('fs');
const path = require('path');

const DATABASE_URL = process.env.DATABASE_URL || 'postgresql://postgres:Moksha@591$%@db.wvgomkamelpziuwdqgbm.supabase.co:5432/postgres';

const pool = new Pool({
  connectionString: DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

async function seed() {
  const client = await pool.connect();
  try {
    // Read the compiled benchmark data or extract JSON
    const benchTs = fs.readFileSync(path.join(__dirname, '../src/repo/benchmark-data.ts'), 'utf8');
    const jsonMatch = benchTs.match(/export const BENCHMARK_CASES: CaseStudy\[\] = (\[[\s\S]*\]);/);
    if (!jsonMatch) throw new Error('Could not parse benchmark data');
    const cases = JSON.parse(jsonMatch[1]);

    for (const c of cases) {
      console.log(`Seeding case: ${c.title} (${c.id})...`);
      await client.query(`
        INSERT INTO ngtp.cases (id, title, taxpayer_name, gstin, financial_year, disputed_amount, notice_type, primary_issue, summary, case_data, updated_at)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, CURRENT_TIMESTAMP)
        ON CONFLICT (id) DO UPDATE SET
          title = EXCLUDED.title,
          taxpayer_name = EXCLUDED.taxpayer_name,
          gstin = EXCLUDED.gstin,
          financial_year = EXCLUDED.financial_year,
          disputed_amount = EXCLUDED.disputed_amount,
          notice_type = EXCLUDED.notice_type,
          primary_issue = EXCLUDED.primary_issue,
          summary = EXCLUDED.summary,
          case_data = EXCLUDED.case_data,
          updated_at = CURRENT_TIMESTAMP;
      `, [
        c.id,
        c.title,
        c.taxpayerName,
        c.gstin,
        c.financialYear,
        c.disputedAmount,
        c.noticeType,
        c.primaryIssue,
        c.summary,
        JSON.stringify(c)
      ]);
    }

    const countRes = await client.query('SELECT count(*) FROM ngtp.cases;');
    console.log(`✓ Successfully seeded ${countRes.rows[0].count} cases into Supabase ngtp.cases!`);
  } finally {
    client.release();
    await pool.end();
  }
}

seed().catch(err => {
  console.error('Seeding error:', err);
  process.exit(1);
});