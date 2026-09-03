with open("tsconfig.json", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    '"exclude": [\n    "node_modules"\n  ]',
    '"exclude": [\n    "node_modules",\n    "scripts"\n  ]'
)

with open("tsconfig.json", "w", encoding="utf-8") as f:
    f.write(content)

with open("scripts/test_both_datasets.ts", "r", encoding="utf-8") as f:
    ts_content = f.read()

ts_content = ts_content.replace("'Clear'", "'Clearly readable text'")

with open("scripts/test_both_datasets.ts", "w", encoding="utf-8") as f:
    f.write(ts_content)

print("Updated tsconfig.json and test_both_datasets.ts!")