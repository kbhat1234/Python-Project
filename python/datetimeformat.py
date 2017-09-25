from datetime import datetime

def dateTimeFormatFunc():
           now = datetime.now()
           print "Year format(YYYY) is ", now.strftime("%Y")
           print "Year format(YY) is ", now.strftime("%y")
           print "Weekday name (format Wed) is ", now.strftime("%a")
           print "Weekday name (format Wednesday) is ", now.strftime("%A")
           print "Month name (format June) is ", now.strftime("%b")
           print "Month nane (format Jun) is ", now.strftime("%B")
           print "Local date and time: ", now.strftime("%c")
           print "Local date: ", now.strftime("%X")
           print "Local time: ", now.strftime("%x")

           print "Date and time is (format1) ", now.strftime("%Y, %A, %B, %d, %c")
           print "Date and time is (format2) ", now.strftime("%y, %a, %b, %d, %c")

           print "Current time(12 hours): ", now.strftime("%I:%M:%S %p")
           print "Current time(12 hours): ", now.strftime("%H:%M:%S %p")
           print "Current time(24 hours): ", now.strftime("%H:%M")

def main():
           dateTimeFormatFunc()

if __name__ == "__main__":
           main()
