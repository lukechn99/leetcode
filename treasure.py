# PALANTIR

import math
"""
Now the board also includes treasures, denoted by 1.

Given a board and start and end positions for the player, write a function to return the shortest simple path of open spaces from start to end that includes all the treasures, if any exist. If multiple shortest paths exist, return any of them. A simple path is one that does not revisit any location.

board3_1 = [
    [  1,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, 1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ],
]

board3_2 = [
    [  0,  1, -1 ],
    [  0,  0,  0 ],
    [  0,  0,  0 ],
]

treasure(board3_1, (5, 0), (0, 4)) -> None

treasure(board3_1, (5, 2), (2, 0)) ->
  [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]
  Or
  [(5, 2), (5, 1), (4, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0)]

treasure(board3_1, (0, 0), (4, 1)) ->
  [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (3, 2), (3, 1), (4, 1)]
  Or
  [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1)]

treasure(board3_2, (2, 1), (1, 2)) ->
  [(2, 1), (2, 0), (1, 0), (0, 0), (0, 1), (1, 1), (1, 2)]

n: width of the input board
m: height of the input board



"""
board3_1 = [
    [  1,  0,  0, 0, 0 ],
    [  0, -1, -1, 0, 0 ],
    [  0, -1,  0, 1, 0 ],
    [ -1,  0,  0, 0, 0 ],
    [  0,  1, -1, 0, 0 ],
    [  0,  0,  0, 0, 0 ],
]

board3_2 = [
    [  0, 1, -1, ],
    [  0, 0,  0, ],
    [  0, 0,  0, ],
]

def findLegalMoves(board, coord):
    moves = []
    # up
    if coord[0] - 1 >= 0 and board[coord[0] - 1][coord[1]] != -1:
        moves.append((coord[0] - 1, coord[1]))
    # down
    if coord[0] + 1 < len(board) and board[coord[0] + 1][coord[1]] != -1:
        moves.append((coord[0] + 1, coord[1]))
    # left
    if coord[1] - 1 >= 0 and board[coord[0]][coord[1] - 1] != -1:
        moves.append((coord[0], coord[1] - 1))
    # right
    if coord[1] + 1 < len(board[0]) and board[coord[0]][coord[1] + 1] != -1:
        moves.append((coord[0], coord[1] + 1))
    return moves


def isReachable(board, coord):
    visited = {}
    queue = []
    num_valid = 0
    first_found = False
    # find first valid spot, count number of 0s
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[j][i] == 0 and not first_found:
                first_found = True
                queue.append((j, i))
                num_valid += 1
            elif board[j][i] == 0:
                num_valid += 1
    while queue:
        cur_cell = queue.pop(0)
        visited[cur_cell] = True
        queue += [cell for cell in findLegalMoves(board, cur_cell) if cell not in visited]
    print(len(visited) == num_valid and coord in visited)
    return len(visited) == num_valid and coord in visited

def treasure(board, start, end):
    # count number of treasures here
    treasures = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                treasures += 1
                
    def aux(board, start, end, length, visited, found, treasures):
        '''
        returns the length of a valid path, +inf otherwise
        '''
        if start == end and found != treasures:
            return math.inf
        valid_moves = [move for move in findLegalMoves(board, start) if move not in visited]
        valid_paths = []
        for move in valid_moves:
            visited_copy = visited
            visited_copy[move] = True
            treasures_found = found
            if board[move[0]][move[1]] == 1:
                treasures_found += 1
            valid_paths.append(aux(board, move, end, length + 1, visited_copy, treasures_found, treasures))
        
        return min(valid_paths)
    
    return aux(board, start, end, 0, {}, 0, treasures)

treasure(board3_1, (5, 0), (0, 4))

treasure(board3_1, (5, 2), (2, 0))

treasure(board3_1, (0, 0), (4, 1))

treasure(board3_2, (2, 1), (1, 2))

'''
O(mn + mn) -> O(2mn) -> O(mn) 
O(mn)
'''