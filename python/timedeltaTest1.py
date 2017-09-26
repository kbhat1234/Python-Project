from datetime  import timedelta, date, time, datetime

def timedelta_func():
           today = datetime.now()
           deltatime = timedelta(days=365, hours=8, minutes=15)
           print "Today is: ", today
           print "Time delta: ", deltatime

           d= date.today()
           nyd = date(d.year,1,1)

           if(nyd<d):
                      print "new year day is already went by ", str((d-nyd).days) +" days"
           else:
                      print "new year day is yet to come by ", str((nyd-d).days) +" days"

def main():
           timedelta_func()

if __name__ == "__main__":
           main()
