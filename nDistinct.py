# given a string, find the number of substrings that have n distinct characters

# use sliding window

def distinct(string, ptr1, ptr2):
    pass


def nDistinct(string, n):
    ptr1 = 0
    ptr2 = n

    number_distinct = 0

    while ptr1 < len(string) - n:
        while ptr2 < len(string):
            if distinct(string, ptr1, ptr2):
                number_distinct += 1
            ptr2 += 1
        ptr1 += 1
        ptr2 = ptr1 + n
    return number_distinct


# we could also maintain a table of the characters and each time we slide we add or remove accordingly
