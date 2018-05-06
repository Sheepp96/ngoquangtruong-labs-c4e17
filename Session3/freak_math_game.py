from random import *

m = randint(0,10)
n = randint(0,10)

op = ['+', '-', '*', '/']

op1 = choice(op)

if op1 == "+":
    result = m + n
elif op1 == "-":
    result = m - n
elif op1 == "*":
    result = m * n
elif op1 == "/":
    result = float(m / n)

error = randint(-1, 1)

# cho ra kết quả đúng nhiều hơn
# error = choice([0, 0, 0, 1])

display = result + error
print("{0} {1} {2} = {3}".format(m, op1, n, display))

a = str(input("(Y/N?) ")).upper()

if error == 0:
    if a == "Y":
        print("Wel-done")
    else:
        print("Game over")
else:
    if a == "Y":
        print("Game over")
    else:
        print("Wel-done")
