with open("scripts/generate_capstone_problem_statement.py", "r", encoding="utf-8") as f:
    content = f.read()

old_canvas_block = """class NumberedCanvas(canvas.Canvas):
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
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, A4[1] - 36, "ICAI / AICA Level 2 Capstone Project | NGTP Litigation Intelligence Engine")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(54, A4[1] - 42, A4[0] - 54, A4[1] - 42)
            
        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(A4[0] - 54, 30, footer_text)
        self.drawString(54, 30, "AICA LEVEL 2 CAPSTONE | Problem Statement & System Architecture Document")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 42, A4[0] - 54, 42)
        self.restoreState()"""

new_canvas_block = """def draw_first_page(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(54, 30, "AICA LEVEL 2 CAPSTONE | Problem Statement & System Architecture Document")
    canvas.drawRightString(A4[0] - 54, 30, f"Page {doc.page}")
    canvas.setStrokeColor(colors.HexColor("#E2E8F0"))
    canvas.setLineWidth(0.5)
    canvas.line(54, 42, A4[0] - 54, 42)
    canvas.restoreState()

def draw_later_pages(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawString(54, A4[1] - 36, "ICAI / AICA Level 2 Capstone Project | NGTP Litigation Intelligence Engine")
    canvas.setStrokeColor(colors.HexColor("#E2E8F0"))
    canvas.setLineWidth(0.5)
    canvas.line(54, A4[1] - 42, A4[0] - 54, A4[1] - 42)

    canvas.drawString(54, 30, "AICA LEVEL 2 CAPSTONE | Problem Statement & System Architecture Document")
    canvas.drawRightString(A4[0] - 54, 30, f"Page {doc.page}")
    canvas.setStrokeColor(colors.HexColor("#E2E8F0"))
    canvas.setLineWidth(0.5)
    canvas.line(54, 42, A4[0] - 54, 42)
    canvas.restoreState()"""

content = content.replace(old_canvas_block, new_canvas_block)
content = content.replace("canvasmaker=NumberedCanvas", "onFirstPage=draw_first_page, onLaterPages=draw_later_pages")

with open("scripts/generate_capstone_problem_statement.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated generate_capstone_problem_statement.py with standard callbacks!")