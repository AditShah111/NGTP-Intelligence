with open("src/service/scoring-engine.ts", "r", encoding="utf-8") as f:
    content = f.read()

# Calibrate calculateReadinessScore
old_readiness = """  // 1. Statutory Position (Max 20):
  // Requires both invoices (16(2)(a)) AND bank payment (2nd proviso & 16(2)(c))
  let statutoryPosition = 2;
  if (hasInvoices && hasBank && hasTransit) statutoryPosition = 20;
  else if (hasInvoices && hasBank) statutoryPosition = 14;
  else if (hasInvoices) statutoryPosition = 6;
  else if (hasBank) statutoryPosition = 5;

  // 2. Evidence Quality (Max 20):
  // 7 pts for Invoices, 7 pts for Bank RTGS, 6 pts for E-Way Bills
  let evidence = 1;
  if (hasInvoices && hasBank && hasTransit) evidence = 20;
  else if (hasInvoices && hasBank) evidence = 13;
  else if (hasInvoices && hasTransit) evidence = 11;
  else if (hasInvoices) evidence = 5;
  else if (hasBank) evidence = 6;

  // 3. Precedent Support (Max 15):
  // Suncraft and D.Y. Beathel CANNOT be applied without genuine bank payment proof!
  let precedent = 2;
  if (hasInvoices && hasBank && hasTransit) precedent = 15;
  else if (hasInvoices && hasBank) precedent = 12;
  else if (hasInvoices) precedent = 3; // Invoices alone cannot invoke Suncraft

  // 4. Lower Authority Error Audit (Max 15):
  // Cannot audit officer errors without actual SCN / DRC-07 order!
  let lowerAuthorityError = 2;
  if (hasScn && hasInvoices && hasBank) lowerAuthorityError = 15;
  else if (hasScn) lowerAuthorityError = 8;
  else if (hasInvoices && hasBank) lowerAuthorityError = 7;
  else if (hasInvoices) lowerAuthorityError = 2;

  // 5. Drafting Quality (Max 10):
  let draftingQuality = 2;
  if (hasInvoices && hasBank && hasTransit) draftingQuality = 10;
  else if (hasInvoices && hasBank) draftingQuality = 6;
  else if (hasInvoices) draftingQuality = 2;

  // 6. Counterargument Resilience (Max 10):
  // Invoices alone immediately collapse against fake-transit and non-payment attacks
  let counterargumentResilience = 1;
  if (hasInvoices && hasBank && hasTransit) counterargumentResilience = 10;
  else if (hasInvoices && hasBank) counterargumentResilience = 5;
  else if (hasInvoices) counterargumentResilience = 2;

  // 7. Procedural Position (Max 10):
  let proceduralPosition = 2;
  if (hasScn && hasInvoices) proceduralPosition = 10;
  else if (hasInvoices) proceduralPosition = 3;"""

new_readiness = """  // 1. Statutory Position (Max 20):
  // Requires invoices (16(2)(a)), physical movement (16(2)(b)), and bank payment (2nd proviso)
  let statutoryPosition = 2;
  if (hasInvoices && hasBank && hasTransit) statutoryPosition = 20;
  else if (hasInvoices && hasBank) statutoryPosition = 10; // Penalized: Missing Section 16(2)(b) transit
  else if (hasInvoices && hasTransit) statutoryPosition = 8;
  else if (hasInvoices) statutoryPosition = 5;
  else if (hasBank) statutoryPosition = 4;

  // 2. Evidence Quality (Max 20):
  let evidence = 1;
  if (hasInvoices && hasBank && hasTransit) evidence = 20;
  else if (hasInvoices && hasBank) evidence = 8; // Heavy penalty for missing E-Way bills & weighment
  else if (hasInvoices && hasTransit) evidence = 9;
  else if (hasInvoices) evidence = 4;
  else if (hasBank) evidence = 4;

  // 3. Precedent Support (Max 15):
  // Suncraft and Halder Enterprises require bona fide physical receipt of goods!
  let precedent = 2;
  if (hasInvoices && hasBank && hasTransit) precedent = 15;
  else if (hasInvoices && hasBank) precedent = 7; // Suncraft weakened if physical receipt is disputed
  else if (hasInvoices) precedent = 3;

  // 4. Lower Authority Error Audit (Max 15):
  let lowerAuthorityError = 2;
  if (hasScn && hasInvoices && hasBank && hasTransit) lowerAuthorityError = 15;
  else if (hasScn && hasInvoices && hasBank) lowerAuthorityError = 10;
  else if (hasScn) lowerAuthorityError = 6;
  else if (hasInvoices && hasBank) lowerAuthorityError = 5;
  else if (hasInvoices) lowerAuthorityError = 2;

  // 5. Drafting Quality (Max 10):
  let draftingQuality = 2;
  if (hasInvoices && hasBank && hasTransit) draftingQuality = 10;
  else if (hasInvoices && hasBank) draftingQuality = 5;
  else if (hasInvoices) draftingQuality = 2;

  // 6. Counterargument Resilience (Max 10):
  // Without E-Way bills, case collapses under Section 74 circular trading attack
  let counterargumentResilience = 1;
  if (hasInvoices && hasBank && hasTransit) counterargumentResilience = 10;
  else if (hasInvoices && hasBank) counterargumentResilience = 3; // Fragile against fake-transit
  else if (hasInvoices) counterargumentResilience = 1;

  // 7. Procedural Position (Max 10):
  let proceduralPosition = 2;
  if (hasScn && hasInvoices && hasTransit) proceduralPosition = 10;
  else if (hasScn && hasInvoices) proceduralPosition = 7;
  else if (hasInvoices) proceduralPosition = 3;"""

content = content.replace(old_readiness, new_readiness)

# Calibrate calculateViabilityScore
old_viability = """  const merits = hasInvoices && hasBank && hasTransit ? 20 : (hasInvoices && hasBank ? 14 : 9);
  const evidenceQuality = hasInvoices && hasBank && hasTransit ? 20 : (hasInvoices && hasBank ? 13 : 8);
  const precedentSupport = hasBank ? 15 : 4;
  const proceduralSoundness = 10;
  const opposingCaseDifficulty = hasTransit ? 13 : 8;
  const curabilityOfGaps = 8;
  const appellateForumTrend = 9;"""

new_viability = """  const merits = hasInvoices && hasBank && hasTransit ? 20 : (hasInvoices && hasBank ? 9 : 5);
  const evidenceQuality = hasInvoices && hasBank && hasTransit ? 20 : (hasInvoices && hasBank ? 8 : 4);
  const precedentSupport = hasBank && hasTransit ? 15 : (hasBank ? 7 : 3);
  const proceduralSoundness = hasTransit ? 10 : 6;
  const opposingCaseDifficulty = hasTransit ? 13 : 4; // High vulnerability to circular trading attack
  const curabilityOfGaps = hasTransit ? 8 : 5;
  const appellateForumTrend = hasTransit ? 9 : 4;"""

content = content.replace(old_viability, new_viability)

with open("src/service/scoring-engine.ts", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated scoring-engine.ts with calibrated transit-gated scoring!")