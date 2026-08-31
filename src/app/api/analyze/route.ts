import { NextResponse } from 'next/server';
import { CaseEvaluationRequestSchema, CaseDocument } from '../../../types';
import { runComplete13StepEvaluation } from '../../../service/evaluator-agent';
import { saveCase } from '../../../repo/case-repo';

export const dynamic = 'force-dynamic';

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