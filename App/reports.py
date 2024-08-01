import webbrowser
import os
from fpdf import FPDF


class PdfReport:
    """
    It creates PDF report that contains data about the flatmates
    such their names, their due amounts and period of the amount
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay=str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay=str(round(flatmate2.pays(bill, flatmate1), 2))

        # Create pdf document
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add Icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # INsert period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=0, h=40, txt=bill.period, border=0, ln=1)

        # INsert period label and value
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name+": ", border=0)
        pdf.cell(w=200, h=40, txt=flatmate1_pay,
                 border=0, ln=1)

        # INsert period label and value
        pdf.cell(w=100, h=40, txt=flatmate2.name+": ", border=0)
        pdf.cell(w=200, h=40, txt=flatmate2_pay,
                 border=0, ln=1)

        # Change the directory of the files, generates and open the pdf file
        os.chdir("files")
        pdf.output(self.file_name)

        webbrowser.open(self.file_name)