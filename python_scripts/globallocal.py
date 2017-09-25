f=101
print f

def function1() :
           global f
           
           print f
           del f

           f="Hello world welcome to python learning"

function1() 
print f
