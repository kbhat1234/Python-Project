def forloopbreak():
           list = [1, 2, 3, 4, 5]
           for i in list:
                      if(i==3):
                                 print "element found"
                                 break
                      print i

def forloopbreak1():
           for x in range(10,20):
                      if(x==16):
                                 break
                      print x

def main():
           forloopbreak()
           forloopbreak1()

if __name__ == "__main__":
           main()
