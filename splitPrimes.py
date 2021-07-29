# given a string of digits, count the number of ways the string can be split into prime numbers using the entire string

# fun split(string):
#     if the whole string is a prime:
#         return 1
#     ways = 0
#     for each length of the string:
#         if that length is prime:
#             ways += split(rest of the string)
#     return


def isPrime(number):
    num = number
    i = 2
    while i * i <= num:
        if ((num % i) == 0):
            return False
        i += 1
    return num > 1


def countPrimeStrings(number, i):
    if (i == 0):
        return 1
    cnt = 0
    for j in range(1, i + 1):
        if (number[i - j] != '0' and isPrime(int(number[i - j: i]))):
            cnt += countPrimeStrings(number, i - j)
    return cnt


if __name__ == "__main__":

    s1 = "3175"
    l1 = len(s1)
    print(countPrimeStrings(s1, l1))

    s2 = "11373"
    l2 = len(s2)
    print(countPrimeStrings(s2, l2))
