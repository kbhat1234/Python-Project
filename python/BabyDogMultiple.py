#multilevel inheritance

class Animal():
           # Animal class -> Base or parent class 1
           "Will print Eating..."
           def eat(self):
                      print "Eating..."
                      print "Animal.__doc__: ", Animal.__doc__
                      print "Animal.__dict__: ", Animal.__dict__
                      print "Animal.__bases__: ", Animal.__bases__
                      print "Animal.__module__: ", Animal.__module__
                      print "Animal.__name__: ", Animal.__name__

class Dog():
           #Dog class -> Base or Parent class 2
           def bark(self):
                      print "Barking..."
                      print "Dog.__doc__: ", Dog.__doc__
                      print "Dog.__dict__: ", Dog.__dict__
                      print "Dog.__bases__: ", Dog.__bases__
                      print "Dog.__module__: ", Dog.__module__
                      print "Dog.__name__: ", Dog.__name__

class BabyDogMultiple(Animal,Dog):
           #BabyDog class -> multiple Derived or child class
           def weep(self):
                      print "Weeping..."
                      print "BabyDogMultiple.__doc__: ", BabyDogMultiple.__doc__
                      print "BabyDogMultiple.__dict__: ", BabyDogMultiple.__dict__
                      print "BabyDogMultiple.__bases__: ", BabyDogMultiple.__bases__
                      print "BabyDogMultiple.__module__: ", BabyDogMultiple.__module__
                      print "BabyDogMultiple.__name__: ", BabyDogMultiple.__name__

def main():
           bd = BabyDogMultiple()
           bd.eat()
           bd.bark()
           bd.weep()

if __name__ == "__main__":
           main()
