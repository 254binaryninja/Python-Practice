print (" Showing sum for the first ten previous and currrent numbers")
# set the starting and final number
previous_num = int (input("Enter your starting number"))
final_num=int(input("Enter your final number"))
# check if the starting number is greater than the final no
if previous_num < final_num :
 for i in range (previous_num,final_num):  # sum of the previous and next number
     x_sum=previous_num +i
     print ("Previous number",previous_num,"Current number",i,"Sum",x_sum)
     previous_num= i
else:
     print("Invalid number arguments")