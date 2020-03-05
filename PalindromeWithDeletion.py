class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        elif s[0] == s[-1]:
            return self.validPalindrome(s[1:][:-1])
        elif s[1] == s[-1] and s[0] == s[-2]:
            if s[2] == s[-2]:
                return self.palinAux(s[1:])
            elif s[1] == s[-3]:
                return self.palinAux(s[:-1])
        elif s[1] == s[-1]:
            return self.palinAux(s[2:][:-1])
        elif s[0] == s[-2]:
            return self.palinAux(s[1:][:-2])
        else:
            return False
    
    def palinAux(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        elif s[0] == s[-1]:
            return self.palinAux(s[1:][:-1])
        else:
            return False
        
    def palin_debug(s, i):
        if len(s) <= 1:
            print("final " + s)
            return True
        elif s[0] == s[-1]:
            print("at index " + str(i) + " and "+ str(101 -i) + ". Val: " + s[0])
            i += 1
            return palin_debug(s[1:][:-1], i)
        else:
            print("error at " + str(i) + " and "+ str(101 -i) + ". Mismatch: " + s[0] + " and " + s[-1])
            print("next chars are " + str(s[1]) + " and " + str(s[-2]) + ". Perhaps it's recoverable")
            return False
    
print(palin_debug("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", 0))