/**let Emploee = function(name,age){
    this.name = name
    this.age =age

    this.getname = function() {
        return this.name
        
    }
    this.getage = function() {
        return this.age
        
    }

}


emp1 = new Emploee ("Nithya" ,23)
emp2 = new Emploee ("Lakshmi" ,42)
console.log(emp1.getname())
console.log(emp1.getage())
console.log(emp2.getname())
console.log(emp2.getage())**/


//proper protype example for interview

let Emploee = function(name,age){
    this.name = name
    this.age =age

}

Emploee.prototype.getname = function() {
    return this.name
    
}

Emploee.prototype.getage = function() {
    return this.age
    
}


emp1 = new Emploee ("Nithya" ,23)
emp2 = new Emploee ("Lakshmi" ,42)
console.log(emp1.getname())
console.log(emp1.getage())
console.log(emp2.getname())
console.log(emp2.getage())