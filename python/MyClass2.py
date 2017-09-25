class MyClass2():
           b=50
           "This is class 2"
           def func1(self):
                      b=30
                      "This is function"
                      print "Hello world"
                      print MyClass2.b
                      print b
                      
class ComplexNumber():
           def __init__(self, r=0, i=0):
                      self.real=r
                      self.imag=i
           def getData(self):
                      print "{0} + {1}j" .format(self.real,self.imag)
def main():
           c=MyClass2()
           c.func1()
           print c.b
           c1=ComplexNumber(5,3)
           c1.getData()

if __name__=="__main__":
           main()

