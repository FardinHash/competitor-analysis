from fpdf import FPDF
import os

class ReportGenerator:
    def generate(self, swot_results, query):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        font_path = os.path.join(os.path.dirname(__file__), "fonts", "FreeSans.ttf")
        bold_font_path = os.path.join(os.path.dirname(__file__), "fonts", "FreeSansBold.ttf")

        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")
        if not os.path.exists(bold_font_path):
            raise FileNotFoundError(f"Bold font file not found: {bold_font_path}")

        pdf.add_font("FreeSans", style="", fname=font_path, uni=True)
        pdf.add_font("FreeSans", style="B", fname=bold_font_path, uni=True)

        pdf.set_font("FreeSans", style="B", size=16)
        pdf.cell(0, 10, f"Competitor Analysis Report: {query}", ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("FreeSans", style="B", size=12)
        pdf.cell(0, 10, "SWOT Analysis:", ln=True)
        pdf.ln(5)

        pdf.set_font("FreeSans", size=10)
        pdf.multi_cell(0, 10, swot_results)

        report_dir = "outputs/reports/"
        os.makedirs(report_dir, exist_ok=True)
        report_path = os.path.join(report_dir, f"{query}_analysis_report.pdf")
        pdf.output(report_path)

        return report_path
