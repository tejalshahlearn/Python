#Formatting time output
from datetime import datetime
def main():
    todaydatetime = datetime.now()
    print("todat time and date" , todaydatetime.today())
    print("time" , todaydatetime.time())
    print(todaydatetime.strftime("the year is :%y"))
    print(todaydatetime.strftime("the year is :%a ,%d ,%b, %y,%X ,%p"))
   
if __name__ == "__main__":
    main()