import { NextResponse } from 'next/server';
import { getAllCases, saveCase, getCaseById } from '../../../repo/case-repo';
import { CaseEvaluationRequestSchema, CaseDocument } from '../../../types';
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
    
    const documents: CaseDocument[] = ((parsed.documents || (body.documentTexts as any) || []) as CaseDocument[]);

    const evaluated = await runComplete13StepEvaluation(
      parsed.title,
      parsed.taxpayerName,
      parsed.gstin,
      parsed.financialYear,
      parsed.disputedAmount,
      parsed.noticeType,
      parsed.primaryIssue,
      parsed.caseSummary,
      documents,
      parsed.geminiApiKey
    );

    const saved = await saveCase(evaluated);
    return NextResponse.json({ success: true, case: saved });
  } catch (err: any) {
    return NextResponse.json({ success: false, error: err.message }, { status: 400 });
  }
}