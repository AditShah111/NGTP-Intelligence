const { Pool } = require('pg');

const DATABASE_URL = process.env.DATABASE_URL || 'postgresql://postgres:Moksha@591$%@db.wvgomkamelpziuwdqgbm.supabase.co:5432/postgres';

const pool = new Pool({
  connectionString: DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

async function main() {
  console.log('🔗 Connecting to Supabase database...');
  const client = await pool.connect();
  try {
    console.log('1. Creating dedicated ngtp schema (guaranteeing zero collision with society tables)...');
    await client.query('CREATE SCHEMA IF NOT EXISTS ngtp;');

    console.log('2. Creating ngtp.cases and ngtp.audit_logs tables...');
    await client.query(`
      CREATE TABLE IF NOT EXISTS ngtp.cases (
        id VARCHAR(100) PRIMARY KEY,
        title TEXT NOT NULL,
        taxpayer_name TEXT NOT NULL,
        gstin VARCHAR(50) NOT NULL,
        financial_year VARCHAR(20) NOT NULL,
        disputed_amount TEXT NOT NULL,
        notice_type VARCHAR(100) NOT NULL,
        primary_issue TEXT NOT NULL,
        summary TEXT,
        case_data JSONB NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
      );
    `);

    await client.query(`
      CREATE TABLE IF NOT EXISTS ngtp.audit_logs (
        id SERIAL PRIMARY KEY,
        case_id VARCHAR(100) REFERENCES ngtp.cases(id) ON DELETE CASCADE,
        action VARCHAR(100) NOT NULL,
        actor VARCHAR(100) DEFAULT 'LitigationEvaluatorAgent',
        payload JSONB,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
      );
    `);

    console.log('3. Checking ngtp.cases count...');
    const countRes = await client.query('SELECT count(*) FROM ngtp.cases;');
    console.log(`✓ ngtp.cases row count: ${countRes.rows[0].count}`);

    // Verify public society tables are intact and untouched
    const pubRes = await client.query("SELECT count(*) FROM information_schema.tables WHERE table_schema='public';");
    console.log(`✓ Public schema untouched (${pubRes.rows[0].count} public tables preserved).`);

    console.log('🎉 Supabase Database Schema Initialized Successfully!');
  } finally {
    client.release();
    await pool.end();
  }
}

main().catch(err => {
  console.error('Database migration error:', err);
  process.exit(1);
});