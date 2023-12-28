income = int(input("Enter your income"))
tax_payable_1 = 0
tax_payable_2= 0
tax_payable_3= 0
tax_payable_4 = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable_1 = x * 10 / 100
    tax_payable = tax_payable_1
elif income <= 30000:
     z=income -20000
     tax_payable_2 +=((z*20/100)+ tax_payable_1 )  
     tax_payable = tax_payable_2 
elif income  <= 40000:
    a=income-30000
    tax_payable_3 += ((a*30/100)+tax_payable_2)
    tax_payable = tax_payable_3
elif income  >= 50000:
     b=income -40000
     tax_payable_4 +=(( b*0.5)+tax_payable_3)
     tax_payable = tax_payable_4
else:
    print("Invalid input")

print("Your due tax is",tax_payable)
