#superclass
class Employee:
    def __init__(self, Empname , Empid , EmpDOJ):
        self.Empname =Empname
        self.Empid =Empid
        self.EmpDOJ =EmpDOJ

    def empdetails (self)   :
        print("The Emp Name is" +self.Empname) 
        print("The Emp ID is" +self.Empid) 
        print("The Emp DOJ is" +self.EmpDOJ) 

#childclass1
class EmployeeDept(Employee) :
    def __init__(self ,Empname , Empid , EmpDOJ ,Empdeptname):
        self.Empdeptname =Empdeptname
        super().__init__(Empname,Empid,EmpDOJ)
       

    def empdeptdetails (self)   :
         print("The Emp Name is" +self.Empname) 
         print("The Emp ID is" +self.Empid) 
         print("The Emp DOJ is" +self.EmpDOJ) 
         print("The Emp Dept Name is" +self.Empdeptname) 

 #childclass2
class EmployeePerformance(EmployeeDept) :
    def __init__(self ,Empname , Empid , EmpDOJ ,Empdeptname,Empperformance):
        self.Empperformance =Empperformance
        super().__init__(Empname,Empid,EmpDOJ,Empdeptname)
       

    def employeeperfromance(self)   :
         print("The Emp Name is" +self.Empname) 
         print("The Emp ID is" +self.Empid) 
         print("The Emp DOJ is" +self.EmpDOJ) 
         print("The Emp Dept Name is" +self.Empdeptname)   
         print("The Employee performance for this quarter is" +self.Empperformance)        
         
        


Emp1 = EmployeePerformance("Nithya" ,"8","8th July","Mechanical","A Band")
Emp1.employeeperfromance()
