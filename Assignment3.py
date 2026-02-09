gross_salary = int(input("Enter your Gross salary here"))

if gross_salary > 0 and gross_salary <= 5999 :
    print("monthly contributions : ksh150.00")

elif gross_salary > 6000 and gross_salary <= 7999 :
    print("monthly contributions : ksh300.00")

elif gross_salary > 8000 and gross_salary <= 11999 :
    print("monthly contributions : ksh400.00")

elif gross_salary > 12000 and gross_salary <= 14999 :
    print("monthly contributions : ksh500.00")

elif gross_salary > 15000 and gross_salary <= 19999 :
    print("monthly contributions : ksh600.00")

elif gross_salary > 20000 and gross_salary <= 24999 :
    print("monthly contributions : ksh750.00")

elif gross_salary > 25000 and gross_salary <= 29999 :
    print("monthly contributions : ksh850.00")

elif gross_salary > 30000 and gross_salary <= 49999 :
    print("monthly contributions : ksh1000.00")

elif gross_salary > 50000 and gross_salary <= 99999 :
    print("monthly contributions : ksh1500.00")

elif gross_salary > 100000:
    print("monthly contributiobs : ksh2000.00")

else :
    print("invalid entry")