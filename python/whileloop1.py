def whileloop():
           x=2
           while(x<4):
                      print "value of x is",x
                      x+=1

def whileloop1():
           a=10
           while(a>0):
                      print "value of a is",a
                      a-=2
                      
def forloop():
           x=0
           for x in range (2,7):
                      print x

def forloopstring():
           Months = ["Jan","Feb","Mar","April","May","June"]
           for m in Months:
                      print m
         
def main():
           whileloop()
           whileloop1()
           forloop()
           forloopstring()

if __name__== "__main__":
           main()
