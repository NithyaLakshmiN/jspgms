class Employee{

    constructor (name,empid, empphone){
        this.name = name
        this.empid = empid
        this.empphone = empphone
    }

    getempname (){
        return this.name
    }

    getempid(){
        return this.empid
    }

    getempphone (){
        return this.empphone
    }
}

let emp1 = new Employee("Nithya",1,90866)
let emp2 = new Employee("Lakshmi",2,90888)
console.log(emp1.name)
console.log(emp1.empid)
console.log(emp1.empphone)
console.log(emp2.name)
console.log(emp2.empid)
console.log(emp2.empphone)
