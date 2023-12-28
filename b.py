a=input("enter the symbol you need for your pattern:")
s=int(input("Input the number reqiured for your pattern"))# this takes the no of lines for your pattern


for num in range(s):
    for i in range(num):
        print (a, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")