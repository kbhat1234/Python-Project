#inheritance example

class Animal():
           a="karthik"
           #Base or parent class
           def eat(self):
                      #a="Karthik"
                      print "Eating..."
                      print Animal().a
                      
class Dog(Animal):
           b="rini"
           #Derived or child class
           def bark(self):
                      #b="Rini"
                      print "Barking..."
                      print Dog().b

def main():
           d = Dog()
           d.eat()
           d.bark()
           
if __name__ == "__main__":
           main()
