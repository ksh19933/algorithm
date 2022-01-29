import sys
input = sys.stdin.readline

def num_check(x, y, num):
    for i in range(9):
        if sqr[x][i] == num or sqr[i][y] == num or sqr[x//3*3 + i//3][y//3*3 + i%3] == num:
            return False
    return True

sqr = []
zero_location = []

for i in range(9):
    tmp = list(map(int, input().split()))
    sqr.append(tmp)
    for j in range(9):
        if tmp[j] == 0:
            zero_location.append([i,j])

def dfs(idx):
    if idx == len(zero_location):
        for row in sqr:
            print(*row)
        exit(0)
    for num in range(1, 10):
        x, y = zero_location[idx]
        if num_check(x, y, num):
            sqr[x][y] = num
            dfs(idx+1)
            sqr[x][y] = 0

dfs(0)

# pypy3로 통과함 
# row, col, box에 대해 1~9를 체크하는 check board를 만들고 확인면서 들어갈 경우 python3으로 통과 가능

def dfs(depth):
    if depth == len(zero_location):
        for v in sqr:
            print(*v)
        exit(0)
        
    x,y = zero_location[depth]
    for n in range(1,10):
        if not row_check[x][n] and not col_check[y][n] and not box_check[x//3*3+y//3][n]:
            row_check[x][n] = col_check[y][n] = box_check[x//3*3+y//3][n] = True
            sqr[x][y] = n
            dfs(depth+1)
            row_check[x][n] = col_check[y][n] = box_check[x//3*3+y//3][n] = False
            sqr[x][y] = 0


sqr = [list(map(int,input().split())) for _ in range(9)]
row_check = [[False]*10 for _ in range(10)]
col_check = [[False]*10 for _ in range(10)]
box_check = [[False]*10 for _ in range(10)]
zero_location = []
for r in range(9):
    for c in range(9):
        if sqr[r][c] == 0: 
            zero_location.append([r,c])
        else:
            row_check[r][sqr[r][c]] = True
            col_check[c][sqr[r][c]] = True
            box_check[r//3*3+c//3][sqr[r][c]] = True
dfs(0)