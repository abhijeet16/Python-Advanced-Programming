import webbrowser
from fpdf import FPDF
import os


class PdfReport:
    """
    Creates a class PdfReport with attribute filename and generates a report
    with bill details and each flatmate share.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period: ', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert share for flatmate 1
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=20, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=20, txt=str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2)), border=0, ln=1)

        # Insert share for flatmate 2
        pdf.cell(w=100, h=20, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=20, txt=str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2)), border=0, ln=1)

        os.chdir("Reports")
        pdf.output(self.filename)

        webbrowser.open(self.filename)
