def sum(x,y):
           "going to add x and y"
           s=x+y
           print "sum of 2 numbers is:", s

#calling the sum function
sum(10,20)
sum(20,40)


def sum(x,y):
           "Adding 2 values"
           print "printing within the function"
           z=x+y
           print z
           return z

def msg():
           print "hello"
           return

total = sum(20,30)
print "printing outside function",total
msg()
print "Rest of the code"
           
def addition(x,y):
           z=x+y
           print z

x=15
addition(x,20)
addition(x,x)
y=30
addition(x,y)
#addition(x)

#function definition
def msg(id, name, age=21):
           print id, name, age;
           return

msg(id=100,name='karthik',age=20)
msg(102,'Ishani',23)
msg('Ishani',102,27)

msg(name="Raghu", age=33, id=222)
msg(id=101,name='rini')
