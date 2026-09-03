with open("src/app/page.tsx", "r", encoding="utf-8") as f:
    content = f.read()

# Add isParsingDoc state
if "const [isParsingDoc, setIsParsingDoc] = useState(false);" not in content:
    content = content.replace(
        "const [isExtracting, setIsExtracting] = useState(false);",
        "const [isExtracting, setIsExtracting] = useState(false);\n  const [isParsingDoc, setIsParsingDoc] = useState(false);"
    )

# Replace handleSubmissionFileImport
old_handler = """  // Import text file into Written Submission textarea
  const handleSubmissionFileImport = async (files: FileList | null) => {
    if (!files || files.length === 0) return;
    const file = files[0];
    try {
      const text = await file.text();
      setWrittenSubmission(text);
    } catch (e) {
      console.warn('Could not read text directly:', e);
    }
  };"""

new_handler = """  // Import text file into Written Submission textarea (clean parsing for .docx, .doc, .pdf, .txt)
  const handleSubmissionFileImport = async (files: FileList | null) => {
    if (!files || files.length === 0) return;
    const file = files[0];
    const filename = file.name.toLowerCase();

    // Plain text formats (.txt, .md, .csv) can be read directly
    if (filename.endsWith('.txt') || filename.endsWith('.md') || filename.endsWith('.csv')) {
      try {
        const text = await file.text();
        setWrittenSubmission(text);
      } catch (e) {
        console.warn('Could not read text directly:', e);
      }
      return;
    }

    // For .docx, .doc, .pdf, send to server extractor to cleanly parse text without binary zip tags
    setIsParsingDoc(true);
    try {
      const formData = new FormData();
      formData.append('file', file);

      const res = await fetch('/api/extract-text', {
        method: 'POST',
        body: formData
      });

      if (res.ok) {
        const data = await res.json();
        if (data.text) {
          setWrittenSubmission(data.text);
        }
      } else {
        const errData = await res.json().catch(() => ({}));
        alert(`Could not extract text: ${errData.error || 'Server parsing error'}`);
      }
    } catch (e: any) {
      console.error('Document extraction error:', e);
      alert('Error parsing document. Please ensure it is a valid .docx, .pdf, or .txt file.');
    } finally {
      setIsParsingDoc(false);
      if (submissionFileInputRef.current) submissionFileInputRef.current.value = '';
    }
  };"""

content = content.replace(old_handler, new_handler)

# Update Load Text from File button
old_button = """                    <button
                      type="button"
                      onClick={() => submissionFileInputRef.current?.click()}
                      className="text-[11px] font-mono font-semibold px-2.5 py-1 rounded bg-white border border-beige-300 text-slate-700 hover:bg-beige-50 transition-all shadow-sm flex items-center gap-1"
                    >
                      <Upload className="w-3 h-3 text-amber-700" />
                      <span>Load Text from File</span>
                    </button>"""

new_button = """                    <button
                      type="button"
                      disabled={isParsingDoc}
                      onClick={() => submissionFileInputRef.current?.click()}
                      className="text-[11px] font-mono font-semibold px-2.5 py-1 rounded bg-white border border-beige-300 text-slate-700 hover:bg-beige-50 transition-all shadow-sm flex items-center gap-1 disabled:opacity-60"
                    >
                      {isParsingDoc ? (
                        <>
                          <Loader2 className="w-3 h-3 animate-spin text-amber-700" />
                          <span>Extracting Text...</span>
                        </>
                      ) : (
                        <>
                          <Upload className="w-3 h-3 text-amber-700" />
                          <span>Load Text from File (.docx, .pdf, .txt)</span>
                        </>
                      )}
                    </button>"""

content = content.replace(old_button, new_button)

with open("src/app/page.tsx", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated page.tsx with clean document text extraction handler!")