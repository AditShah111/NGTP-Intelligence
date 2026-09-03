code_analyze_route = """import { NextResponse } from 'next/server';
import { CaseEvaluationRequestSchema, CaseDocument } from '../../../types';
import { runComplete13StepEvaluation } from '../../../service/evaluator-agent';
import { saveCase } from '../../../repo/case-repo';
import { validateNGTPScope } from '../../../service/ngtp-gatekeeper';

export const dynamic = 'force-dynamic';

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const parsed = CaseEvaluationRequestSchema.parse(body);

    const documents: CaseDocument[] = ((parsed.documents || (body.documentTexts as any) || []) as CaseDocument[]);

    // 1. Mandatory NGTP Scope Gatekeeper Check
    const gatekeeperResult = validateNGTPScope(
      parsed.title,
      parsed.primaryIssue,
      parsed.caseSummary,
      parsed.noticeType,
      documents
    );

    if (!gatekeeperResult.isNGTP) {
      return NextResponse.json({
        success: false,
        notApplicable: true,
        rejectionReason: gatekeeperResult.rejectionReason,
        detectedDomain: gatekeeperResult.detectedDomain,
        allowedTopics: gatekeeperResult.allowedTopics
      }, { status: 422 });
    }

    // 2. Execute 13-Step Verification Pipeline (Restricted to NGTP)
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
"""

with open("src/app/api/analyze/route.ts", "w", encoding="utf-8") as f:
    f.write(code_analyze_route)

print("Updated src/app/api/analyze/route.ts with NGTP scope validation!")