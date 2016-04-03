class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

   def sayBye(self)
<<<<<<< HEAD
        print "Bye, my name is " self.name

   def sayHello(self)
        print "Hello, my name is " self.name
=======
        print "Bye, my name is " self.name
>>>>>>> 4786e7b017f03c5977a312739ea2169d86938cb7
