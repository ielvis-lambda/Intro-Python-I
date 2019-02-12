"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

argNum = len(sys.argv)
today = datetime.today()

if argNum == 3:
	month = int(sys.argv[1]) 
	year = int(sys.argv[2])
elif argNum == 2:
	month = int(sys.argv[1]) 
	year = today.year
elif argNum == 1:
	month = today.month
	year = today.year
else:
	print("python3 cal.py month[int] year[int]")
	exit()

print(month)
print(year)

print(calendar.TextCalendar().formatmonth(year, month, 0, 0))