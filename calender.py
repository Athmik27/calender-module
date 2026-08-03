import time
import calendar
current_time=time.time()
print(current_time) #here output is in unix timestamp

#time in redable format
current_time=time.asctime(time.localtime(time.time()))
print(current_time)
# asctime() function give the time in read-able format

#get the calendar of specific year and the specified month
print(calendar.month(2030,1))
#this gives the calender of the year 2030,Jan
#calendar.month(year,month,day)

#if we need to set the 1st day of the week as Tuesday
calendar.setfirstweekday(1)
print(calendar.month(2030,2))
#calender.setfirstweekday(argument) in argument use this numbers
#0 = Monday
#1 = Tuesday
#2 = Wednesday
#3 = Thursday
#4 = Friday
#5 = Saturday
#6 = Sunday

#to find the yeap year
is_leap=calendar.isleap(2028)
print(is_leap)

#to find leap days
is_leap=calendar.leapdays(2028,2030)
print(is_leap)
#this returns the number of leap year between 2028 and 2030
#we use leapdays() and not isleapdays() as function with "is" gives us boolean