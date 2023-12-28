X =[]
n=int(input("enter the number of elements required by your list:"))
for n in range (0,n) :
    bro=int(input())
    X.append(bro)

print("divisible by five")

for i in X :
    if i % 5== 0:
      print(i)
    