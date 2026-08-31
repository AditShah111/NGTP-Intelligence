import { NextResponse } from 'next/server';
import { pool } from '../../../repo/db';

export const dynamic = 'force-dynamic';

export async function GET() {
  let dbStatus = 'disconnected';
  try {
    const res = await Promise.race([
      pool.query('SELECT 1 as test'),
      new Promise((_, reject) => setTimeout(() => reject(new Error('timeout')), 2000))
    ]);
    if ((res as any)?.rows?.length > 0) dbStatus = 'connected';
  } catch (err) {
    dbStatus = 'fallback_cache';
  }

  return NextResponse.json({
    status: 'healthy',
    engine: 'NGTP Litigation Readiness & Viability Engine',
    version: '1.0.0',
    database: dbStatus,
    timestamp: new Date().toISOString()
  });
}
