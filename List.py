List1=[21,23,45,67]
List2=[34,89,100,37]

result_list=[]
for num in List1:
    if num % 2 !=0:
     result_list.append(num)    


for num in List2 :
   if num % 2==0:
      result_list.append(num)    


print("Your final list is ",result_list)