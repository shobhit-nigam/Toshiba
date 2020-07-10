num = 100

x = int(input("please enter a whole number:\n"))

if x < num:
    print("x is lesser")
    if x > num//3 and x < num//2:
        print("quite low")
#    elif....
#    elif....
#    else
    # some code
elif x == num:
    print("x & num are same")
    # some more code
else:
    print("probably x is greater")
    
print("last line")

