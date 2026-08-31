import { CaseStudy } from '../types';
import { BENCHMARK_CASES } from './benchmark-data';
import { pool, initDbSchema } from './db';

let casesCache: Map<string, CaseStudy> = new Map();
BENCHMARK_CASES.forEach(c => casesCache.set(c.id, c));

export async function getAllCases(): Promise<CaseStudy[]> {
  try {
    const isDbReady = await initDbSchema();
    if (isDbReady) {
      const res = await pool.query('SELECT case_data FROM ngtp.cases ORDER BY updated_at DESC');
      if (res.rows.length > 0) {
        res.rows.forEach(r => {
          const c: CaseStudy = r.case_data;
          casesCache.set(c.id, c);
        });
      } else {
        for (const bCase of BENCHMARK_CASES) {
          await saveCase(bCase);
        }
      }
    }
  } catch (err: any) {
    console.warn('⚠️ [CaseRepo] Reading from local in-memory cache:', err.message);
  }
  return Array.from(casesCache.values());
}

export async function getCaseById(id: string): Promise<CaseStudy | null> {
  if (casesCache.has(id)) {
    return casesCache.get(id)!;
  }
  try {
    const isDbReady = await initDbSchema();
    if (isDbReady) {
      const res = await pool.query('SELECT case_data FROM ngtp.cases WHERE id = $1', [id]);
      if (res.rows.length > 0) {
        const c: CaseStudy = res.rows[0].case_data;
        casesCache.set(c.id, c);
        return c;
      }
    }
  } catch (err: any) {
    console.warn('⚠️ [CaseRepo] DB read fallback for ID:', id, err.message);
  }
  return null;
}

export async function saveCase(caseData: CaseStudy): Promise<CaseStudy> {
  casesCache.set(caseData.id, caseData);
  try {
    const isDbReady = await initDbSchema();
    if (isDbReady) {
      await pool.query(`
        INSERT INTO ngtp.cases (id, title, taxpayer_name, gstin, financial_year, disputed_amount, notice_type, primary_issue, summary, case_data, updated_at)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, CURRENT_TIMESTAMP)
        ON CONFLICT (id) DO UPDATE SET
          title = EXCLUDED.title,
          taxpayer_name = EXCLUDED.taxpayer_name,
          gstin = EXCLUDED.gstin,
          financial_year = EXCLUDED.financial_year,
          disputed_amount = EXCLUDED.disputed_amount,
          notice_type = EXCLUDED.notice_type,
          primary_issue = EXCLUDED.primary_issue,
          summary = EXCLUDED.summary,
          case_data = EXCLUDED.case_data,
          updated_at = CURRENT_TIMESTAMP;
      `, [
        caseData.id,
        caseData.title,
        caseData.taxpayerName,
        caseData.gstin,
        caseData.financialYear,
        caseData.disputedAmount,
        caseData.noticeType,
        caseData.primaryIssue,
        caseData.summary,
        JSON.stringify(caseData)
      ]);

      await pool.query(`
        INSERT INTO ngtp.audit_logs (case_id, action, payload)
        VALUES ($1, $2, $3);
      `, [
        caseData.id,
        'CASE_SAVED_OR_EVALUATED',
        JSON.stringify({ title: caseData.title, readiness: caseData.readinessScore.totalScore, viability: caseData.viabilityScore.totalScore })
      ]);
    }
  } catch (err: any) {
    console.warn('⚠️ [CaseRepo] DB save fallback to cache:', err.message);
  }
  return caseData;
}
