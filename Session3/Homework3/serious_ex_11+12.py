def is_inside(m, n):
# m = [100, 120]
# n = [140, 60, 100, 200]

    if n[0] < m[0] < (n[0] + n[2]):
        return True
    elif n[1] < m[1] < (n[1] + n[3]):
        return False

test_inside = is_inside([200, 120], [140, 60, 100, 200])
print(test_inside)
