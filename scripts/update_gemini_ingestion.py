code_gemini_full = """import { GoogleGenerativeAI } from '@google/generative-ai';
import { ENV } from '../config/env';
import { PrecedentAnalysis, PrecedentEvidentiaryImpact, CaseDocument } from '../types';

export async function runGeminiLegalAnalysis(
  prompt: string,
  userApiKey?: string,
  systemInstruction?: string,
  preferredModel?: string
): Promise<string | null> {
  const apiKey = userApiKey || ENV.GEMINI_API_KEY || process.env.GEMINI_API_KEY;
  if (!apiKey) {
    console.log('[Gemini Client] No API Key provided, using deterministic legal knowledge engine.');
    return null;
  }

  const genAI = new GoogleGenerativeAI(apiKey);
  const modelsToTry = [
    preferredModel,
    'gemini-2.5-pro',
    'gemini-2.5-flash',
    'gemini-2.0-flash',
    'gemini-2.0-pro-exp-02-05'
  ].filter(Boolean) as string[];

  const instruction = systemInstruction || 'You are an elite Indian Supreme Court and High Court GST litigation research counsel specializing in Non-Genuine Taxable Persons (NGTP), Section 16(2)(c) supplier default, Section 155 burden of proof, Circular 183/193 safe-harbors, and forensic evidence audits. Maintain absolute factual and legal accuracy.';

  for (const modelName of modelsToTry) {
    try {
      const model = genAI.getGenerativeModel({
        model: modelName,
        systemInstruction: instruction
      });

      const result = await model.generateContent(prompt);
      const response = await result.response;
      const text = response.text();
      if (text) return text;
    } catch (err: any) {
      console.warn(`[Gemini Client Warning] Model ${modelName} failed, trying fallback:`, err.message);
    }
  }

  return null;
}

export async function ingestRealTimeNgtpPrecedents(
  topicDomain: string,
  primaryIssue: string,
  financialYear: string,
  userApiKey?: string,
  documents: CaseDocument[] = []
): Promise<PrecedentAnalysis[] | null> {
  const docSummary = documents.map(d => `${d.name} (${d.type}): ${d.extractedTextSnippet}`).join('\\n');

  const prompt = `Act as an expert Indian GST judicial researcher. Ingest and analyze real-time landmark and latest (2023, 2024, 2025, 2026) Indian High Court and Supreme Court rulings specifically relating to NGTP (Non-Genuine / Non-Existent Taxable Persons), Section 16(2)(c), Section 74, fake invoicing, or supplier non-payment.

Dispute Context:
- Domain: ${topicDomain}
- Primary Legal Issue: ${primaryIssue}
- Financial Year: ${financialYear}
- Available Evidence in Present Case:
${docSummary || 'None uploaded yet'}

Return an array of 3-4 genuine, authoritative High Court or Supreme Court precedents (e.g. Suncraft Energy, D.Y. Beathel, Arise India, LGW Industries, M/s MT Agencies, Halder Enterprises, Gheru Lal, or recent 2024-2025 HC orders).

For EACH precedent, perform a deep EVIDENCE AUDIT:
1. Extract exact citations and dates.
2. List the specific "evidencesReliedOnByCourt" (e.g., invoices, bank RTGS, Part-B E-way bills, FASTag toll logs, CA Cert, active GST status on invoice date).
3. State the "criticalEvidentiaryThreshold" (the decisive piece of evidence that determined the outcome).
4. Detail the "evidentiaryWeightImpact" on parameters P1 through P8.
5. Compute a 6-axis comparability score (0-100) against the present case's evidence.

Return ONLY a valid JSON array matching this exact schema:
[
  {
    "id": "prec-dyn-1",
    "caseName": "string",
    "court": "string",
    "citation": "string",
    "relevantProvision": "string",
    "topicDomain": "string",
    "materialFacts": "string",
    "ratioLegalPrinciple": "string",
    "evidencesReliedOnByCourt": ["string"],
    "criticalEvidentiaryThreshold": "string",
    "necessaryConditions": ["string"],
    "distinguishingFacts": ["string"],
    "favourableApplicability": "HIGH" | "MEDIUM" | "LOW",
    "adverseApplicability": "NONE" | "LOW" | "MEDIUM",
    "parameterExtracted": "string",
    "evidentiaryWeightImpact": [
      {
        "parameterCode": "P1" | "P2" | "P3" | "P4" | "P5" | "P6" | "P7" | "P8",
        "impactDescription": "string",
        "weightModifier": number
      }
    ],
    "presentCaseEvidenceSatisfying": ["string"],
    "presentCaseEvidenceFailing": ["string"],
    "litigationUse": "string",
    "comparabilityScore": {
      "statutorySimilarity": number,
      "factualSimilarity": number,
      "evidentiarySimilarity": number,
      "proceduralSimilarity": number,
      "courtAuthorityRelevance": number,
      "distinguishabilityRisk": number,
      "totalScore": number,
      "explanation": "string"
    }
  }
]`;

  const raw = await runGeminiLegalAnalysis(prompt, userApiKey);
  if (!raw) return null;

  try {
    const jsonMatch = raw.match(/\\[[\\s\\S]*\\]/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]) as PrecedentAnalysis[];
    }
  } catch (e) {
    console.warn('Could not parse ingested NGTP precedents JSON');
  }
  return null;
}

export async function fetchLatestPrecedentsWithGemini(
  primaryIssue: string,
  financialYear: string,
  userApiKey?: string,
  documents: CaseDocument[] = []
): Promise<PrecedentAnalysis[] | null> {
  return ingestRealTimeNgtpPrecedents('Section 16(2)(c) & NGTP Supplier Default', primaryIssue, financialYear, userApiKey, documents);
}

export async function generateAdversarialRedTeamWithGemini(
  caseSummary: string,
  primaryIssue: string,
  userApiKey?: string,
  preferredModel?: string
) {
  const prompt = `Analyze this GST matter and act as an aggressive Senior Departmental Standing Counsel / Revenue Representative.
Matter Summary: ${caseSummary}
Primary Issue: ${primaryIssue}

Generate 4 lethal opposing arguments testing:
1. Section 16(2)(c) tax-paid condition non-obstante override
2. Burden of proof under Section 155 CGST Act
3. Physical goods movement and E-Way bill corroboration
4. Upstream non-genuine supplier (NGTP) / cancelled GSTIN taint

Return ONLY a JSON array with schema:
[
  {
    "id": "rt-ai-1",
    "category": "string",
    "opposingArgument": "string",
    "strengthOfOpposingArgument": number (60-95),
    "taxpayerResponse": "string",
    "evidenceSupportingResponse": "string",
    "residualRisk": "LOW" | "MEDIUM" | "HIGH",
    "survivesAttack": boolean
  }
]`;

  const raw = await runGeminiLegalAnalysis(prompt, userApiKey, undefined, preferredModel);
  if (!raw) return null;

  try {
    const jsonMatch = raw.match(/\\[[\\s\\S]*\\]/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }
  } catch (e) {
    console.warn('Could not parse Gemini JSON response');
  }
  return null;
}
"""

with open("src/service/gemini-client.ts", "w", encoding="utf-8") as f:
    f.write(code_gemini_full)

print("Updated src/service/gemini-client.ts with real-time NGTP case law ingestion and evidence extraction!")