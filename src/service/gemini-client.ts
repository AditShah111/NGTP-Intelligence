import { GoogleGenerativeAI } from '@google/generative-ai';
import { ENV } from '../config/env';

export async function runGeminiLegalAnalysis(
  prompt: string,
  userApiKey?: string,
  systemInstruction?: string
): Promise<string | null> {
  const apiKey = userApiKey || ENV.GEMINI_API_KEY || process.env.GEMINI_API_KEY;
  if (!apiKey) {
    console.log('[Gemini Client] No API Key provided, using deterministic legal knowledge engine.');
    return null;
  }

  try {
    const genAI = new GoogleGenerativeAI(apiKey);
    const model = genAI.getGenerativeModel({
      model: 'gemini-1.5-pro',
      systemInstruction: systemInstruction || 'You are an expert Indian tax litigation analyst specializing in GST litigation, Section 16(2)(c), Section 74, SCNs, First Appeals, and Supreme Court precedent strategy. Maintain strict factual discipline and never hallucinate citations.'
    });

    const result = await model.generateContent(prompt);
    const response = await result.response;
    return response.text();
  } catch (err: any) {
    console.warn('[Gemini Client Error]', err.message);
    return null;
  }
}

export async function generateAdversarialRedTeamWithGemini(
  caseSummary: string,
  primaryIssue: string,
  userApiKey?: string
) {
  const prompt = `Analyze this GST matter and act as an aggressive Senior Departmental Standing Counsel / Revenue Representative.
Matter Summary: ${caseSummary}
Primary Issue: ${primaryIssue}

Generate 3 lethal opposing arguments testing:
1. Section 16(2)(c) tax-paid condition non-obstante override
2. Burden of proof under Section 155 CGST Act
3. Fact verification, transport records, or supplier status

Return a JSON array with schema:
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

  const raw = await runGeminiLegalAnalysis(prompt, userApiKey);
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
