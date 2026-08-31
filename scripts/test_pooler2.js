const { Pool } = require('pg');

const connectionStringsToTest = [
  "postgresql://postgres.wvgomkamelpziuwdqgbm:Moksha%40591%24%25@aws-0-ap-south-1.pooler.supabase.com:6543/postgres",
  "postgresql://postgres.wvgomkamelpziuwdqgbm:Moksha%40591%24%25@aws-0-ap-south-1.pooler.supabase.com:5432/postgres",
  "postgresql://postgres:Moksha%40591%24%25@aws-0-ap-south-1.pooler.supabase.com:6543/postgres",
  "postgresql://postgres:Moksha%40591%24%25@db.wvgomkamelpziuwdqgbm.supabase.co:5432/postgres"
];

async function testConnections() {
  for (const connStr of connectionStringsToTest) {
    console.log('\nTesting:', connStr.replace(/:[^:@]+@/, ':***@'));
    const pool = new Pool({
      connectionString: connStr,
      ssl: { rejectUnauthorized: false },
      connectionTimeoutMillis: 6000
    });
    try {
      const client = await pool.connect();
      const res = await client.query('SELECT 1 as connected, current_database(), current_user;');
      console.log('SUCCESS! Connected:', res.rows[0]);
      client.release();
      await pool.end();
      return connStr;
    } catch (err) {
      console.log('FAILED:', err.message);
      await pool.end();
    }
  }
}

testConnections().catch(console.error);