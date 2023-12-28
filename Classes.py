x=input("Please input your name" )
y=int(input("Please input borrowed amount"))
z=int(input("Months your loan is due"))
class Loanbook():
      # definination of class
      def __init__ (self,name,loan):
         self.name=name
         self.loan=loan
         # class method
      def  myfunc(self):
          p=(self.loan+(self.loan*9/100))
          print ("Dear",self.name, "Your due Amount is ",p)





# child class of loan book
          
class Child(Loanbook):
    def __init__(self,name,loan,months):
       super().__init__(name,loan)
       self.monthsdue=months
       # class method
    def  myfunc(self):
          p=((self.loan*9/100*self.monthsdue/12)+self.loan)
          print ("Dear",self.name, "Your due Amount is ",p)
# child object and passing in variables
loanee_1=Child(x,y,z)
loanee_1.myfunc()