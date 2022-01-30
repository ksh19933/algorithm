import sys
input = sys.stdin.readline
def dfs(x, y, depth):
    global max_move
    max_move = max(max_move, depth)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and check[board[nx][ny]] == 0:
            check[board[nx][ny]] = 1
            dfs(nx, ny, depth+1)
            check[board[nx][ny]] = 0

r, c = map(int, input().split())
board = []
for i in range(r):
    tmp = list(input().rstrip())
    for j in range(c):
        tmp[j] = ord(tmp[j]) - 65
    board.append(tmp)
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

check = [0] * 26
max_move = 0
check[board[0][0]] = 1
dfs(0, 0, 1)
print(max_move)

## ================= BFS 풀이 =============== ##
# import sys
# from collections import deque
# input = sys.stdin.readline

# r, c = list(map(int, input().split()))
# board = [list(input().rstrip()) for _ in range(r)]
# # for i in range(r):
# #     tmp = list(input().rstrip())
# #     for j in range(c):
# #         tmp[j] = ord(tmp[j]) - 65
# #     board.append(tmp)
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# max_move = 0

# que = set()
# que.add((0, 0, board[0][0]))
# while que:
#     x, y, alph_list = que.pop()
#     max_move = max(max_move, len(alph_list))
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in alph_list:
#             que.add((nx, ny,  board[nx][ny]+alph_list))

# print(max_move)
