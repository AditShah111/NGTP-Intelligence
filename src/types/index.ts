import { z } from 'zod';

export type EvidenceStrength = 
  | 'Established' 
  | 'Strongly supported' 
  | 'Probable' 
  | 'Disputed' 
  | 'Unsupported' 
  | 'Contradicted' 
  | 'Unable to determine';

export type AssessmentStatus = 
  | 'SATISFIED' 
  | 'PARTIALLY SATISFIED' 
  | 'NOT SATISFIED' 
  | 'UNCERTAIN';

export type RiskLevel = 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
export type ErrorSeverity = 'Minor' | 'Material' | 'Serious' | 'Fundamental';
export type PriorityLevel = 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
export type Recommendation = 'PROCEED' | 'PROCEED AFTER RECTIFICATION' | 'HOLD' | 'DO NOT PROCEED';
export type OutcomeProbability = 'LOW' | 'MODERATE' | 'HIGH';
export type OcrReadability = 'Clearly readable text' | 'Uncertain OCR text' | 'Missing text' | 'Potentially misread text';

export interface FactMatrixItem {
  id: string;
  issue: string;
  allegedFact: string;
  sourceDocument: string;
  pageParagraph: string;
  evidenceStrength: EvidenceStrength;
  contradiction: string;
  significance: string;
  ocrStatus?: OcrReadability;
}

export interface StatutoryParameter {
  id: string;
  parameterCode: string;
  title: string;
  statutoryProvision: string;
  statutoryRequirement: string;
  legalTest: string;
  burdenOfProof: string;
  requiredEvidence: string[];
  availableEvidence: string[];
  assessment: AssessmentStatus;
  risk: RiskLevel;
  reason: string;
}

export interface PrecedentAnalysis {
  id: string;
  caseName: string;
  court: string;
  citation: string;
  relevantProvision: string;
  materialFacts: string;
  ratioLegalPrinciple: string;
  necessaryConditions: string[];
  distinguishingFacts: string[];
  favourableApplicability: 'HIGH' | 'MEDIUM' | 'LOW' | 'NONE';
  adverseApplicability: 'HIGH' | 'MEDIUM' | 'LOW' | 'NONE';
  parameterExtracted: string;
  presentCaseEvidenceSatisfying: string[];
  presentCaseEvidenceFailing: string[];
  litigationUse: string;
  comparabilityScore: {
    statutorySimilarity: number;
    factualSimilarity: number;
    evidentiarySimilarity: number;
    proceduralSimilarity: number;
    courtAuthorityRelevance: number;
    distinguishabilityRisk: number;
    totalScore: number;
    explanation: string;
  };
}

export interface LowerAuthorityError {
  id: string;
  finding: string;
  lowerAuthorityReasoning: string;
  evidenceIgnoredMisread: string;
  legalError: string;
  relevantAuthority: string;
  strength: ErrorSeverity;
}

export interface ImprovedSubmissionGround {
  groundNumber: string;
  title: string;
  proposition: string;
  supportingFacts: string[];
  evidence: string[];
  statutoryBasis: string;
  precedent: string;
  application: string;
  likelyRevenueCounterargument: string;
  response: string;
  residualWeakness: string;
  groundStrength: number;
}

export interface AdversarialRedTeamItem {
  id: string;
  category: string;
  opposingArgument: string;
  strengthOfOpposingArgument: number;
  taxpayerResponse: string;
  evidenceSupportingResponse: string;
  residualRisk: RiskLevel;
  survivesAttack: boolean;
}

export interface EvidenceGapItem {
  id: string;
  missingEvidence: string;
  legalRelevance: string;
  whyItMatters: string;
  possibleSource: string;
  impactIfObtained: string;
  impactIfUnavailable: string;
  priority: PriorityLevel;
  category: 'Exists but not relied upon' | 'Should be obtained' | 'Cannot realistically be obtained' | 'Material game-changer';
}

export interface ReadinessScoreBreakdown {
  statutoryPosition: number;
  evidence: number;
  precedent: number;
  lowerAuthorityError: number;
  draftingQuality: number;
  counterargumentResilience: number;
  proceduralPosition: number;
  totalScore: number;
  interpretation: string;
}

export interface ViabilityScoreBreakdown {
  merits: number;
  evidenceQuality: number;
  precedentSupport: number;
  proceduralSoundness: number;
  opposingCaseDifficulty: number;
  curabilityOfGaps: number;
  appellateForumTrend: number;
  totalScore: number;
  probabilityOfFavourableOutcome: OutcomeProbability;
  probabilityNote: string;
}

export interface ForwardLitigationDecision {
  currentReadinessScore: number;
  potentialScoreAfterRemediation: number;
  scoreEnhancers: string[];
  scoreReducers: string[];
  evidenceDependentImprovements: string[];
  nonCurableWeaknesses: string[];
  actionRequiredToAchievePotential: string[];
}

export interface DraftAuditDefect {
  id: string;
  parameter: string;
  issueDetected: string;
  recommendedCorrection: string;
  severity: 'Critical' | 'High' | 'Medium' | 'Low';
}

export interface FinalEvaluatorOutput {
  executiveVerdict: {
    litigationReadiness: number;
    litigationViability: number;
    recommendation: Recommendation;
    top5Reasons: string[];
  };
  strongestLegalParameters: string[];
  weakestParameters: string[];
  strongestGroundsOfChallenge: { ground: string; rank: number; strength: number }[];
  strongestOpposingArguments: string[];
  evidenceGapReport: string[];
  precedentMatrix: { precedent: string; applicability: string; score: number }[];
  lowerAuthorityErrorMatrix: { error: string; significance: string }[];
  draftDefects: { defect: string; severity: string }[];
  litigationImprovementPlan: {
    p0MustFixBeforeFiling: string[];
    p1StronglyRecommended: string[];
    p2AdditionalStrengthening: string[];
  };
  finalLitigationAssessment: {
    shouldProceed: boolean;
    proceedExplanation: string;
    singleBiggestRisk: string;
    singleStrongestAdvantage: string;
    evidenceMostNeeded: string;
    propositionRequiringCarefulDrafting: string;
  };
}

export interface CaseDocument {
  id: string;
  name: string;
  type: 'SCN' | 'DRC-01' | 'DRC-07' | 'Reply' | 'APL-01' | 'Invoice' | 'E-Way Bill' | 'GSTR-1' | 'GSTR-2A' | 'GSTR-2B' | 'GSTR-3B' | 'Bank Statement' | 'Ledger' | 'Transporter Bilty' | 'CA Certificate' | 'Other';
  fileSize: string;
  uploadedAt: string;
  ocrReadability: OcrReadability;
  extractedTextSnippet: string;
}

export interface CaseStudy {
  id: string;
  title: string;
  taxpayerName: string;
  gstin: string;
  financialYear: string;
  disputedAmount: string;
  noticeType: 'SCN / DRC-01' | 'Order-in-Original / DRC-07' | 'First Appeal / APL-01' | 'High Court Writ Petition';
  primaryIssue: string;
  summary: string;
  documents: CaseDocument[];
  
  factMatrix: FactMatrixItem[];
  statutoryParameters: StatutoryParameter[];
  precedents: PrecedentAnalysis[];
  lowerAuthorityErrors: LowerAuthorityError[];
  improvedSubmissions: ImprovedSubmissionGround[];
  redTeamItems: AdversarialRedTeamItem[];
  evidenceGaps: EvidenceGapItem[];
  readinessScore: ReadinessScoreBreakdown;
  viabilityScore: ViabilityScoreBreakdown;
  forwardDecision: ForwardLitigationDecision;
  draftAudit: DraftAuditDefect[];
  finalOutput: FinalEvaluatorOutput;
}

export const CaseEvaluationRequestSchema = z.object({
  caseId: z.string().optional(),
  title: z.string().min(3),
  taxpayerName: z.string().min(2),
  gstin: z.string().min(10),
  financialYear: z.string(),
  disputedAmount: z.string(),
  noticeType: z.enum(['SCN / DRC-01', 'Order-in-Original / DRC-07', 'First Appeal / APL-01', 'High Court Writ Petition']),
  primaryIssue: z.string(),
  caseSummary: z.string(),
  geminiApiKey: z.string().optional(),
  documents: z.array(z.any()).optional(),
  documentTexts: z.array(z.object({
    name: z.string(),
    type: z.string(),
    content: z.string(),
    ocrStatus: z.string().optional()
  })).optional()
});

export type CaseEvaluationRequest = z.infer<typeof CaseEvaluationRequestSchema>;
