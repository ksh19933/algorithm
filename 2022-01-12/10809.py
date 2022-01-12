import sys
input = sys.stdin.readline
str_list = list(input().rstrip())
dp = [-1] * 26

for i in range(len(str_list)):
    location = ord(str_list[i]) - 97
    if dp[location] == -1:
        dp[location] = i

print(' '.join(map(str, dp)))