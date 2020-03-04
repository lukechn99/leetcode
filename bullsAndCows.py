# You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

# Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

# Please note that both secret number and friend's guess may contain duplicate digits.
def getHint(self, secret: str, guess: str) -> str:
    a = 0
    b = 0
    icache = set()
    jcache = set()
    length = len(secret)
    for i in range (0, length):
        if secret[i] == guess[i]:
            a += 1
            icache.add(i)
            jcache.add(i)
    for i in range (0, length):
        for j in range (0, length):
            if secret[i] == guess[j] and i not in icache and j not in jcache:
                b += 1
                icache.add(i)
                jcache.add(j)
    return str(a) + "A" + str(b) + "B"