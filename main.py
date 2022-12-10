sum=0
while True:
    num=int(input("Num -->"))
    if num != 7:
        if num==0:
            print("«Number is equal to zero»")
        if num<=0:
            print("Number is negative")
        if num >= 0:
            print("Number is positive")
        sum+=num
    else:
        print("sum=",sum)