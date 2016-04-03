from firstClass import Employee

def doStuff(stuff):
    print stuff, stuff
    
if __name__ == '__main__':
    prvni = Employee("Pavel",10000)
    print "Num of employees: ", Employee.empCount
    prvni.displayEmployee()
    prvni.displayEmployee()
    doStuff("tada")