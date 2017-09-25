from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def date_func():
           #using date object
           print "=======================Using Date Object====================="
           today_date = date.today()
           day = today_date.day
           month = today_date.month
           year = today_date.year

           print "Today's date is : ",today_date
           print "Date components are: ", day, month, year

           weekday = today_date.weekday()
           if (weekday == 0):
                      print "Monday"
           elif(weekday == 1):
                      print "Tuesday"
           elif(weekday == 2):
                      print "Wednesday"
           elif(weekday == 3):
                      print "Thursday"
           elif(weekday == 4):
                      print "Friday"
           elif(weekday == 5):
                      print "Saturday"
           else:
                      print "Sunday"

           print "_______________________________________________________________"

def datetime_func():
           #using datetime objects
           print "===================Using datetime objects================="
           today = datetime.now()
           day = today.day
           month =today.month
           year = today.year

           print "Today's date and time is ", today
           print "Date and time components: ", day, month, year

           weekday = today.weekday()
           if(weekday == 0):
                      print "Monday"
           elif(weekday == 1):
                      print "Tuesday"
           elif(weekday == 2):
                      print "Wednesday"
           elif(weekday == 3):
                      print "Thursday"
           elif(weekday == 4):
                      print "Friday"
           elif(weekday == 5):
                      print "Saturday"
           else:
                      print "Sunday"
           
           print "_______________________________________________________________________"

def time_func():
           #using time object get only time
           print "====================Display time only using time class====================="
           time = datetime.time(datetime.now())
           print "The current time is ", time
           print "_______________________________________________________________________"
           
def date_weekday():
           #using date object using weekday number find the day
           print "==============================================================="
           today = date.today()
           wd = date.weekday(today)
           days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
           print "Today is day number ", wd
           print "which is a ", days[wd]
