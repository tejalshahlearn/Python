#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
textcal = calendar.TextCalendar(calendar.SUNDAY)
St = textcal.formatmonth(2021, 3, 4 ,0)
print(St)
# create an HTML formatted calendar
Htmlcalc = calendar.HTMLCalendar(calendar.MONDAY)
ht = Htmlcalc.formatmonth(2021,8)
print(ht)
# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for monthname in calendar.month_name:
    print(monthname)
for dayname in calendar.day_name:
    print(dayname)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("teams meeting")
for m in range (1,13):
    cal =calendar.monthcalendar (2021, m)
    week1 =cal[0]
    week2 = cal[2]
    if week1[calendar.FRIDAY]!=0:
         meetday=week1[calendar.FRIDAY]
    else:
        meetday=week2[calendar.FRIDAY]
    print("%10s, %2d" %(calendar.month_name[m], meetday))
