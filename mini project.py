first = int(input("enter your fisrt : " ))
second  = int(input("enter your second : " ))
operator = input("enter operator (+,-,*,%,/): " )

if operator =="+":
    print(first + second )
elif operator =="-":
    print(first  - second )
elif operator =="*":
    print(first  * second )
elif operator =="%":
    print(first  % second )
elif operator =="/":
    print(first  / second )
else :
    print("invaild operator")



