#fomat the time output

from datetime import date
from datetime import time
from datetime import datetime

def main():
           now = datetime.now()

           print now.strftime("%Y") #prints year as YYYY (2017)
           print now.strftime("%y") #prints year as yy (17)
           print now.strftime("%a") #prints weekday name as Mon
           print now.strftime("%A") #prints weekday name as Monday
           print now.strftime("%b") #prints month name as Sep
           print now.strftime("%B") #prints month name as September
           print now.strftime("%d") #prints date

           print now.strftime("%a, %d, %b, %y") #prints output as Mon, 25, Sep, 17

           print now.strftime("%A, %d, %B, %Y") #prints output as Monday, 25, September, 2017

           print now.strftime("%c") #prints output as 09/25/17 14:28:14
           print now.strftime("%x") #prints output as 09/25/17
           print now.strftime("%X") #prints output as 14:28:14

           print now.strftime("%I:%M:%S %p")
           print now.strftime("%H:%M %p")
           
           
if __name__ == "__main__":
           main()
