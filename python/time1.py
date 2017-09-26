import time

def time_func():
           localtime = time.localtime(time.time())
           print time.time()
           print localtime
           print time.clock()
           print time.ctime()
           print time.altzone
           localtime = time.asctime( time.localtime(time.time()) )  
           print localtime  
           print "sleep for 10 seconds", time.sleep( 10 )  
           localtime = time.asctime( time.localtime(time.time()) )  
           print localtime
           print time.daylight
           print time.gmtime()
           print time.timezone
           print time.tzname
           print "Sleep for 10 seconds", time.sleep(10)
           print time.strptime("26 Sep 17", "%d %b %y")
           

def main():
           time_func()

if(__name__ == "__main__"):
           main()
           
