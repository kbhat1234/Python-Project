# Example file for working with classes
class myClass():
           def method1(self):
                      print "Guru99"
        
           def method2(self,someString):
                      print "Software Testing:" + someString
      
class childClass(myClass):
           def method1(self):
                      myClass.method1(self);
                      print "Child Class Method1"

           def method2(self):
                      myClass.method2(self, "Karthik");
                      print "childClass method2"     
         
def main():           
  # exercise the class methods
  c2 = childClass()
  c2.method1()
  c2.method2()

if __name__== "__main__":
  main()
