# Please Pass the Coded Messages
# ==============================

# You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed
# to use is... obscure, to say the least. The bunnies are given food on standard-issue prison
# plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets
# of plates to create the numbers in the code. The signal that a number is part of the code is
# that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers
# like 144 and 414 are a little trickier. Write a program to help yourself quickly create large
# numbers for use in the code, given a limited number of plates to work with.

# You have L, a list containing some digits (0 to 9). Write a function solution(L) which finds the
# largest number that can be made from some or all of these digits and is divisible by 3. If it is
# not possible to make such a number, return 0 as the solution. L will contain anywhere from 1 to 9
# digits.  The same digit may appear multiple times in the list, but each element in the list may
# only be used once.

import unittest
import itertools

def solution(l):
    return helper(sorted(l, reverse = True))

def helper(l):
    if l == []:
        return 0
    if sum(l) % 3 != 0:
        potentials = []
        for i in range(len(l)):
            new_l = l[:i] + l[i + 1:]
            potentials.append(helper(new_l))
        if potentials == []:
            return 0
        return max(potentials)
    else:
        str_list = [str(n) for n in l]
        cur_perm = "".join(str_list)
        int_cur_perm = int(cur_perm)
        return int_cur_perm
            

# wrong solution, we must consider subsets
# def solution(l):
#     perm = list(itertools.permutations(l))
#     max = 0
#     for p in perm:
#         # convert to int
#         str_list = [str(n) for n in p]
#         cur_perm = "".join(str_list)
#         int_cur_perm = int(cur_perm)
#         if int_cur_perm > max and int_cur_perm % 3 == 0:
#             max = int_cur_perm
#             print(max)
#     return max

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([3, 1, 4, 1]), 4311)
    def test2(self):
        self.assertEqual(solution([3, 1, 4, 1, 5, 9]), 94311)

if __name__=="__main__": 
    # main()
    unittest.main()