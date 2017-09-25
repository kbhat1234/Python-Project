class Animal():
           def eat(self):
                      print "Eating..."

class Dog(Animal):
           def bark(self):
                      print "Barking..."

class Cat(Dog):
          def meow(self):
                      print "Meow Meow"
c=Cat()  
c.eat()  
c.bark()  
c.meow()
