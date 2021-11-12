#This is a calculator for your monthly salary after taxes and other legal expences in Finland.
#This project is unfinished and bound to change so take the results with a grain of salt


def calc(num1, num2, num3, num4, num5):
    
    a_tax = num1/100*num2


    a_union = num1/100*num3


    a_pension = num1/100*num4

    a_ins = num1/100*num5

    salary = num1-a_tax-a_union-a_pension-a_ins
    print(salary)



while True:

    hours = float(input("What are your work hours for the month? "))
    wage = float(input("What is your hourly wage? "))

    bef_tax = hours*wage
    print("\nYour salary before taxes is ", bef_tax, "€\n")

    tax = float(input("What is your tax percentage? "))
    union = float(input("Do you belong to a trade union? \nIf yes, what percentage of your salary does it cost? If not, put 0. "))

    pension = float(input("What percentage of your salary does the employee pension cost? "))
    insurance = float(input("What percentage of your salary does the unemployment insurance cost? "))

    calc(bef_tax, tax, union, pension, insurance)
