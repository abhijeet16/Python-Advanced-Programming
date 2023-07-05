from flat import Bill, Flatmate
from report import PdfReport

# Take user inputs
amount = float(input('What is the bill amount? '))
period = input("What is the period of the bill (eg June 2021)? ")
name1 = input("What is your name? ")
days_stayed1 = int(input("How many days did you stay in the house during this period? "))
name2 = input("What is your flatmate's name? ")
days_stayed2 = int(input("How many days did your flatmate stay in the house during this period? "))

# Create Instances
the_bill = Bill(amount=amount, period=period)
flatmate1 = Flatmate(name=name1, days_stayed=days_stayed1)
flatmate2 = Flatmate(name=name2, days_stayed=days_stayed2)

# Print the share
print(f"{flatmate1.name} pays: ", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name}  pays: ", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

# Generate report
pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
