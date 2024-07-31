from fpdf import FPDF
import webbrowser

class Bill:
    """
    Object that contains the data about a bill.
    Such as total amount and the period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate():
    """
    Create a flatmate person who lives in the flat and pays share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight=self.days_in_house/(self.days_in_house+flatmate2.days_in_house)
        return weight*bill.amount


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
        pdf.image("house.png", w=30, h=30)

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

        pdf.output(self.file_name)

        webbrowser.open(self.file_name)



bill_amount=float(input("Hello User! Please enter the bill amount: "))
bill_period=str(input("Please enter the period as well (e.g. May 2024): "))
mate1=str(input("Please enter the name of flatemate1: "))
mate1_days=int(input("PLease enter the number of days in house: "))
mate2=str(input("Please enter the name of flatemate2: "))
mate2_days=int(input("PLease enter the number of days in house: "))


bill1=Bill(bill_amount, bill_period)
flat_mate1=Flatmate(mate1, days_in_house=mate1_days)
flat_mate2=Flatmate(mate2, days_in_house=mate2_days)
print(f"{mate1} should pay: {flat_mate1.pays(bill1, flatmate2=flat_mate2):.2f}")
print(f"{mate2} should pay: {flat_mate2.pays(bill1, flatmate2=flat_mate1):.2f}")



pdf_report=PdfReport(file_name="Report1.pdf")
pdf_report.generate(flatmate1=flat_mate1, flatmate2=flat_mate2, bill=bill1)




