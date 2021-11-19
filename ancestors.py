# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

# For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

#                15
#               / \
#          14  13  21
#          |   |
# 1   2    4   12
#  \ /   / | \ /
#   3   5  8  9
#    \ / \     \
#     6   7     11

# parent_child_pairs_2 = [
#     (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
#     (15, 21), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
#     (12, 9), (15, 13)
# ]

# Write a function that takes this data and the identifiers of two individuals as inputs and returns true if and only if they share at least one ancestor. 

# Sample input and output:

# has_common_ancestor(parent_child_pairs_2, 3, 8)   => false
# has_common_ancestor(parent_child_pairs_2, 5, 8)   => true
# has_common_ancestor(parent_child_pairs_2, 6, 8)   => true
# has_common_ancestor(parent_child_pairs_2, 6, 9)   => true
# has_common_ancestor(parent_child_pairs_2, 1, 3)   => false
# has_common_ancestor(parent_child_pairs_2, 3, 1)   => false
# has_common_ancestor(parent_child_pairs_2, 7, 11)  => true
# has_common_ancestor(parent_child_pairs_2, 6, 5)   => true
# has_common_ancestor(parent_child_pairs_2, 5, 6)   => true
# has_common_ancestor(parent_child_pairs_2, 3, 6)   => true
# has_common_ancestor(parent_child_pairs_2, 21, 11) => true

# n: number of pairs in the input

parent_child_pairs_2 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (15, 21),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
    (15, 13)
]

def has_common_ancestor(pairs, a, b):
    parent_tracker = {}
    for pair in pairs:
        if pair[0] not in parent_tracker:
            parent_tracker[pair[0]] = []
        if pair[1] in parent_tracker:
            parent_tracker[pair[1]].append(pair[0])
        else:
            parent_tracker[pair[1]] = [pair[0]]
            
    a_ancestors = []
    a_queue = parent_tracker[a]
    while a_queue:
        cur_parent = a_queue.pop(0)
        a_ancestors.append(cur_parent)
        temp = parent_tracker[cur_parent]
        print(parent_tracker[cur_parent])
        a_queue += temp
        
    b_ancestors = []
    b_queue = parent_tracker[b]
    while b_queue:
        cur_parent = b_queue.pop(0)
        b_ancestors.append(cur_parent)
        b_queue += parent_tracker[cur_parent]
        
#     print(a_ancestors, b_ancestors)
    common = {}
    for entry in a_ancestors:
        common[entry] = 0
    for entry in b_ancestors:
        if entry in common:
            return True
    return False
            
print(has_common_ancestor(parent_child_pairs_2, 5, 6))#,has_common_ancestor(parent_child_pairs_2, 5, 8), has_common_ancestor(parent_child_pairs_2, 6, 8), has_common_ancestor(parent_child_pairs_2, 6, 9), has_common_ancestor(parent_child_pairs_2, 1, 3) , has_common_ancestor(parent_child_pairs_2, 3, 1), has_common_ancestor(parent_child_pairs_2, 7, 11), has_common_ancestor(parent_child_pairs_2, 6, 5), has_common_ancestor(parent_child_pairs_2, 5, 6), has_common_ancestor(parent_child_pairs_2, 3, 6), has_common_ancestor(parent_child_pairs_2, 21, 11))
    
# parent_child_pairs = [
#     (5, 6), (1, 3), (2, 3), (3, 6), (15, 12),
#     (5, 7), (4, 5), (4, 9), (9, 12), (30, 16)
# ]

def find(pairs):
    parent_count = {}
    for pair in pairs:
        if pair[0] not in parent_count:
            parent_count[pair[0]] = 0
        if pair[1] in parent_count:
            parent_count[pair[1]] += 1
        else:
            parent_count[pair[1]] = 1
    parentless = []
    oneparent = []
    for person in parent_count.keys():
        if parent_count[person] == 0:
            parentless.append(person)
        elif parent_count[person] == 1:
            oneparent.append(person)
    return [parentless, oneparent]
        
# print(find(parent_child_pairs))

# O(n)

# O(n)