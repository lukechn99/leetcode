# given a string of digits, count the number of ways the string can be split into prime numbers using the entire string


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
        if (i - j >= 0 and number[i - j] != '0' and isPrime(int(number[i - j: i]))):
            cnt += countPrimeStrings(number, i - j)
    return cnt
