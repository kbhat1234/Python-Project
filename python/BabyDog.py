#multilevel inheritance

class Animal():
           # Animal class -> Base or parent class
           "Will print Eating..."
           def eat(self):
                      print "Eating..."
                      print "Animal.__doc__: ", Animal.__doc__
                      print "Animal.__dict__: ", Animal.__dict__
                      print "Animal.__bases__: ", Animal.__bases__
                      print "Animal.__module__: ", Animal.__module__
                      print "Animal.__name__: ", Animal.__name__

class Dog(Animal):
           #Dog class -> Derived or child class 1
           def bark(self):
                      print "Barking..."
                      print "Dog.__doc__: ", Dog.__doc__
                      print "Dog.__dict__: ", Dog.__dict__
                      print "Dog.__bases__: ", Dog.__bases__
                      print "Dog.__module__: ", Dog.__module__
                      print "Dog.__name__: ", Dog.__name__

class BabyDog(Dog):
           #BabyDog class -> Derived or child class 2
           def weep(self):
                      print "Weeping..."
                      print "BabyDog.__doc__: ", BabyDog.__doc__
                      print "BabyDog.__dict__: ", BabyDog.__dict__
                      print "BabyDog.__bases__: ", BabyDog.__bases__
                      print "BabyDog.__module__: ", BabyDog.__module__
                      print "BabyDog.__name__: ", BabyDog.__name__

def main():
           bd = BabyDog()
           bd.eat()
           bd.bark()
           bd.weep()

if __name__ == "__main__":
           main()
