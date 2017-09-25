def forloopenumerate():
           months  = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
           for i, m in enumerate(months):
                      print (i,m)

def forrepeat():
           for i in '123':
                      print i,"Guru99"

def passtest():
           list = [1,2,3,4,5]
           for i in list:
                      if i==4:
                                 pass
                                 print "Pass when value is",i
                      print i,
                      
def main():
           forloopenumerate()
           forrepeat()
           passtest()
           
if __name__ == "__main__":
           main()
