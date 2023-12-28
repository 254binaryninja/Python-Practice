print("This is a  python calculator")
operator = input("The operator you like to use")
print ("Enter your first number")
b=input()
b=float(b)
print("Enter your second number")
c=input()
c=float(c)
match operator:
    case "+":
        print (b+c)
    case "-":
        print(b-c)    
    case  "*":
        print(b*c)   
    case "%":
        print(b%c)
    case _:
        print("you have input an operator that is invalid")     