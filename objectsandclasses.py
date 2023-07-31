class car :
    def __init__ (self,carname,carcompany,carcost):
        self.carname = carname
        self.carcompany = carcompany
        self.carcost = carcost

    def cardetails(self):
        print("The car name is " +self.carname) 
        print("The car company is " +self.carcompany)     
        print("The car cost is " +self.carcost)  

car1 = car("Tata Indica" , "TATA" ,"4L")    
car2 = car("Hyundai" , "Accent" ,"6L")     

car1.cardetails()
car2.cardetails()