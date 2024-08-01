from flat import Bill, Flatmate
from reports import PdfReport

bill_amount=float(input("Hello User! Please enter the bill amount: "))
bill_period=input("Please enter the period as well (e.g. May 2024): ")
mate1=input("Please enter the name of flatemate1: ")
mate1_days=int(input(f"{mate1}! PLease enter the number of days in house: "))
mate2=input("Please enter the name of flatemate2: ")
mate2_days=int(input(f"{mate2}! Please enter the number of days in house: "))


bill1= Bill(bill_amount, bill_period)
flat_mate1= Flatmate(mate1, days_in_house=mate1_days)
flat_mate2= Flatmate(mate2, days_in_house=mate2_days)

print(f"{flat_mate1.name} should pay: {flat_mate1.pays(bill1, flatmate2=flat_mate2):.2f}")
print(f"{flat_mate2.name} should pay: {flat_mate2.pays(bill1, flatmate2=flat_mate1):.2f}")

pdf_report= PdfReport(file_name=f"{bill1.period}.pdf")
pdf_report.generate(flatmate1=flat_mate1, flatmate2=flat_mate2, bill=bill1)




