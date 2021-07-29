def reductionCost(num):
    # find two loswest, remove them
    # keep track of two lowest
    # sort and insert new element in the right place
    num.sort()
    cost = 0
    while len(num) > 1:
        twosum = num[0] + num[1]
        num = num[1:]
        cost += twosum
        # insert
        i = 0
        while twosum < num[i]:
            i += 1
        num.insert(i, twosum)
    return cost


# print(reductionCost([3, 1, 2, 3]))

def mystery(a, b):
    x = a
    y = b
    while x != y:
        if x > y:
            x = x - y
        elif y > x:
            y = y - x
    return x


print(mystery(2437, 875))
