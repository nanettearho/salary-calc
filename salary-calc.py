#This is a calculator for your monthly salary after taxes and other legal expences in Finland.
#This project is unfinished and bound to change so take the results with a grain of salt

hours = float(input("What are your work hours for the month? "))
wage = float(input("What is your hourly wage? "))

before_tax = hours*wage
print("\nYour salary before taxes is ", before_tax, "€\n")

tax = float(input("What is your tax percentage? "))
union = float(input("Do you belong to a trade union? \nIf yes, what percentage of your salary does it cost? If not, put 0. "))

pension = float(input("What percentage of your salary does the employee pension cost? "))
insurance = float(input("What percentage of your salary does the unemployment insurance cost? "))

def calc():
    pass
