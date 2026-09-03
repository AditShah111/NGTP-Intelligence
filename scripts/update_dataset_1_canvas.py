with open(r"C:\Users\ajay_\.gemini\antigravity\brain\b21d6f25-c48e-4a17-9d27-1f8b3d49fcc8\create_dataset_1.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace SinglePageNumberedCanvas with standard onFirstPage / onLaterPages callback
old_canvas_block = """class SinglePageNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawRightString(A4[0] - 40, 20, f"Page {self._pageNumber} of {page_count} | Evidentiary Exhibit")
        self.drawString(40, 20, "VERIFIED LEGAL EVIDENCE | AICA CAPSTONE DATASET 1 (PROCEED WORTHY - RETROSPECTIVE CANCELLATION)")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(40, 30, A4[0] - 40, 30)
        self.restoreState()

def create_pdf(path, story):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=40)
    doc.build(story, canvasmaker=SinglePageNumberedCanvas)
    print(f"Generated: {path}")"""

new_canvas_block = """def draw_footer_set1(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(40, 20, "VERIFIED LEGAL EVIDENCE | AICA CAPSTONE DATASET 1 (PROCEED WORTHY - RETROSPECTIVE CANCELLATION)")
    canvas.drawRightString(A4[0] - 40, 20, f"Page {doc.page} | Evidentiary Exhibit")
    canvas.setStrokeColor(colors.HexColor("#CBD5E1"))
    canvas.setLineWidth(0.5)
    canvas.line(40, 30, A4[0] - 40, 30)
    canvas.restoreState()

def create_pdf(path, story):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=40, rightMargin=40, topMargin=40, bottomMargin=45)
    doc.build(story, onFirstPage=draw_footer_set1, onLaterPages=draw_footer_set1)
    print(f"Generated: {path}")"""

content = content.replace(old_canvas_block, new_canvas_block)

with open(r"C:\Users\ajay_\.gemini\antigravity\brain\b21d6f25-c48e-4a17-9d27-1f8b3d49fcc8\create_dataset_1.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated create_dataset_1.py with standard onFirstPage callback!")