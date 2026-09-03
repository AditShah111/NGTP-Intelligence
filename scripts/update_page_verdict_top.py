with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Let ExecutiveSummaryView be rendered above the ingestion form when activeCase exists
# 1. Remove ExecutiveSummaryView from bottom
content = content.replace("""        {/* 2. EXECUTIVE VERDICT & SUMMARY (Appears when activeCase is evaluated) */}
        {activeCase && (
          <ExecutiveSummaryView
            caseStudy={activeCase}
            onOpenExportModal={() => setIsExportOpen(true)}
          />
        )}""", "")

# 2. Insert ExecutiveSummaryView directly above the ingestion form
top_verdict_block = """        {/* 1. EXECUTIVE VERDICT & LITIGATION READINESS OUTPUT (Rendered at top when evaluated) */}
        {activeCase && (
          <div className="space-y-4 animate-fade-in">
            <ExecutiveSummaryView
              caseStudy={activeCase}
              onOpenExportModal={() => setIsExportOpen(true)}
            />
          </div>
        )}"""

content = content.replace(
    "{/* 1. CLEAN WORKSPACE: Ingestion & Assessment Form */}",
    top_verdict_block + "\n\n        {/* 2. MATTER PARTICULARS & EVIDENCE INGESTION WORKSPACE */}"
)

# Update form title when activeCase exists
content = content.replace(
    "{activeCase ? activeCase.title : 'Matter Assessment Workspace'}",
    "{activeCase ? 'Modify Matter Particulars & Evidence' : 'Matter Assessment Workspace'}"
)

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated page.tsx so output & export options appear directly at the top on the UI!")