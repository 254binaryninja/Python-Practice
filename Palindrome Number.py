s=int(input("Enter your number to check if its a palindrome number"))

original_num=s

reverse_num=0
while s>0:
    remeinder=s%10
    reverse_num=(reverse_num*10)+remeinder
    s= s //10


if original_num == reverse_num :
    print("This is a palindrome number")
else:
    print("This given number is not a palindrome")    