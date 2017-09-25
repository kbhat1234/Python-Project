import os

def createfile():
           #fp=open("abc.txt","w")
           #fp=open("abc.txt","w+")
           #fp=open("xyz.txt","wb")
           fp=open("abc.txt","w+")
           for i in range(10):
                      fp.write("This is line %d\r\n" %(i+1))
           fp.close()
                      
def appendfile():
           #fp=open("abc.txt","a")
           #fp=open("abc.txt","a+")
           #fp=open("abc.txt","ab")
           fp=open("abc.txt","a+")        
           for i in range(10):
                      fp.write("Appended line is %d\r\n" %(i+1))
           fp.close()
    
def readfile():
           #fp=open("abc.txt","r")
           #fp=open("abc.txt","r+")
           #fp=open("abc.txt","ab+")
           fp=open("abc.txt","r")
           #if(fp.mode == 'r'):
                      #contents = fp.read()
           contents = fp.readlines()
           for x in contents:
                      print x
           fp.close()
           
def main():
           createfile()
           appendfile()
           readfile()
           #os.remove('abc.txt')
           #os.rename('abc.txt','xyz.txt')
           #os.tell()
           
if __name__ == "__main__":
           main()
