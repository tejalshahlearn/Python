def main():
    x=0
# define a while loop 
    while (x<5):
        print(str(x) +"in a while")
        x=x+1
# Define afor loop 
    for x in range(5,10):
        print(x)
#use for loop over a collection
    days= ["mon","Tue", "wed", "thu","fri","sat","sun"]
    for d in days:
        print(d + "only for")
#use Break and continue statement
    days= ["mon","Tue", "wed", "thu","fri","sat","sun"]
    for d in days:
        if (d=="wed"):break
        print(d)
#continue statement 
    for x in range(5,10):
        if (x % 2 == 0): continue
        print(x)
#use for enumerate to get index 
    days= ["mon","Tue", "wed", "thu","fri","sat","sun"]
    for i,d in enumerate(days):
        print(i ,d + "only for")
if __name__ =="__main__":
    main()