import os

code_health = """import { NextResponse } from 'next/server';
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
"""

code_bench = """import { NextResponse } from 'next/server';
import { BENCHMARK_CASES } from '../../../repo/benchmark-data';

export const dynamic = 'force-dynamic';

export async function GET() {
  return NextResponse.json({
    success: true,
    count: BENCHMARK_CASES.length,
    cases: BENCHMARK_CASES
  });
}
"""

code_cases = """import { NextResponse } from 'next/server';
import { getAllCases, saveCase, getCaseById } from '../../../repo/case-repo';
import { CaseEvaluationRequestSchema } from '../../../types';
import { runComplete13StepEvaluation } from '../../../service/evaluator-agent';

export const dynamic = 'force-dynamic';

export async function GET(req: Request) {
  const { searchParams } = new URL(req.url);
  const id = searchParams.get('id');
  if (id) {
    const c = await getCaseById(id);
    if (!c) return NextResponse.json({ success: false, error: 'Case not found' }, { status: 404 });
    return NextResponse.json({ success: true, case: c });
  }
  const all = await getAllCases();
  return NextResponse.json({ success: true, count: all.length, cases: all });
}

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const parsed = CaseEvaluationRequestSchema.parse(body);
    
    const evaluated = runComplete13StepEvaluation(
      parsed.title,
      parsed.taxpayerName,
      parsed.gstin,
      parsed.financialYear,
      parsed.disputedAmount,
      parsed.noticeType,
      parsed.primaryIssue,
      parsed.caseSummary,
      parsed.documentTexts || []
    );

    const saved = await saveCase(evaluated);
    return NextResponse.json({ success: true, case: saved });
  } catch (err: any) {
    return NextResponse.json({ success: false, error: err.message }, { status: 400 });
  }
}
"""

code_analyze = """import { NextResponse } from 'next/server';
import { CaseEvaluationRequestSchema } from '../../../types';
import { runComplete13StepEvaluation } from '../../../service/evaluator-agent';
import { saveCase } from '../../../repo/case-repo';

export const dynamic = 'force-dynamic';

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const parsed = CaseEvaluationRequestSchema.parse(body);

    const evaluated = runComplete13StepEvaluation(
      parsed.title,
      parsed.taxpayerName,
      parsed.gstin,
      parsed.financialYear,
      parsed.disputedAmount,
      parsed.noticeType,
      parsed.primaryIssue,
      parsed.caseSummary,
      parsed.documentTexts || []
    );

    await saveCase(evaluated);

    return NextResponse.json({
      success: true,
      evaluatedCase: evaluated
    });
  } catch (err: any) {
    return NextResponse.json({
      success: false,
      error: err.message
    }, { status: 400 });
  }
}
"""

with open("src/app/api/health/route.ts", "w", encoding="utf-8") as f:
    f.write(code_health)
with open("src/app/api/benchmark/route.ts", "w", encoding="utf-8") as f:
    f.write(code_bench)
with open("src/app/api/cases/route.ts", "w", encoding="utf-8") as f:
    f.write(code_cases)
with open("src/app/api/analyze/route.ts", "w", encoding="utf-8") as f:
    f.write(code_analyze)

print("Updated all API routes to be force-dynamic!")