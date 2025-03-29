def suma(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


def pierwsze(*args):
    for i in args:
        # print(i)
        for j in range(i - 1, 1, -1):
            # print(j)
            if i % j == 0:
                # print("i%j==0")
                return False
    # print("none found")
    return True


# print(suma(1,2,3,4,5,6,7,8))
# print(pierwsze(1,2,3,5,17))
