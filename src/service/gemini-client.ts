import { GoogleGenerativeAI } from '@google/generative-ai';
import { ENV } from '../config/env';

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
    const jsonMatch = raw.match(/\[[\s\S]*\]/);
    if (jsonMatch) {
      return JSON.parse(jsonMatch[0]);
    }
  } catch (e) {
    console.warn('Could not parse Gemini JSON response');
  }
  return null;
}