class WordPattern:
    # given a pattern, and a string of words
    # this function determines if there is a
    # 1-to-1 match and outputs True or False
    def wordPattern(self, pattern: str, string: str) -> bool:
        # store pattern by character and string by space into lists
        key = list(pattern)
        val = string.split()
        dic = {}
        # patterns must be the same length as a basic requirement
        if len(key) != len(val):
            return False
        # for element in key, if not in dict, store in dict with val
        # if in dict, match vals
        # if match false, return
        for i in range (len(key)):
            if key[i] in dic.keys() and dic.get(key[i]) != val[i]:
                return False
            elif key[i] not in dic.keys():
                dic.update({key[i]: val[i]})
        # check for one-to-one matching in both directions
        temp = key
        key = val
        val = temp
        dic.clear()
        for i in range (len(key)):
            if key[i] in dic.keys() and dic.get(key[i]) != val[i]:
                return False
            elif key[i] not in dic.keys():
                dic.update({key[i]: val[i]})
        # once finished return true
        return True