from datetime import date, time, datetime, timedelta

def timedelta_func():
           timeDelta = timedelta(days=365, hours=8, minutes=15)
           print str(timeDelta)
           
           print "Today is: ", str(datetime.now())
           print "Today is: ", str(date.today())

           print "date 1 year from now: ", str(datetime.now() + timedelta(days=365))
           print "date 2 months from now: ", str(datetime.now() + timedelta(days=60))

           print "in one week and 4 days it will be ", str(datetime.now() + timedelta(weeks=1, days=4))
           today = date.today()
           nyd = date(2018,1,1)
           if(nyd < today):
                      print "New year day already went by " +str((today-nyd).days) + " ago"
           else:
                      print "New year yet to come by " +str((nyd-today).days) + " days"

def main():
           timedelta_func()

if __name__ == "__main__":
           main()
