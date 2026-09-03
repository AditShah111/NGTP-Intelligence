with open("src/service/evaluator-agent.ts", "r", encoding="utf-8") as f:
    content = f.read()

old_gating = """  // Strict Document Type Gating
  const hasInvoices = documents.some(d => d.type === 'Invoice');
  const hasTransit = documents.some(d => d.type === 'E-Way Bill' || d.type === 'Transporter Bilty');
  const hasBank = documents.some(d => d.type === 'Bank Statement');
  const hasScn = documents.some(d => d.type === 'SCN' || d.type === 'DRC-01' || d.type === 'DRC-07');
  const hasCaCert = documents.some(d => d.type === 'CA Certificate');"""

new_gating = """  // Strict Document Type Gating (Flexible matching by type and file name)
  const hasInvoices = documents.some(d => d.type === 'Invoice' || /invoice/i.test(d.type || '') || /invoice/i.test(d.name || ''));
  const hasTransit = documents.some(d => d.type === 'E-Way Bill' || d.type === 'Transporter Bilty' || /eway|e-way|transit|weighbridge|fastag|transport/i.test(d.type || '') || /eway|e-way|weighbridge|fastag|transit/i.test(d.name || ''));
  const hasBank = documents.some(d => d.type === 'Bank Statement' || /bank|rtgs|neft|ledger/i.test(d.type || '') || /bank|rtgs|ledger/i.test(d.name || ''));
  const hasScn = documents.some(d => d.type === 'SCN' || d.type === 'DRC-01' || d.type === 'DRC-07' || /drc|scn|order/i.test(d.type || '') || /drc|scn|order/i.test(d.name || ''));
  const hasCaCert = documents.some(d => d.type === 'CA Certificate' || /certificate|ca/i.test(d.type || '') || /cert/i.test(d.name || ''));"""

if old_gating in content:
    content = content.replace(old_gating, new_gating)
    with open("src/service/evaluator-agent.ts", "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated evaluator-agent.ts with flexible document type gating!")
else:
    print("Already updated or pattern not found.")