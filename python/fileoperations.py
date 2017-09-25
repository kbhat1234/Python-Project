def fileOperations():
           #open() method to open file
           fp = open("file.txt","w")
           fp.write("Welcome to the world of python ")
           print "String is written to file.txt"
           fp.close()

           print "Name of the file is ",fp.name
           print "Mode opened file is ",fp.mode
           print "File is closed ",fp.closed
           
           fp1 = open("file.txt","r")
           r = fp1.read()
           print "Reading the file.txt",r
           fp1.close()

           print "Name of the file is ",fp1.name
           print "Mode opened file is ",fp1.mode
           print "File is closed ",fp1.closed

           fp2 = open("file.txt", "r")
           r1 = fp2.read(50)
           print "Reading file.txt when value is 5 bytes",r1
           fp2.close()

           print "Name of the file is ",fp2.name
           print "Mode opened file is ",fp2.mode
           print "File is closed ",fp2.closed

           fp3 = open("file.txt", "a+")
           fp3.write(" Append the file")
           print "File append done check file.txt"
           fp3.close()

           print "Name of the file is ",fp3.name
           print "Mode opened file is ",fp3.mode
           print "File is closed ",fp3.closed

def main():
           fileOperations()

if __name__ == "__main__":
           main()
