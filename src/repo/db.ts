import dns from 'dns';
try {
  dns.setDefaultResultOrder('ipv4first');
} catch (e) {}

import { Pool } from 'pg';
import { ENV } from '../config/env';

// Connection pool with SSL support for Supabase PostgreSQL
export const pool = new Pool({
  connectionString: ENV.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false
  },
  max: 10,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 8000
});

// Auto-initialize dedicated 'ngtp' schema and tables
let isInitialized = false;

export async function initDbSchema(): Promise<boolean> {
  if (isInitialized) return true;
  try {
    const client = await pool.connect();
    try {
      // 1. Create dedicated schema 'ngtp' to guarantee ZERO COLLISION with public tables
      await client.query(`CREATE SCHEMA IF NOT EXISTS ngtp;`);

      // 2. Create ngtp.cases table
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

      // 3. Create ngtp.audit_logs table
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

      isInitialized = true;
      console.log('? [Supabase PostgreSQL] NGTP Schema & Tables verified successfully.');
      return true;
    } finally {
      client.release();
    }
  } catch (err: any) {
    console.warn('?? [Supabase DB Warning] Could not connect to remote DB; using resilient in-memory store:', err.message);
    return false;
  }
}
