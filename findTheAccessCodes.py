# Find the Access Codes
# =====================

# In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But
# the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number
# of passcodes changes daily. Commander Lambda gets a report every day that includes the locks'
# access codes, but only she knows how to figure out which of several lists contains the access
# codes. You need to find a way to determine which list contains the access codes once you're
# ready to go in. 

# Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that
# she made all the access codes "lucky triples" in order to help her better find them in the
# lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as
# (1, 2, 4). With that information, you can figure out which list contains the number of access
# codes that matches the number of locks on the door when you're ready to go in (for example, if
# there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

# Write a function solution(l) that takes a list of positive integers l and counts the number of
# "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The
# length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999
# inclusive.  The answer fits within a signed 32-bit integer. Some of the lists are purposely
# generated without any access codes to throw off spies, so if no triples are found, return 0. 

# For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the
# answer 3 total.

import unittest

# brute force??? O(n^3)
# sort list
# starting with largest number as z
# find largest y
# with y, find x
# continue to next y and x
# def solution(l):
#     keys = 0
#     for z in reversed(range(len(l))):
#         for y in reversed(range(z)):
#             if l[z] % l[y] == 0:
#                 for x in reversed(range(y)):
#                     if l[y] % l[x] == 0:
#                         keys += 1
#     return keys

# fill out a list with indicies marked with how many viable doubles come from there
# when a new double is found, it checks the bottom part of the double to see if
# the bottom forms a double, which would make the new double a triple
def solution(l):
    seen = [0] * len(l)
    keys = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                seen[i] = seen[i] + 1
                keys = keys + seen[j]
    return keys

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([1, 1, 1]), 1)
    def test2(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 3)
    def test3(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8]), 6)
    def test4(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 16]), 12)

if __name__=="__main__":
    # main()
    unittest.main()