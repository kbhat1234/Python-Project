def forloop1():
           #x=0
           for x in range(2,7):
                      print x

def forloop2():
           months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
           print len(months)
           print max(months)
           print min(months)
           string = "Karthik"
           print len(string)
           dict= {1:"Karthik", 2:"Rini", 3:"Ishani"}
           dict1 = {"K":123, "A":234}
           print dict1.values()
           print dict1.keys()
           tup1 = (1, 2, 10, 9, 4)

           """for m in months:
                      print m

           for s in string:
                      print s
           
           for v in dict.values():
                      print v

           for k in dict.keys():
                      print k

           for t in tup1:
                      print t"""

           for d in dict1:
                      print d
                      
def main():
           forloop1()
           forloop2()
           
if __name__ == "__main__":
           main()
