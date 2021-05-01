from datetime import date
from datetime import time
from datetime import datetime

def main():
    today=date.today()
    print("today date" , today )
    print ("Date components: ", today.day , today.month , today.year )
    print ("weeday ", today.weekday())
    days = ["mon", "tues", "wed", "thurs","fri", "sat","sun"]
    print("day is ", days[today.weekday()])
    todaydatetime = datetime.now()
    print("todat time and date" , todaydatetime.today())
    print("time" , todaydatetime.time())
   
if __name__ == "__main__":
    main()