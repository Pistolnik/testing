from firstClass import Employee

def doStuffing():
    print "Say HW"

if __name__ == '__main__':
    prvni = Employee("Pavel",10000)
    print "Num of employees: ", Employee.empCount
    prvni.displayEmployee()