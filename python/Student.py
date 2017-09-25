class Student():
          
           """def __init__(self, rollno, name):
                      self.rollno = rollno
                      self.name = name
            """          

           def getData(self, rollno, name):
                      self.name = name
                      self.rollno = rollno
                      
           def displayStudent(self):
                      print "Roll no: ", self.rollno, ",Name: ", self.name

def main():
           s1 = Student()
           s1.getData(121, "karthik")
           s1.displayStudent()
           print "Student.__doc__: ", Student.__doc__
           print "Student.__name__: ", Student.__name__
           print "Student.__module__: ", Student.__module__
           print "Student.__bases__: ", Student.__bases__
           print "Student.__dict__: ", Student.__dict__
           
           #emp1=Student(121,"karthik")
           #emp2=Student(122,"rini")
           #emp1.displayStudent()
           #emp2.displayStudent()

if __name__=="__main__":
           main()
           
