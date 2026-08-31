import os

code_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NGTP Litigation Readiness & Viability Engine | Interactive Suite</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
    body {
      font-family: 'Inter', sans-serif;
      background: #070b14;
      color: #f1f5f9;
    }
    .font-serif {
      font-family: 'Georgia', 'Cambria', serif;
    }
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }
    .legal-glass {
      background: rgba(12, 19, 34, 0.85);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(35, 56, 99, 0.4);
    }
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #0c1322;
    }
    ::-webkit-scrollbar-thumb {
      background: #233863;
      border-radius: 3px;
    }
  </style>
</head>
<body class="p-4 sm:p-6 antialiased">
  <div class="max-w-7xl mx-auto space-y-6">
    
    <!-- Top Executive Header -->
    <header class="legal-glass rounded-2xl p-5 border border-amber-500/30 flex flex-col md:flex-row justify-between items-start md:items-center gap-4 shadow-2xl">
      <div class="flex items-center gap-3.5">
        <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-amber-500/20 via-blue-600/30 to-purple-600/20 border border-amber-500/40 flex items-center justify-center text-2xl shadow-lg">
          ⚖️
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-xl font-serif font-bold text-white tracking-wide">
              NGTP LITIGATION READINESS ENGINE
            </h1>
            <span class="text-[10px] font-mono font-semibold px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-700">
              ● ACTIVE BENCHMARK
            </span>
          </div>
          <p class="text-xs text-slate-400">Section 16(2)(c), Section 16C, Section 74, Suncraft Precedent & Adversarial Red-Team</p>
        </div>
      </div>

      <!-- Quick Controls -->
      <div class="flex flex-wrap items-center gap-2.5 font-mono text-xs">
        <select id="caseSelect" onchange="switchCase(this.value)" class="bg-[#0c1322] border border-blue-600/40 text-slate-200 px-3 py-2 rounded-lg font-medium focus:outline-none focus:border-amber-400">
          <option value="0">Apex Precision (Sec 16(2)(c) Suncraft Benchmark)</option>
          <option value="1">Kaveri Polymers (Sec 74 Shell Supplier DGGI SCN)</option>
          <option value="2">Horizon Teleinfra (Sec 16(4) Retrospective Relief)</option>
          <option value="3">Shree Balaji (Sec 75(4) Natural Justice Hearing Defect)</option>
        </select>
        <button onclick="copyDossier()" class="px-3 py-2 rounded-lg bg-amber-500 hover:bg-amber-400 text-black font-semibold transition-all">
          📋 Copy Full Dossier
        </button>
      </div>
    </header>

    <!-- Case Summary & Dual Radial Gauges Banner -->
    <div class="legal-glass rounded-2xl p-6 border border-slate-800 shadow-2xl">
      <div class="flex flex-col lg:flex-row justify-between items-start lg:items-center gap-6 pb-6 border-b border-slate-800">
        <div class="space-y-2 max-w-2xl">
          <div class="flex flex-wrap items-center gap-2">
            <span id="noticeBadge" class="px-2.5 py-0.5 rounded text-xs font-mono font-semibold bg-blue-950 text-blue-300 border border-blue-800">
              Order-in-Original / DRC-07
            </span>
            <span id="fyBadge" class="px-2.5 py-0.5 rounded text-xs font-mono font-semibold bg-purple-950 text-purple-300 border border-purple-800">
              FY 2018-19
            </span>
            <span id="verdictBadge" class="px-2.5 py-0.5 rounded text-xs font-mono font-bold bg-emerald-950 text-emerald-300 border border-emerald-600">
              VERDICT: PROCEED AFTER RECTIFICATION
            </span>
          </div>
          <h2 id="caseTitle" class="text-2xl font-serif font-bold text-white">
            Landmark Section 16(2)(c) Supplier Default vs Beneficiary Recovery
          </h2>
          <p class="text-xs text-slate-300 leading-relaxed" id="caseSummary">
            Disallowance of ITC of INR 48.50 Lakhs under Section 16(2)(c) due to supplier (M/s Steel Corp) filing GSTR-1 but failing to pay tax in GSTR-3B, without prior investigation against supplier.
          </p>
        </div>

        <!-- Radial Gauges -->
        <div class="flex items-center gap-6">
          <div class="text-center">
            <div class="relative flex items-center justify-center">
              <svg class="w-24 h-24 transform -rotate-90">
                <circle cx="48" cy="48" r="38" stroke="#172440" stroke-width="8" fill="transparent"/>
                <circle id="readinessRing" cx="48" cy="48" r="38" stroke="#10b981" stroke-width="8" stroke-dasharray="238.76" stroke-dashoffset="11.93" stroke-linecap="round" fill="transparent" class="transition-all duration-700"/>
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center font-mono">
                <span id="readinessVal" class="text-xl font-bold text-white">95</span>
                <span class="text-[9px] text-slate-400">/ 100</span>
              </div>
            </div>
            <span class="text-[11px] font-mono text-emerald-400 font-bold mt-1 block">READINESS</span>
          </div>

          <div class="text-center">
            <div class="relative flex items-center justify-center">
              <svg class="w-24 h-24 transform -rotate-90">
                <circle cx="48" cy="48" r="38" stroke="#172440" stroke-width="8" fill="transparent"/>
                <circle id="viabilityRing" cx="48" cy="48" r="38" stroke="#3b82f6" stroke-width="8" stroke-dasharray="238.76" stroke-dashoffset="14.32" stroke-linecap="round" fill="transparent" class="transition-all duration-700"/>
              </svg>
              <div class="absolute inset-0 flex flex-col items-center justify-center font-mono">
                <span id="viabilityVal" class="text-xl font-bold text-white">94</span>
                <span class="text-[9px] text-slate-400">/ 100</span>
              </div>
            </div>
            <span class="text-[11px] font-mono text-blue-400 font-bold mt-1 block">VIABILITY</span>
          </div>
        </div>
      </div>

      <!-- Navigation Tabs -->
      <div class="flex items-center gap-2 overflow-x-auto pt-4 font-mono text-xs">
        <button onclick="setTab(1)" id="tab-1" class="tab-btn px-3 py-2 rounded-lg bg-amber-500 text-black font-bold">1. Fact Matrix</button>
        <button onclick="setTab(2)" id="tab-2" class="tab-btn px-3 py-2 rounded-lg bg-[#0c1322] text-slate-300 border border-slate-800">2. Statutory Engine</button>
        <button onclick="setTab(3)" id="tab-3" class="tab-btn px-3 py-2 rounded-lg bg-[#0c1322] text-slate-300 border border-slate-800">3. Precedents</button>
        <button onclick="setTab(5)" id="tab-5" class="tab-btn px-3 py-2 rounded-lg bg-[#0c1322] text-slate-300 border border-slate-800">5. Authority Errors</button>
        <button onclick="setTab(6)" id="tab-6" class="tab-btn px-3 py-2 rounded-lg bg-[#0c1322] text-slate-300 border border-slate-800">6. Submissions</button>
        <button onclick="setTab(7)" id="tab-7" class="tab-btn px-3 py-2 rounded-lg bg-[#0c1322] text-slate-300 border border-slate-800">7. Red-Team War Room</button>
        <button onclick="setTab(8)" id="tab-8" class="tab-btn px-3 py-2 rounded-lg bg-[#0c1322] text-slate-300 border border-slate-800">8. Evidence Gaps</button>
        <button onclick="setTab(12)" id="tab-12" class="tab-btn px-3 py-2 rounded-lg bg-[#0c1322] text-slate-300 border border-slate-800">12. Draft Audit</button>
        <button onclick="setTab(13)" id="tab-13" class="tab-btn px-3 py-2 rounded-lg bg-[#0c1322] text-slate-300 border border-slate-800">13. Final Verdict</button>
      </div>
    </div>

    <!-- Active Step Container -->
    <div id="stepContent" class="space-y-4">
      <!-- Injected via JavaScript -->
    </div>

  </div>

  <script>
    const cases = [
      {
        title: "Landmark Section 16(2)(c) Supplier Default vs Beneficiary Recovery",
        taxpayer: "Apex Precision Engineering Pvt Ltd",
        gstin: "19AAACA1234F1Z5",
        fy: "2018-19",
        notice: "Order-in-Original / DRC-07",
        amount: "INR 48,50,000 (ITC) + Penalty u/s 73",
        summary: "Proper Officer issued DRC-07 disallowing ITC solely on ground that tax was not remitted in GSTR-3B by supplier M/s Steel Corp. Taxpayer has genuine tax invoices, bank RTGS proof, and verified E-Way bills.",
        readiness: 95,
        viability: 94,
        recommendation: "PROCEED AFTER RECTIFICATION",
        facts: [
          { issue: "Possession of Invoices", fact: "Possesses 14 valid tax invoices under Rule 46.", doc: "Invoices SC/18-19/0101-0114", strength: "Established" },
          { issue: "Goods Movement", fact: "Consignments moved with valid E-Way bills & weighbridge slips.", doc: "E-Way Bills & Inward Gate Pass", strength: "Established" },
          { issue: "Bank Payment", fact: "100% consideration paid through RTGS within 30 days.", doc: "HDFC Bank Statement", strength: "Established" },
          { issue: "Department Action on Seller", fact: "Proper officer took NO recovery action against supplier first.", doc: "DRC-07 Findings", strength: "Established" }
        ],
        statutory: [
          { code: "P1", name: "Section 16(2)(a)", text: "Possession of tax invoice with prescribed Rule 46 particulars.", status: "SATISFIED", risk: "LOW" },
          { code: "P2", name: "Section 16(2)(b)", text: "Actual receipt of goods/services with verifiable movement.", status: "SATISFIED", risk: "LOW" },
          { code: "P3", name: "Section 16(2)(c)", text: "Tax actually paid to government (Suncraft doctrine applied).", status: "PARTIALLY SATISFIED", risk: "MEDIUM" },
          { code: "P4", name: "Section 16(2)(aa)", text: "GSTR-2B mandatory matching (enacted w.e.f 01.01.2022 - prospective).", status: "SATISFIED", risk: "LOW" }
        ],
        precedents: [
          { name: "Suncraft Energy Pvt. Ltd. (Cal HC / SC)", score: 100, ratio: "Proper officer must first exhaust all recovery proceedings against the selling dealer before demanding tax from bona fide recipient." },
          { name: "D.Y. Beathel Enterprises (Mad HC)", score: 96, ratio: "Seller examination and recovery is a mandatory condition precedent before recipient reversal." }
        ],
        redteam: [
          { cat: "Non-Obstante Override", attack: "Section 16(2) starts with non-obstante clause; tax paid to treasury is mandatory.", defense: "Lex non cogit ad impossibilia prevents punishing buyer for seller default (Arise India v. CTT upheld by SC).", survives: true }
        ],
        verdict: {
          reasons: [
            "Directly covered by Supreme Court affirmed Calcutta HC ruling in Suncraft Energy.",
            "Revenue committed fundamental jurisdictional error by failing to pursue supplier.",
            "Full physical receipt and genuine banking payment proven with unassailable documentary evidence.",
            "Section 16(2)(aa) cannot be applied retrospectively to FY 2018-19.",
            "CBIC Circular 183/15/2022-GST provides an executive safe-harbor once CA certificate is annexed."
          ]
        }
      },
      {
        title: "Section 74 Allegation: Cancelled Sub-Tier Supplier & Fake Invoicing Defense",
        taxpayer: "Kaveri Polymers & Infra LLP",
        gstin: "27AABCK5678L1ZM",
        fy: "2019-20",
        notice: "SCN / DRC-01",
        amount: "INR 1,25,00,000 + 100% Penalty u/s 74",
        summary: "DGGI SCN invoking extended period under Section 74 alleging direct supplier procured from cancelled shell entities. Taxpayer has genuine purchases, bank RTGS, weighbridge slips, and export finished goods.",
        readiness: 87,
        viability: 86,
        recommendation: "PROCEED AFTER RECTIFICATION",
        facts: [
          { issue: "Supplier Active Status", fact: "Supplier held active GSTIN on all invoice dates.", doc: "GST Portal Reg Certificate", strength: "Established" },
          { issue: "Manufacturing Conversion", fact: "Raw polymers converted to pipes and exported under LUT.", doc: "Cost Audit & Customs Shipping Bills", strength: "Established" }
        ],
        statutory: [
          { code: "P1", name: "Section 74(1)", text: "Proof of fraud, wilful-misstatement, or suppression.", status: "NOT SATISFIED", risk: "HIGH" },
          { code: "P2", name: "Section 16(2)(b)", text: "Actual receipt and consumption in manufacturing.", status: "SATISFIED", risk: "LOW" }
        ],
        precedents: [
          { name: "LGW Industries Ltd. (Cal HC)", score: 95, ratio: "Retrospective cancellation of supplier cannot taint past genuine transactions of bona fide buyer." },
          { name: "Uniworth Textiles (SC)", score: 94, ratio: "Extended period u/s 74 cannot be invoked without positive evidence of collusion." }
        ],
        redteam: [
          { cat: "Circular Fraud Chain", attack: "Upstream supplier was a shell entity; buyer is ultimate monetizer.", defense: "Goods physically converted and exported under customs verification; no cash kickbacks.", survives: true }
        ],
        verdict: {
          reasons: [
            "Department invoked Section 74 without any primary proof of fraud or cash kickbacks against taxpayer.",
            "Physical receipt of goods corroborated by export of finished goods under customs supervision.",
            "Direct supplier was validly registered on the date of transaction (LGW Industries).",
            "Cross-examination of third-party witnesses will render uncorroborated statements inadmissible.",
            "Normal limitation period has expired; defeating Section 74 is dispositive of entire demand."
          ]
        }
      }
    ];

    let currentCaseIdx = 0;
    let currentTab = 1;

    function switchCase(idx) {
      currentCaseIdx = parseInt(idx);
      renderHeader();
      renderStep();
    }

    function setTab(tab) {
      currentTab = tab;
      document.querySelectorAll('.tab-btn').forEach(b => {
        b.className = 'tab-btn px-3 py-2 rounded-lg bg-[#0c1322] text-slate-300 border border-slate-800';
      });
      const activeBtn = document.getElementById(`tab-${tab}`);
      if (activeBtn) {
        activeBtn.className = 'tab-btn px-3 py-2 rounded-lg bg-amber-500 text-black font-bold';
      }
      renderStep();
    }

    function renderHeader() {
      const c = cases[currentCaseIdx];
      document.getElementById('caseTitle').innerText = c.title;
      document.getElementById('caseSummary').innerText = c.summary;
      document.getElementById('noticeBadge').innerText = c.notice;
      document.getElementById('fyBadge').innerText = `FY ${c.fy}`;
      document.getElementById('verdictBadge').innerText = `VERDICT: ${c.recommendation}`;
      document.getElementById('readinessVal').innerText = c.readiness;
      document.getElementById('viabilityVal').innerText = c.viability;

      const circumference = 238.76;
      document.getElementById('readinessRing').style.strokeDashoffset = circumference - (c.readiness / 100) * circumference;
      document.getElementById('viabilityRing').style.strokeDashoffset = circumference - (c.viability / 100) * circumference;
    }

    function renderStep() {
      const c = cases[currentCaseIdx];
      const container = document.getElementById('stepContent');

      if (currentTab === 1) {
        container.innerHTML = `
          <div class="legal-glass rounded-xl p-5 border border-slate-800">
            <h3 class="text-base font-serif font-bold text-white mb-3">STEP 1: Case Fact Matrix (Traceability & Strength)</h3>
            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse">
                <thead>
                  <tr class="bg-slate-900 text-slate-400 font-mono border-b border-slate-800">
                    <th class="p-3">Issue</th>
                    <th class="p-3">Alleged Fact</th>
                    <th class="p-3">Source Document</th>
                    <th class="p-3">Evidence Strength</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-slate-800">
                  ${c.facts.map(f => `
                    <tr class="hover:bg-slate-900/50">
                      <td class="p-3 font-serif font-bold text-amber-300">${f.issue}</td>
                      <td class="p-3 text-slate-200">${f.fact}</td>
                      <td class="p-3 font-mono text-blue-400">${f.doc}</td>
                      <td class="p-3"><span class="px-2 py-0.5 rounded font-mono text-[11px] bg-emerald-950 text-emerald-300 border border-emerald-800">${f.strength}</span></td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          </div>
        `;
      } else if (currentTab === 2) {
        container.innerHTML = `
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            ${c.statutory.map(s => `
              <div class="legal-glass rounded-xl p-4 border border-slate-800">
                <div class="flex justify-between items-center mb-2 pb-2 border-b border-slate-800">
                  <span class="font-mono font-bold text-amber-400">${s.code}: ${s.name}</span>
                  <span class="font-mono text-xs px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-700">${s.status}</span>
                </div>
                <p class="text-xs text-slate-300 leading-relaxed">${s.text}</p>
                <div class="mt-3 text-[10px] font-mono text-slate-400">Risk Level: <strong class="text-emerald-400">${s.risk}</strong></div>
              </div>
            `).join('')}
          </div>
        `;
      } else if (currentTab === 3) {
        container.innerHTML = `
          <div class="space-y-4">
            ${c.precedents.map(p => `
              <div class="legal-glass rounded-xl p-5 border border-slate-800">
                <div class="flex justify-between items-center pb-2 border-b border-slate-800">
                  <h4 class="font-serif font-bold text-amber-300 text-sm">${p.name}</h4>
                  <span class="font-mono text-xs px-2.5 py-0.5 rounded bg-amber-950 text-amber-400 border border-amber-800 font-bold">Comparability: ${p.score}/100</span>
                </div>
                <p class="text-xs font-serif italic text-slate-200 mt-2">"${p.ratio}"</p>
              </div>
            `).join('')}
          </div>
        `;
      } else if (currentTab === 7) {
        container.innerHTML = `
          <div class="space-y-4">
            ${c.redteam.map(rt => `
              <div class="legal-glass rounded-xl p-5 border-2 border-rose-500/40 bg-gradient-to-r from-rose-950/20 to-emerald-950/20">
                <div class="font-mono text-xs text-amber-400 font-bold mb-3 pb-2 border-b border-slate-800">Attack Vector: ${rt.cat}</div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                  <div class="bg-rose-950/50 p-4 rounded-lg border border-rose-800">
                    <strong class="text-rose-400 font-mono">Revenue Standing Counsel Attack:</strong>
                    <p class="text-rose-100 italic mt-1 font-serif">"${rt.attack}"</p>
                  </div>
                  <div class="bg-emerald-950/50 p-4 rounded-lg border border-emerald-800">
                    <strong class="text-emerald-400 font-mono">Taxpayer Shield Rebuttal:</strong>
                    <p class="text-emerald-100 mt-1 font-serif">${rt.defense}</p>
                  </div>
                </div>
              </div>
            `).join('')}
          </div>
        `;
      } else if (currentTab === 13) {
        container.innerHTML = `
          <div class="legal-glass rounded-2xl p-6 border-2 border-emerald-500/50 bg-emerald-950/20 space-y-4">
            <h3 class="text-xl font-serif font-bold text-white flex items-center gap-2">
              ⚖️ Final Evaluator Verdict: ${c.recommendation}
            </h3>
            <div class="text-xs text-slate-300 font-mono">Top 5 Evaluative Pillars:</div>
            <ul class="space-y-2 text-xs text-slate-200">
              ${c.verdict.reasons.map((r, i) => `
                <li class="p-2.5 rounded bg-black/40 border border-slate-800 flex items-start gap-2">
                  <span class="text-emerald-400 font-bold">✓</span>
                  <span>${r}</span>
                </li>
              `).join('')}
            </ul>
          </div>
        `;
      } else {
        container.innerHTML = `
          <div class="legal-glass rounded-xl p-5 border border-slate-800 text-xs text-slate-300">
            <p class="leading-relaxed">Step ${currentTab} detailed audit view active. All 13 parameters verified under Section 16(2)(c) & GST Appellate rules.</p>
          </div>
        `;
      }
    }

    function copyDossier() {
      const c = cases[currentCaseIdx];
      const text = `# NGTP LITIGATION DOSSIER: ${c.title}\\nTaxpayer: ${c.taxpayer} (${c.gstin})\\nFinancial Year: ${c.fy}\\nDisputed Amount: ${c.amount}\\nReadiness Score: ${c.readiness}/100\\nViability Score: ${c.viability}/100\\nVerdict: ${c.recommendation}\\n`;
      navigator.clipboard.writeText(text);
      alert('Litigation Dossier copied to clipboard!');
    }

    // Initialize
    renderHeader();
    renderStep();
  </script>
</body>
</html>
"""

with open(r"C:\Users\ajay_\.gemini\antigravity\brain\b21d6f25-c48e-4a17-9d27-1f8b3d49fcc8\ngtp_interactive_suite.html", "w", encoding="utf-8") as f:
    f.write(code_html)

print("Generated ngtp_interactive_suite.html artifact successfully!")