import sys

def dfs(sum, depth, add, sub, mul, div):
    global max_n, min_n
    if depth == n:
        max_n = max(max_n, sum)
        min_n = min(min_n, sum)
        return
    if add:
        dfs(sum+num_list[depth], depth+1, add-1, sub, mul, div)
    if sub:
        dfs(sum-num_list[depth], depth+1, add, sub-1, mul, div)
    if mul:
        dfs(sum*num_list[depth], depth+1, add, sub, mul-1, div)
    if div:
        dfs(int(sum/num_list[depth]), depth+1, add, sub, mul, div-1)

n = int(input())
num_list = list(map(int, input().split()))
operation = list(map(int, input().split()))
max_n = -1e9
min_n = 1e9

dfs(num_list[0], 1, operation[0], operation[1], operation[2], operation[3])

print(max_n)
print(min_n)