import os

code_gemini_expanded = """import { GoogleGenerativeAI } from '@google/generative-ai';
import { ENV } from '../config/env';
import { PrecedentAnalysis } from '../types';

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

  const instruction = systemInstruction || 'You are an expert Indian tax litigation analyst specializing in GST litigation, Section 16(2)(c), Section 74, SCNs, First Appeals, and Supreme Court precedent strategy. Maintain strict factual discipline and never hallucinate citations.';

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

export async function fetchLatestPrecedentsWithGemini(
  primaryIssue: string,
  financialYear: string,
  userApiKey?: string
): Promise<PrecedentAnalysis[] | null> {
  const prompt = `You are an elite Indian GST legal researcher. Research the latest landmark High Court and Supreme Court rulings (including 2023, 2024, 2025, and 2026 judgments) concerning:
Issue: ${primaryIssue}
Financial Year: ${financialYear}

Return an array of 2-3 genuine, verifiable landmark precedents (e.g. Suncraft Energy, D.Y. Beathel, Arise India, LGW Industries, Bharti Airtel, or latest HC orders).

Return ONLY valid JSON matching this schema:
[
  {
    "id": "prec-ai-1",
    "caseName": "string",
    "court": "string",
    "citation": "string",
    "relevantProvision": "string",
    "materialFacts": "string",
    "ratioLegalPrinciple": "string",
    "necessaryConditions": ["string"],
    "distinguishingFacts": ["string"],
    "favourableApplicability": "HIGH" | "MEDIUM" | "LOW",
    "adverseApplicability": "NONE" | "LOW" | "MEDIUM",
    "parameterExtracted": "string",
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
    console.warn('Could not parse Gemini precedent JSON');
  }
  return null;
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

Generate 3 lethal opposing arguments testing:
1. Section 16(2)(c) tax-paid condition non-obstante override
2. Burden of proof under Section 155 CGST Act
3. Fact verification, transport records, or supplier status

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
    f.write(code_gemini_expanded)

print("Updated src/service/gemini-client.ts with fetchLatestPrecedentsWithGemini!")