import sys
input = sys.stdin.readline
n = int(input())

num_arr = list(map(int, input().split()))
num_arr.sort()

result = 0

for i in range(n):
    if result+1 < num_arr[i]:
        break
    result += num_arr[i]

print(result+1)
