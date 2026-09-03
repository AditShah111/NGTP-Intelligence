with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Insert handleLoadDataset1 and handleLoadDataset2 right after handleCreateNewCaseFromModal
target = """    setIsNewCaseOpen(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };"""

replacement = """    setIsNewCaseOpen(false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Quick Load Dataset 1 (Proceed Worthy - Retrospective Cancellation)
  const handleLoadDataset1 = async () => {
    try {
      setIsParsingDoc(true);
      const res = await fetch('/sample-data/set1-proceed/Set1_Statement_of_Facts_and_Grounds.txt');
      const text = await res.text();
      setTitle('Apex Precision v. ACST LTU-1 Pune - Retrospective NGTP Cancellation FY 2018-19');
      setTaxpayerName('Apex Precision Engineering Pvt. Ltd.');
      setGstin('27AAACA9876C1Z3');
      setFinancialYear('2018-19');
      setDisputedAmount('INR 38,40,000');
      setNoticeType('Order-in-Original / DRC-07');
      setPrimaryIssue('Section 16(2)(c) ITC denial due to retrospective cancellation of supplier GSTIN even though tax was deposited via RTGS while registration was active');
      setWrittenSubmission(text);
      setUploadedDocuments([
        { id: 'doc-set1-1', name: 'Set1_Tax_Invoice_Rule46.pdf', type: 'Invoice', fileSize: '124 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'Tax Invoice DMA/2018-19/0402 Hot Rolled Steel Coils 40 MT Tax 38,40,000 Supplier GSTIN 27AABCD5544E1Z2 active on date' },
        { id: 'doc-set1-2', name: 'Set1_Bank_RTGS_Statement.pdf', type: 'Bank Statement', fileSize: '115 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'RTGS DEBIT UTR HDFCR52018102400918234 amount 2,51,73,333 paid in 12 days' },
        { id: 'doc-set1-3', name: 'Set1_EWay_Bill_PartA_B.pdf', type: 'E-Way Bill', fileSize: '98 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'E-Way Bill 241089201945 Vehicle MH-12-RN-7845 valid' },
        { id: 'doc-set1-4', name: 'Set1_Weighbridge_FASTag_Receipt.pdf', type: 'E-Way Bill', fileSize: '108 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'Weighbridge Slip DWB/18/10492 Net Weight 40040 Kg FASTag Toll Khalapur Kusgaon Talegaon' },
        { id: 'doc-set1-5', name: 'Set1_Tax_Ledger_GSTR1_Ack.pdf', type: 'Invoice', fileSize: '92 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'GSTR-1 ARN AA2710180918234 filed 10-11-2018' },
        { id: 'doc-set1-6', name: 'Set1_Impugned_DRC07_Order.pdf', type: 'DRC-07', fileSize: '118 KB', uploadedAt: '2024-04-10', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'DRC-07 Order ZA2703240098412 disallowing ITC due to retrospective cancellation' }
      ]);
      setActiveCase(null);
      setScopeRejection(null);
      setEvalError(null);
    } catch (e) {
      console.error(e);
    } finally {
      setIsParsingDoc(false);
    }
  };

  // Quick Load Dataset 2 (Not Worthy / HOLD - Missing Transit & 216-Day Delay)
  const handleLoadDataset2 = async () => {
    try {
      setIsParsingDoc(true);
      const res = await fetch('/sample-data/set2-hold/Set2_Statement_of_Facts_and_Grounds.txt');
      const text = await res.text();
      setTitle('Shaurya Infra v. DCST Nodal-7 Thane - Paper-Only Allegation FY 2019-20');
      setTaxpayerName('Shaurya Infra Projects Ltd.');
      setGstin('27AAACS4321D1Z8');
      setFinancialYear('2019-20');
      setDisputedAmount('INR 52,00,000');
      setNoticeType('Order-in-Original / DRC-07');
      setPrimaryIssue('Section 16(2)(c) circular trading allegation - NO e-way bill, NO transit proof, supplier fictitious 100 sq ft room, payment delayed 216 days beyond 180-day limit');
      setWrittenSubmission(text);
      setUploadedDocuments([
        { id: 'doc-set2-1', name: 'Set2_Tax_Invoice_Deficient.pdf', type: 'Invoice', fileSize: '102 KB', uploadedAt: '2024-04-15', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'Tax Invoice GTS/19-20/0118 building materials lump sum without vehicle or eway bill' },
        { id: 'doc-set2-2', name: 'Set2_Bank_Statement_Delayed.pdf', type: 'Bank Statement', fileSize: '105 KB', uploadedAt: '2024-04-15', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'Paid after 216 days delayed beyond 180 days statutory limit under Section 16(2)' },
        { id: 'doc-set2-3', name: 'Set2_Impugned_DRC07_Order.pdf', type: 'DRC-07', fileSize: '112 KB', uploadedAt: '2024-04-15', ocrReadability: 'Clearly readable text', extractedTextSnippet: 'DRC-07 Order ZA2701240049182 circular trading without movement of goods under Section 74' }
      ]);
      setActiveCase(null);
      setScopeRejection(null);
      setEvalError(null);
    } catch (e) {
      console.error(e);
    } finally {
      setIsParsingDoc(false);
    }
  };"""

code = code.replace(target, replacement)

# 2. Insert Quick Test Buttons inside the Matter Assessment Workspace header
btn_target = """            <div className="flex items-center gap-2 flex-wrap">
              {activeCase && (
                <button
                  onClick={handleResetWorkspace}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-beige-100 hover:bg-beige-200 text-slate-700 text-xs font-semibold transition-all shadow-sm"
                  title="Clear on-screen data back to blank form"
                >
                  <X className="w-3.5 h-3.5" />
                  <span>Clear Screen</span>
                </button>
              )}
            </div>"""

btn_replacement = """            <div className="flex items-center gap-2 flex-wrap">
              <span className="text-[11px] font-mono font-bold text-slate-400 uppercase mr-1 hidden sm:inline">
                Capstone Demos:
              </span>
              <button
                onClick={handleLoadDataset1}
                disabled={isLoading}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-emerald-50 hover:bg-emerald-100 text-emerald-900 border border-emerald-300 text-xs font-bold transition-all shadow-sm"
                title="Load Set 1: Apex Precision (Retrospective Cancellation - Proceed 100/100)"
              >
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-700" />
                <span>Load Set 1 (Proceed Worthy)</span>
              </button>
              <button
                onClick={handleLoadDataset2}
                disabled={isLoading}
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-900 border border-rose-300 text-xs font-bold transition-all shadow-sm"
                title="Load Set 2: Shaurya Infra (No E-Way Bill / 216-Day Delay - HOLD 50/100)"
              >
                <AlertTriangle className="w-3.5 h-3.5 text-rose-700" />
                <span>Load Set 2 (Not Worthy / HOLD)</span>
              </button>
              {activeCase && (
                <button
                  onClick={handleResetWorkspace}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-beige-100 hover:bg-beige-200 text-slate-700 text-xs font-semibold transition-all shadow-sm"
                  title="Clear on-screen data back to blank form"
                >
                  <X className="w-3.5 h-3.5" />
                  <span>Clear Screen</span>
                </button>
              )}
            </div>"""

code = code.replace(btn_target, btn_replacement)

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(code)

print("Inserted handleLoadDataset1, handleLoadDataset2 and UI quick load buttons in page.tsx!")