def ExceptionHandleWithException():
           try:
                      a=10/0
                      print a

           except ArithmeticError:
                      print "airthmetic exception division by zero error"
           else:
                      print "Welcome"

def  ExceptionHandleWithoutException():
           try:
                      a=10/0
                      print a
           except:
                      print "Airthmetic exception"
           else:
                      print "Successfully Done"

def ExceptionHandleMultiple():
           try:
                      a=10/0
                      print a
           except ArithmeticError, StandardError:
                      print "Error seen"
           else:
                      print "Successfully Done"

def ExceptionHandleFinally():
           try:
                      a=10/0
                      print a
           except ArithmeticError:
                      print "Arithmetic Error"
           else:
                      print "No Error seen"
           finally:
                      print "Execution is complete with or without exceptions"

def RaiseException():
           try:
                      print "Start of try block"
                      a=10
                      print a
                      raise NameError("Hello")
           except NameError as e:
                      print "An Exception Occured"
                      print e
           finally:
                      print "End of try block"

           try:
                      print "Start of try block"
                      b=10/0
                      print b
                      raise ArithmeticError("Arithmetic Exception")
           except ArithmeticError as f:
                      print "An Airthmetic Error"
                      print  f
           finally:
                      print "End of try block"

class ErrorInCode(Exception):
           def __init__(self,data):
                      self.data=data
           def __str__(self):
                      return repr(self.data)

def CustomException():
           try:
                      raise ErrorInCode(2000)
           except ErrorInCode as ae:
                      print "Received eror:", ae.data
           finally:
                      print "End of function"
