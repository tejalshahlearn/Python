#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365,hours=5,minutes=10))

# print today's date
timedate =datetime.now()
print("todays date "+str(timedate))



# print today's date one year from now
print("one year from now",timedate+ timedelta(days=365))

# create a timedelta that uses more than one argument
print("2 days from now",timedate+ timedelta(days=2,hours=5,minutes=10))

# calculate the date 1 week ago, formatted as a string
print("1 week from now",timedate - timedelta(days=7,hours=5,minutes=10))

weekago= timedate - timedelta(days=7,hours=5,minutes=10)
strweekago = weekago.strftime("%A %B %d %y")
print("1 week from now",strweekago)

### How many days until April Fools' Day?
aprilfd= datetime(timedate.year,4,1)
print(aprilfd)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if (aprilfd < timedate):
    print( "april fool day has passed" )
    aprilfd = aprilfd.replace(aprilfd.year +1)
    print ("new april fool day", aprilfd)
else:
     print( "april fool day has  not passed" )
     print ("new april fool day", aprilfd)

# Now calculate the amount of time until April Fool's Day
daysleft= aprilfd -timedate
print(daysleft.days ,"days left ")

