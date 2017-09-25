def main():
           f=open("guru99.txt","w+")

           for i in range(10):
                      f.write("This is karthik %d\r\n" % (i+1))
           #f.close()
           print f.name
           print f.mode
           print f.closed

if __name__ == "__main__":
           main()
