import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (1000001)
stack = []
result = [-1] * n
for i in range(n):
    dp[arr[i]] += 1

## stack[-1]에 있는 element의 dp 값보다 arr[i]의 dp 값이 작거나 같을 경우 stack에 idx를 append
## 클 경우 stack.pop하면서 idx를 빼낸 후 result[idx]에 arr[i] 값을 넣는다
for i in range(n):
    while stack and dp[arr[stack[-1]]] < dp [arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(' '.join(map(str,result)))


## dp를 dict type으로 하면 더 빠르고 메모리를 적게 먹는다...
# dp = dict()
# for i in range(n):
#     try :
#         dp[arr[i]] += 1
#     except:
#         dp[arr[i]] = 1