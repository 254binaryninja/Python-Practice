class Employee():
    def __init__(self,first,last,):
          self.first=first
          self.last=last
          self.email=first+'.'+last+'@gmail.com'
    
        

emp_1=Employee('Arnold','Musandu')

print(emp_1.email)