with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Add auto-scroll effect when activeCase changes
scroll_effect = """  // Auto-scroll to top when activeCase verdict is evaluated
  useEffect(() => {
    if (activeCase) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }, [activeCase]);"""

if "window.scrollTo({ top: 0, behavior: 'smooth' });" not in content:
    content = content.replace(
        "const [isExportOpen, setIsExportOpen] = useState(false);",
        "const [isExportOpen, setIsExportOpen] = useState(false);\n" + scroll_effect
    )

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)

print("Added auto-scroll effect to page.tsx!")