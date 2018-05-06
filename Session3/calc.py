x = int(input("Enter x: "))

calc = input("Operation (+, -, *, /): ")

y = int(input("Enter y: "))

if calc == "+":
    print("x + y =", x+y)
elif calc == "-":
    print("x - y =", x-y)
elif calc == "*":
    print("x * y =", x*y)
elif calc == "/":
    print("x / y =", float(x / y))
else:
    print("Wrong input")
