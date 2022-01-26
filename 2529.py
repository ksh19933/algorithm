import sys
input = sys.stdin.readline
def dfs(idx, arr):
    if len(arr) == n+1:
        # print(arr)
        answer.append(arr[:])
        return

    for i in range(10):
        if not used[i]:
            if (opr[idx] == "<" and arr[-1] < num[i]) or (opr[idx] == ">" and arr[-1] > num[i]):
                arr.append(num[i])
                used[i] = True
                idx += 1
                dfs(idx, arr)
                arr.pop()
                used[i] = False
                idx -= 1


n = int(input())
opr = input().split()
num = [0,1,2,3,4,5,6,7,8,9]
used = [False] * 10
answer = []

for i in range(10):
    used[i] = True
    dfs(0, [i])
    used[i] = False

answer.sort()
print(''.join(map(str, answer[-1])))
print(''.join(map(str, answer[0])))


## 아래와 같은 방법도 있다.

# n = int(input())
# arr = input().split()
# def func(a, l, b):
#     ans = [-1] * (n + 1)
#     i, j = 0, 0
#     while j < n:
#         if arr[j] == a:
#             for k in range(j, i - 1, -1):
#                 ans[k] = l
#                 l += b
#             i = j + 1
#         j += 1
#     for k in range(j, i - 1, -1):
#         ans[k] = l
#         l += b
#     for i in range(n + 1):
#         if ans[i] < 0:
#             ans[i] = l
#             l += b
#     print(''.join(map(str, ans)))
#     return
# func('>', 9, -1)
# func('<', 0, 1)

