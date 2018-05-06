def get_even_list(l):

    ln = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            ln.append(l[i])
    return ln

# a = get_even_list([1, 3, 4, 5, 10, 20])
# print(a)

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
