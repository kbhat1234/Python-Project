def inputExpression():
           n = input("Enter your expression: ")
           print "Evaluated expression is ",n

def inputRaw():
           n = raw_input("Enter your name:")
           r = int(raw_input("Enter roll no:"))
           s = float(raw_input("Enter salary:"))
           
           print "Welcome ",n
           print "Roll no: ",r
           print "Salary: ",s

def simpleInterest():
           pr = (int(raw_input("Enter the principl")))
           r = (int(raw_input("Enter rate")))
           t = (int(raw_input("Enter time")))
           si = (pr*r*t)/100
           print "Simple Interest is ", si

def userDetails():
           name = raw_input("Enter name:")
           roll_no = raw_input("Enter roll no:")
           math = float(raw_input("Enter math marks:"))
           physics = float(raw_input("Enter physics marks:"))
           chemistry = float(raw_input("Enter chemistry marks:"))
           avg = (math+physics+chemistry)/3

           print "welcome ",name
           print "roll  no: ", roll_no
           print "maths marks: ", math
           print "physics marks: ", physics
           print "chemistry marks: ", chemistry
           print "average marks: " ,round(avg,2)

def main():
           #inputExpression()
           #inputRaw()
           #simpleInterest()
           userDetails()
if __name__ == "__main__":
           main()

