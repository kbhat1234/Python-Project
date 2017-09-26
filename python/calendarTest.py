import calendar

def calText_func():
           print "Text Calendar"
           c = calendar.TextCalendar(calendar.SUNDAY)
           str = c.formatmonth(2017,1)
           print str
           
           for i in c.itermonthdays(2017,1):
                      print i

           print "------------------------------weekday names are-----------------------------------"
           for day in calendar.day_name :
                      print day

           print "-----------------------------month names are---------------------------------------"
           for name in calendar.month_name :
                      print name

           print calendar.isleap(2022)
           print calendar.calendar(2017)
                      
def calHTML_func():
           print "HTML Calendar"
           c = calendar.HTMLCalendar(calendar.SUNDAY)
           str = c.formatmonth(2017,1)
           print str

           for i in c.itermonthdays(2017, 1):
                      print i

def main():
           calText_func()
           #calHTML_func()

if __name__ == "__main__":
           main()
