from random import *

#khai báo function
def calc(m, n, op):
    # m = randint(0,10)
    # n = randint(0,10)
    # op1 = choice(['+', '-'])

    result = 0
    # op1 = "+"

    if op == "+":
        result = m + n
    elif op == "-":
        result = m - n
    elif op == "*":
        result = m * n
    elif op == "/":
        result = float(m / n)

    return result

# print(result)

# mỗi function thì chỉ nên thực hiện 1 chức năng
# usage/call function
# calc(3, 7, '-')

#return arguments
# result = calc(1, 2, '+')
#
# print(result)

# print(__name__) # khi file đc chạy trực tiếp - __name__ có giá trị là __main__
                  # khi file đc chạy gián tiếp - __name__ có giá trị là tên file

if __name__ == "__main__":
    print('eval.py imported')
