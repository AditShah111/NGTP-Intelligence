import { NextRequest, NextResponse } from 'next/server';
import { ingestRealTimeNgtpPrecedents } from '../../../service/gemini-client';
import { evaluateStatutoryParameters } from '../../../service/statutory-engine';
import { BENCHMARK_PRECEDENTS } from '../../../service/precedent-engine';
import { resolvePrecedentConflicts } from '../../../service/hierarchy-engine';
import { CaseDocument } from '../../../types';

export const dynamic = 'force-dynamic';

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { 
      topicDomain = 'Section 16(2)(c) & NGTP Supplier Default',
      primaryIssue = 'Recovery from recipient under Section 16(2)(c) without pursuing supplier',
      financialYear = '2018-19',
      geminiApiKey,
      documents = []
    } = body;

    const hasInvoices = (documents as CaseDocument[]).some(d => d.type === 'Invoice');
    const hasTransit = (documents as CaseDocument[]).some(d => d.type === 'E-Way Bill' || d.type === 'Transporter Bilty');
    const hasBank = (documents as CaseDocument[]).some(d => d.type === 'Bank Statement');
    const hasScn = (documents as CaseDocument[]).some(d => d.type === 'SCN' || d.type === 'DRC-01' || d.type === 'DRC-07');
    const hasCaCert = (documents as CaseDocument[]).some(d => d.type === 'CA Certificate');

    // 1. Ingest dynamic case laws via Gemini
    let livePrecedents = await ingestRealTimeNgtpPrecedents(topicDomain, primaryIssue, financialYear, geminiApiKey, documents);
    
    // Fall back to rich benchmark library if needed
    if (!livePrecedents || livePrecedents.length === 0) {
      livePrecedents = BENCHMARK_PRECEDENTS.map(p => ({
        ...p,
        topicDomain,
        evidencesReliedOnByCourt: [
          'Tax Invoices fulfilling Rule 46 particulars',
          '100% Consideration + GST paid through RTGS/NEFT banking channels',
          'Supplier GSTR-1 return filing acknowledgment',
          'Absence of Departmental recovery or summons issued against supplier'
        ],
        criticalEvidentiaryThreshold: 'Bank RTGS payment proof establishing bona fide recipient status.',
        evidentiaryWeightImpact: [
          { parameterCode: 'P3', impactDescription: 'Mandatory supplier exhaustion doctrine', weightModifier: 1.3 },
          { parameterCode: 'P8', impactDescription: 'Initial burden discharged via bank records', weightModifier: 1.2 }
        ]
      }));
    }

    // 2. Resolve Article 141 Judicial Hierarchy & High Court Conflicts
    livePrecedents = resolvePrecedentConflicts(livePrecedents, hasBank);

    // 3. Calibrate statutory parameters dynamically
    const calibratedParameters = evaluateStatutoryParameters(
      financialYear,
      primaryIssue,
      hasInvoices,
      hasTransit,
      hasBank,
      hasScn,
      hasCaCert,
      livePrecedents
    );

    return NextResponse.json({
      success: true,
      topicDomain,
      ingestedCount: livePrecedents.length,
      ingestedPrecedents: livePrecedents,
      calibratedParameters,
      evidenceAuditSummary: {
        totalEvidencesRequiredByCourts: livePrecedents.flatMap(p => p.evidencesReliedOnByCourt || []).length,
        evidencesSatisfiedInPresentCase: livePrecedents.flatMap(p => p.presentCaseEvidenceSatisfying || []).length,
        criticalEvidentiaryThresholdMet: hasBank && hasInvoices
      }
    });
  } catch (err: any) {
    console.error('Ingestion API error:', err);
    return NextResponse.json({ success: false, error: err.message }, { status: 500 });
  }
}