
first = int(input("enter the first number : "))
second =int(input("enter the second number : "))
operator = input("enter operator (+,-,/,*,**) : ")
if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator =="/":
    print(first%second)
elif operator=="*":
    print(first*second)
elif operator =="**":
    print(first**second)
else:
    print("Invalid operator")
