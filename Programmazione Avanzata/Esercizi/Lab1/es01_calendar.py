import calendar
import datetime

def getNextLeapYear():
    yearToCheck = datetime.datetime.now().year
    while not calendar.isleap(yearToCheck):
        yearToCheck += 1
    return yearToCheck



print("Next Leap Year: ",getNextLeapYear())
print("NUmber of leap years between 2020 and 2050 (inclusive): ",calendar.leapdays(2019, 2050))
print("July 29, 2016 was a ",calendar.day_name[calendar.weekday(2016, 7, 29)])