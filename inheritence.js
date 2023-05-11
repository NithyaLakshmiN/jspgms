class Car{

    setName(name){
        this.name = name
        console.log("ThMy car name is" +this.name)
    }

    startengine(){
        console.log("The Engine started for" +this.name)
    }

    stopengine(){
        console.log("The Engine stopped for" +this.name)
    }

}

class Toyota extends Car {
      topspeed(speed){
        this.speed= speed
        console.log("Top speed of my car is" + speed)

}
}

let car1 = new  Toyota()
car1.setName("Toyota")
car1.topspeed(100)
car1.startengine()
car1.stopengine()
