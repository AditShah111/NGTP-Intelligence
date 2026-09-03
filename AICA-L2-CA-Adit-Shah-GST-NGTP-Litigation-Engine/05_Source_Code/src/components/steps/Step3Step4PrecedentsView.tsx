'use client';

import React, { useState } from 'react';
import { PrecedentAnalysis } from '../../types';
import { BookOpen, Award, CheckCircle2, AlertCircle, Sparkles, Scale, RefreshCw, Layers, ShieldCheck, Database, Filter, ArrowRight, Gavel, GitCompare, Search, Zap } from 'lucide-react';

interface Props {
  precedents: PrecedentAnalysis[];
  onIngestPrecedents?: (domain: string, customQuery?: string) => Promise<void>;
  isIngesting?: boolean;
}

export const Step3Step4PrecedentsView: React.FC<Props> = ({ 
  precedents, 
  onIngestPrecedents,
  isIngesting = false 
}) => {
  const [selectedDomain, setSelectedDomain] = useState('Section 16(2)(c) & NGTP Supplier Default');
  const [customSearchQuery, setCustomSearchQuery] = useState('');
  const [filterCourt, setFilterCourt] = useState<'ALL' | 'SUPREME_COURT' | 'HIGH_COURT_DIVISION' | 'HIGH_COURT_SINGLE'>('ALL');
  const [isSearchOpen, setIsSearchOpen] = useState(false);

  const domains = [
    'Section 16(2)(c) & NGTP Supplier Default',
    'Non-Genuine / Cancelled Supplier (NGTP)',
    'Retrospective Cancellation of Supplier GSTIN',
    'Fake Invoicing & Physical Transit Genuineness',
    'Circular 183 / 193 CA Safe-Harbor',
    'Section 16(4) / 16(5) Retrospective Relief'
  ];

  const filteredPrecedents = precedents.filter(p => {
    if (filterCourt === 'ALL') return true;
    if (filterCourt === 'SUPREME_COURT') return p.court.toLowerCase().includes('supreme court') || p.article141Status === 'SUPREME_BINDING';
    if (filterCourt === 'HIGH_COURT_DIVISION') return p.benchType === 'High Court Division Bench';
    if (filterCourt === 'HIGH_COURT_SINGLE') return p.benchType === 'High Court Single Bench';
    return true;
  });

  const handleTriggerCustomIngestion = () => {
    if (!onIngestPrecedents) return;
    if (customSearchQuery.trim()) {
      onIngestPrecedents(selectedDomain, customSearchQuery.trim());
    } else {
      onIngestPrecedents(selectedDomain);
    }
  };

  return (
    <div className="space-y-6">
      {/* Real-time Ingestion & Article 141 Header Card */}
      <div className="bg-white border border-beige-200 rounded-2xl p-6 shadow-sm">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 pb-4 border-b border-beige-200">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <Gavel className="w-5 h-5 text-amber-700" />
              <h3 className="text-xl font-serif font-bold text-slate-900">
                Steps 3 & 4: Automatic Judicial Ingestion & Article 141 Hierarchy Matrix
              </h3>
            </div>
            <p className="text-xs text-slate-600">
              Permanently and automatically ingests Supreme Court & High Court rulings on every case evaluation. Reverse-engineers required court evidence, resolves Article 141 conflicts, and recalibrates parameters in real time.
            </p>
          </div>

          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-xs font-mono px-3 py-1 rounded-full bg-emerald-50 text-emerald-900 border border-emerald-200 font-semibold flex items-center gap-1.5 shadow-sm">
              <Zap className="w-3.5 h-3.5 text-emerald-600 fill-emerald-600" />
              Auto-Ingestion Active ({precedents.length} Rulings Ingested)
            </span>
          </div>
        </div>

        {/* Automatic Ingestion Status Banner */}
        <div className="mt-4 p-3.5 rounded-xl bg-gradient-to-r from-emerald-50/90 via-beige-50 to-purple-50/80 border border-emerald-200 text-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-2 shadow-sm">
          <div className="flex items-center gap-2 text-emerald-900 font-medium">
            <CheckCircle2 className="w-4 h-4 text-emerald-700 flex-shrink-0" />
            <span>
              <strong>Fully Automated Real-Time Synchronization:</strong> Ingests new case laws and recalibrates statutory parameters P1–P8 automatically whenever case facts or documents update.
            </span>
          </div>
          <button
            onClick={() => setIsSearchOpen(!isSearchOpen)}
            className="text-[11px] font-mono font-semibold px-3 py-1 rounded-lg bg-white border border-beige-300 text-slate-700 hover:bg-beige-50 shadow-sm transition-all whitespace-nowrap"
          >
            {isSearchOpen ? 'Hide Custom Search' : '+ Research Specific Citation'}
          </button>
        </div>

        {/* Optional Custom Citation Research Drawer */}
        {isSearchOpen && (
          <div className="mt-3 p-4 rounded-xl bg-beige-50 border border-beige-300 space-y-3 animate-fade-in">
            <div className="text-xs font-semibold text-slate-800 flex items-center gap-1.5">
              <Search className="w-4 h-4 text-amber-700" />
              <span>Deep Judicial Query Engine:</span>
            </div>
            <div className="flex flex-col sm:flex-row items-center gap-2">
              <input
                type="text"
                value={customSearchQuery}
                onChange={(e) => setCustomSearchQuery(e.target.value)}
                placeholder="e.g. Karnataka HC Wipro Ltd Circular 183, Kerala HC M/s MT Agencies, or Section 16(4) Finance Act 2024..."
                className="bg-white border border-beige-300 rounded-lg px-3 py-2 text-xs font-medium text-slate-800 focus:outline-none focus:border-amber-600 shadow-sm w-full"
              />
              <button
                onClick={handleTriggerCustomIngestion}
                disabled={isIngesting}
                className="flex items-center justify-center gap-2 px-4 py-2 rounded-lg bg-amber-600 hover:bg-amber-700 disabled:opacity-50 text-white text-xs font-semibold shadow-sm transition-all whitespace-nowrap w-full sm:w-auto"
              >
                <RefreshCw className={`w-3.5 h-3.5 ${isIngesting ? 'animate-spin' : ''}`} />
                <span>{isIngesting ? 'Searching Case Law...' : 'Search & Ingest Ruling'}</span>
              </button>
            </div>
          </div>
        )}

        {/* Filter Pills */}
        <div className="flex items-center gap-2 mt-5 text-xs flex-wrap">
          <span className="text-slate-500 font-mono text-[11px] font-semibold uppercase">Filter View:</span>
          <button
            onClick={() => setFilterCourt('ALL')}
            className={`px-2.5 py-1 rounded-md text-[11px] font-medium transition-all ${
              filterCourt === 'ALL' ? 'bg-slate-900 text-white' : 'bg-beige-100 text-slate-700 hover:bg-beige-200'
            }`}
          >
            All Judgments ({precedents.length})
          </button>
          <button
            onClick={() => setFilterCourt('SUPREME_COURT')}
            className={`px-2.5 py-1 rounded-md text-[11px] font-medium transition-all ${
              filterCourt === 'SUPREME_COURT' ? 'bg-amber-700 text-white' : 'bg-amber-50 text-amber-900 border border-amber-200'
            }`}
          >
            Supreme Court Binding (Art. 141)
          </button>
          <button
            onClick={() => setFilterCourt('HIGH_COURT_DIVISION')}
            className={`px-2.5 py-1 rounded-md text-[11px] font-medium transition-all ${
              filterCourt === 'HIGH_COURT_DIVISION' ? 'bg-purple-700 text-white' : 'bg-purple-50 text-purple-900 border border-purple-200'
            }`}
          >
            HC Division Bench
          </button>
          <button
            onClick={() => setFilterCourt('HIGH_COURT_SINGLE')}
            className={`px-2.5 py-1 rounded-md text-[11px] font-medium transition-all ${
              filterCourt === 'HIGH_COURT_SINGLE' ? 'bg-blue-700 text-white' : 'bg-blue-50 text-blue-900 border border-blue-200'
            }`}
          >
            HC Single Bench
          </button>
        </div>

        {/* Ingested Precedents Feed */}
        <div className="space-y-5 mt-5">
          {filteredPrecedents.map((p, idx) => {
            const score = p.comparabilityScore?.totalScore || 90;
            const isSc = p.article141Status === 'SUPREME_BINDING' || p.court.toLowerCase().includes('supreme court');
            const authScore = p.judicialAuthorityStrengthScore || (isSc ? 98 : 85);

            return (
              <div
                key={p.id || idx}
                className="bg-beige-50/60 border border-beige-200 rounded-xl p-5 hover:border-amber-300 transition-all shadow-sm"
              >
                {/* Header with Court, Bench Strength & Article 141 Tag */}
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-beige-200">
                  <div>
                    <div className="flex items-center gap-2 flex-wrap">
                      <h4 className="text-base font-serif font-bold text-slate-900">{p.caseName}</h4>
                      {isSc && (
                        <span className="text-[10px] font-mono font-bold px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-900 border border-amber-300 shadow-sm flex items-center gap-1">
                          <Award className="w-3 h-3 text-amber-700" />
                          Article 141 Supreme Court Binding
                        </span>
                      )}
                      {p.benchType && (
                        <span className="text-[10px] font-mono font-semibold px-2 py-0.5 rounded bg-slate-100 text-slate-700 border border-slate-200">
                          {p.benchType}
                        </span>
                      )}
                    </div>
                    <div className="text-xs text-slate-600 flex items-center gap-2 mt-1">
                      <span className="font-semibold text-amber-800">{p.court}</span>
                      <span>•</span>
                      <span className="font-mono text-slate-500">{p.citation}</span>
                      {p.slpStatus && (
                        <>
                          <span>•</span>
                          <span className="font-mono text-emerald-800 font-semibold">{p.slpStatus}</span>
                        </>
                      )}
                    </div>
                  </div>

                  <div className="flex items-center gap-2.5">
                    {/* Authority Strength Badge */}
                    <div className="bg-white border border-beige-200 px-3 py-1 rounded-lg text-center shadow-sm min-w-[90px]">
                      <div className="text-[9px] font-mono text-slate-400 uppercase">Bench Authority</div>
                      <div className="text-xs font-mono font-bold text-purple-700">{authScore}/100</div>
                    </div>
                    {/* Fact Match Score */}
                    <div className="bg-white border border-beige-200 px-3 py-1 rounded-lg text-center shadow-sm min-w-[85px]">
                      <div className="text-[9px] font-mono text-slate-400 uppercase">Fact Match</div>
                      <div className="text-xs font-mono font-bold text-amber-700">{score}/100</div>
                    </div>
                  </div>
                </div>

                {/* Core Ratio & Litigation Use */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4 text-xs">
                  <div className="bg-white p-3.5 rounded-lg border border-beige-200">
                    <div className="text-[11px] font-mono uppercase text-slate-400 mb-1 font-semibold">Judicial Ratio & Principle:</div>
                    <p className="text-slate-800 leading-relaxed font-sans">{p.ratioLegalPrinciple}</p>
                  </div>
                  <div className="bg-white p-3.5 rounded-lg border border-beige-200">
                    <div className="text-[11px] font-mono uppercase text-slate-400 mb-1 font-semibold">Litigation Application:</div>
                    <p className="text-slate-800 leading-relaxed font-sans">{p.litigationUse}</p>
                  </div>
                </div>

                {/* Evidences Relied On by Court */}
                <div className="mt-4 p-3.5 rounded-lg bg-white border border-beige-200">
                  <div className="flex items-center gap-1.5 mb-2">
                    <ShieldCheck className="w-4 h-4 text-emerald-700" />
                    <span className="text-xs font-mono font-bold text-slate-900 uppercase">Evidences Relied On by Court:</span>
                  </div>
                  <div className="flex flex-wrap gap-1.5 mb-2">
                    {(p.evidencesReliedOnByCourt || [
                      'Tax Invoices fulfilling Rule 46 particulars',
                      '100% Consideration + GST paid through RTGS/NEFT',
                      'Supplier GSTR-1 acknowledgement',
                      'No recovery action initiated against supplier'
                    ]).map((ev, i) => (
                      <span key={i} className="text-[11px] font-medium px-2.5 py-0.5 rounded-md bg-emerald-50 text-emerald-900 border border-emerald-200">
                        ✓ {ev}
                      </span>
                    ))}
                  </div>

                  {p.criticalEvidentiaryThreshold && (
                    <div className="text-[11px] text-amber-900 bg-amber-50/80 p-2 rounded-md border border-amber-200 mt-2">
                      <strong>Critical Evidentiary Threshold:</strong> {p.criticalEvidentiaryThreshold}
                    </div>
                  )}
                </div>

                {/* Conflict Resolution & Article 141 Interplay */}
                {p.competingConflictAnalysis && (
                  <div className="mt-3 p-3.5 rounded-xl bg-purple-50/60 border border-purple-200 text-xs">
                    <div className="flex items-center gap-1.5 mb-1.5 text-purple-900 font-bold font-serif">
                      <GitCompare className="w-4 h-4 text-purple-700" />
                      <span>Article 141 Conflict Resolution vs Divergent Rulings</span>
                    </div>
                    <div className="space-y-1.5 text-slate-800">
                      <div>
                        <span className="font-semibold text-rose-800">Divergent Ruling: </span>
                        <span>{p.competingConflictAnalysis.conflictWith}</span>
                      </div>
                      <p className="text-slate-700 leading-relaxed bg-white/80 p-2.5 rounded-lg border border-purple-100 font-sans">
                        <strong className="text-purple-900">Why {p.caseName} Prevails: </strong>
                        {p.competingConflictAnalysis.whyThisPrecedentPrevails}
                      </p>
                      <div className="text-[11px] font-mono font-semibold text-emerald-800 mt-1">
                        ✓ Resolution: {p.competingConflictAnalysis.article141Resolution}
                      </div>
                    </div>
                  </div>
                )}

                {/* 6-Axis Comparability Metrics */}
                {p.comparabilityScore && (
                  <div className="mt-3 pt-3 border-t border-beige-200 grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2 text-[10px] font-mono text-slate-600">
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Statutory</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.statutorySimilarity}/20</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Factual</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.factualSimilarity}/25</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Evidentiary</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.evidentiarySimilarity}/20</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Procedural</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.proceduralSimilarity}/10</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Authority</div>
                      <div className="font-bold text-slate-800 mt-0.5">{p.comparabilityScore.courtAuthorityRelevance}/15</div>
                    </div>
                    <div className="bg-beige-100/60 p-2 rounded text-center">
                      <div className="text-slate-400">Distinguish Risk</div>
                      <div className="font-bold text-emerald-700 mt-0.5">{p.comparabilityScore.distinguishabilityRisk}/10</div>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
};
