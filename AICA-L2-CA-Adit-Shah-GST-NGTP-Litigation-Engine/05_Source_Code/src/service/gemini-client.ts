import { GoogleGenerativeAI } from '@google/generative-ai';
import { ENV } from '../config/env';
import { PrecedentAnalysis, PrecedentEvidentiaryImpact, CaseDocument, BenchType, Article141Precedence, SlpStatus } from '../types';

// Helper with strict 5-second timeout to prevent ANY UI hang or freeze
function timeoutPromise<T>(promise: Promise<T>, timeoutMs: number): Promise<T> {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => {
      reject(new Error(`Operation timed out after ${timeoutMs}ms`));
    }, timeoutMs);

    promise
      .then((res) => {
        clearTimeout(timer);
        resolve(res);
      })
      .catch((err) => {
        clearTimeout(timer);
        reject(err);
      });
  });
}

export async function runGeminiLegalAnalysis(
  prompt: string,
  userApiKey?: string,
  systemInstruction?: string,
  preferredModel?: string
): Promise<string | null> {
  const apiKey = userApiKey || ENV.GEMINI_API_KEY || process.env.GEMINI_API_KEY;
  if (!apiKey || apiKey.trim() === '') {
    return null;
  }

  const genAI = new GoogleGenerativeAI(apiKey);
  const modelsToTry = [
    preferredModel,
    'gemini-2.5-flash',
    'gemini-2.0-flash',
    'gemini-2.5-pro'
  ].filter(Boolean) as string[];

  const instruction = systemInstruction || 'You are an expert Indian Supreme Court and High Court GST litigation research counsel. Provide factual legal analysis without hallucination.';

  for (const modelName of modelsToTry) {
    try {
      const model = genAI.getGenerativeModel({
        model: modelName,
        systemInstruction: instruction
      });

      const generateTask = async () => {
        const result = await model.generateContent(prompt);
        const response = await result.response;
        return response.text();
      };

      // 5-second strict timeout per model
      const text = await timeoutPromise(generateTask(), 5000);
      if (text) return text;
    } catch (err: any) {
      console.warn(`[Gemini Client] Model ${modelName} skipped or timed out:`, err.message);
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
  const docSummary = documents.map(d => `${d.name} (${d.type}): ${d.extractedTextSnippet}`).join('\n');

  const prompt = `Act as an authoritative Indian GST legal researcher. Research genuine High Court & Supreme Court judgments for:
Topic: ${customQuery || topicDomain}
Issue: ${primaryIssue}
Financial Year: ${financialYear}

Return 4-6 genuine judgments (e.g. Suncraft Energy, Arise India, D.Y. Beathel, LGW Industries, Diya Agencies, Halder Enterprises, Gheru Lal, Wipro Ltd) in JSON array format:
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
    "benchType": "High Court Division Bench" | "Supreme Court Division Bench" | "High Court Single Bench",
    "benchStrength": 2,
    "article141Status": "SUPREME_BINDING" | "HIGH_COURT_BINDING",
    "slpStatus": "Affirmed by Supreme Court" | "No SLP Filed",
    "judicialAuthorityStrengthScore": 95,
    "evidentiaryWeightImpact": [
      { "parameterCode": "P3", "impactDescription": "Exhaustion doctrine", "weightModifier": 1.3 }
    ],
    "presentCaseEvidenceSatisfying": ["Invoices", "Bank Statements"],
    "presentCaseEvidenceFailing": [],
    "litigationUse": "string",
    "comparabilityScore": {
      "statutorySimilarity": 19,
      "factualSimilarity": 24,
      "evidentiarySimilarity": 19,
      "proceduralSimilarity": 10,
      "courtAuthorityRelevance": 14,
      "distinguishabilityRisk": 9,
      "totalScore": 95,
      "explanation": "string"
    }
  }
]`;

  const raw = await runGeminiLegalAnalysis(prompt, userApiKey);
  if (!raw) return null;

  try {
    const jsonMatch = raw.match(/\[[\s\S]*\]/);
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
  const prompt = `Analyze this GST matter and generate 3 opposing Revenue Counsel arguments:
Matter: ${caseSummary}
Issue: ${primaryIssue}

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
    const jsonMatch = raw.match(/\[[\s\S]*\]/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }
  } catch (e) {
    console.warn('Could not parse Gemini JSON response');
  }
  return null;
}
