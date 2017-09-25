a=20
c=100

def msg():
           a=10
           b=20
           c=101
           print "Accessing values within the function"
           print "value of a is",a
           print "value of b is",b
           print "value of c is",c
           return

msg()
print "Accessing values outside the function"
print a
print c
#print b NameError: name 'b' is not defined
