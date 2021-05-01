def  main():
    x,y= 100,100
    #Conditional flow uses if ,elif,else
    if (x<y):
        st =" x is less than y"
    elif(x==y):
        st =" x is same as  y"
    else:
        st ="x is greter than y"
    print(st)
    st="x is in conditional statement " if (x<y) else "x is greater thn or same"
    print(st)
if __name__ == "__main__":
    main()