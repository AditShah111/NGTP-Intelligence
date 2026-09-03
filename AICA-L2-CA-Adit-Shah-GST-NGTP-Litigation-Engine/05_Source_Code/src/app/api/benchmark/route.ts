import { NextResponse } from 'next/server';
import { BENCHMARK_CASES } from '../../../repo/benchmark-data';

export const dynamic = 'force-dynamic';

export async function GET() {
  return NextResponse.json({
    success: true,
    count: BENCHMARK_CASES.length,
    cases: BENCHMARK_CASES
  });
}
