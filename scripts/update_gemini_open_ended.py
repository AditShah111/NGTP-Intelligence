import os

code_gemini_dynamic = """import { GoogleGenerativeAI } from '@google/generative-ai';
import { ENV } from '../config/env';
import { PrecedentAnalysis, PrecedentEvidentiaryImpact, CaseDocument, BenchType, Article141Precedence, SlpStatus } from '../types';

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

  const instruction = systemInstruction || 'You are an elite Indian Supreme Court and High Court GST judicial research counsel. You possess comprehensive knowledge of all Indian High Court rulings (Calcutta, Madras, Delhi, Bombay, Karnataka, Kerala, Allahabad, Gujarat, Telangana, Punjab & Haryana, Patna, MP) and Supreme Court decisions on GST, Section 16(2)(c), Non-Genuine Taxable Persons (NGTP), Section 74, fake billing, and Section 155. Maintain strict factual discipline and never hallucinate citations.';

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
  documents: CaseDocument[] = [],
  customQuery?: string
): Promise<PrecedentAnalysis[] | null> {
  const docSummary = documents.map(d => `${d.name} (${d.type}): ${d.extractedTextSnippet}`).join('\\n');

  const prompt = `Act as an authoritative Indian GST legal researcher. Ingest and perform a comprehensive judicial research across Indian Supreme Court and ALL High Courts (Calcutta, Madras, Delhi, Bombay, Karnataka, Kerala, Allahabad, Gujarat, Telangana, Punjab & Haryana, Patna, Madhya Pradesh, etc.) for genuine, verifiable case laws on:

Search Topic / Domain: ${customQuery || topicDomain}
Primary Legal Issue: ${primaryIssue}
Financial Year: ${financialYear}

Case Evidence Context:
${docSummary || 'No specific files attached yet'}

Return an extensive array of 6 to 10 genuine, verifiable judgments (spanning Supreme Court and multiple High Courts) relevant to this dispute. Include both controlling favorable rulings (e.g., Suncraft Energy, Arise India, D.Y. Beathel, LGW Industries, M/s MT Agencies, Halder Enterprises, Gheru Lal, Diya Agencies, Wipro Ltd) and notable adverse/distinguishable rulings (e.g., Aastha Enterprises, ALD Automotive, Agrawal Metal).

For EVERY judgment returned, provide:
1. Exact case name, court, official citation, and date.
2. Judicial hierarchy details:
   - benchType: "Supreme Court Full/Constitution Bench" | "Supreme Court Division Bench" | "High Court Full Bench" | "High Court Division Bench" | "High Court Single Bench" | "Appellate Tribunal (CESTAT / GSTAT)"
   - benchStrength: number of judges on bench (e.g. 1, 2, 3, 5)
   - slpStatus: "Affirmed by Supreme Court" | "Pending before Supreme Court" | "Stayed by Supreme Court" | "Dismissed in Limine" | "No SLP Filed"
   - article141Status: "SUPREME_BINDING" | "HIGH_COURT_BINDING" | "PERSUASIVE" | "OVERRULED" | "DISTINGUISHABLE"
   - judicialAuthorityStrengthScore: number (0-100 based on bench composition and SC status)
3. Deep Evidentiary Reverse-Engineering:
   - evidencesReliedOnByCourt: Array of exact documents and evidentiary facts the court relied on to reach its verdict.
   - criticalEvidentiaryThreshold: The single decisive document or factual threshold that determined the outcome.
   - evidentiaryWeightImpact: Array of { parameterCode: "P1" | "P2" | "P3" | "P4" | "P5" | "P6" | "P7" | "P8", impactDescription: string, weightModifier: number }
4. Competing Conflict Analysis (if applicable):
   - competingConflictAnalysis: { conflictWith: string, conflictingCourt: string, conflictReason: string, whyThisPrecedentPrevails: string, article141Resolution: string }
5. 6-Axis Comparability Scoring against the present case facts (0-100).

Return ONLY valid JSON matching this schema:
[
  {
    "id": "prec-dyn-uuid",
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
    "adverseApplicability": "NONE" | "LOW" | "MEDIUM" | "HIGH",
    "parameterExtracted": "string",
    "benchType": "string",
    "benchStrength": number,
    "article141Status": "string",
    "slpStatus": "string",
    "judicialAuthorityStrengthScore": number,
    "competingConflictAnalysis": {
      "conflictWith": "string",
      "conflictingCourt": "string",
      "conflictReason": "string",
      "whyThisPrecedentPrevails": "string",
      "article141Resolution": "string"
    },
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
    console.warn('Could not parse ingested NGTP precedents JSON:', e);
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
    f.write(code_gemini_dynamic)

print("Updated src/service/gemini-client.ts with open-ended multi-case real-time ingestion!")