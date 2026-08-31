const { Pool } = require('pg');

// Project reference: wvgomkamelpziuwdqgbm
// Region: ap-south-1 (Mumbai) / AWS
const connectionStringsToTest = [
  "postgresql://postgres.wvgomkamelpziuwdqgbm:Moksha%40591%24%25@aws-0-ap-south-1.pooler.supabase.com:6543/postgres?sslmode=require",
  "postgresql://postgres.wvgomkamelpziuwdqgbm:Moksha%40591%24%25@aws-0-ap-south-1.pooler.supabase.com:5432/postgres?sslmode=require",
  "postgresql://postgres:Moksha%40591%24%25@db.wvgomkamelpziuwdqgbm.supabase.co:5432/postgres?sslmode=require"
];

async function testConnections() {
  for (const connStr of connectionStringsToTest) {
    console.log('\nTesting:', connStr.replace(/:[^:@]+@/, ':***@'));
    const pool = new Pool({
      connectionString: connStr,
      ssl: { rejectUnauthorized: false },
      connectionTimeoutMillis: 5000
    });
    try {
      const client = await pool.connect();
      const res = await client.query('SELECT 1 as connected;');
      console.log('SUCCESS! Result:', res.rows);
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