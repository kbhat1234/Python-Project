#scope of variable

a=20
c=100

def msg():
           b=20
           #global a
           a=30
           print "value of a is",a
           print "value of b is",b
           print "value of c is",c
           return

msg()
print a
#print b
print c
