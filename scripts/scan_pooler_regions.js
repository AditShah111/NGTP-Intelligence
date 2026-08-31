const { Pool } = require('pg');

const regions = [
  'ap-south-1',
  'ap-southeast-1',
  'ap-southeast-2',
  'ap-northeast-1',
  'ap-northeast-2',
  'us-east-1',
  'us-east-2',
  'us-west-1',
  'us-west-2',
  'eu-central-1',
  'eu-west-1',
  'eu-west-2',
  'eu-west-3',
  'sa-east-1',
  'ca-central-1'
];

async function findRegion() {
  for (const reg of regions) {
    const host = `aws-0-${reg}.pooler.supabase.com`;
    const connStr = `postgresql://postgres.wvgomkamelpziuwdqgbm:Moksha%40591%24%25@${host}:6543/postgres`;
    const pool = new Pool({
      connectionString: connStr,
      ssl: { rejectUnauthorized: false },
      connectionTimeoutMillis: 3000
    });
    try {
      const client = await pool.connect();
      const res = await client.query('SELECT 1 as connected;');
      console.log(`FOUND WORKING POOLER! Region: ${reg}, Host: ${host}`);
      client.release();
      await pool.end();
      return connStr;
    } catch (err) {
      if (!err.message.includes('tenant/user') && !err.message.includes('timeout')) {
        console.log(`Region ${reg} returned:`, err.message);
      }
      await pool.end();
    }
  }
  console.log('Finished region scan.');
}

findRegion().catch(console.error);