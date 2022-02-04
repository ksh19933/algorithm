import sys

input = sys.stdin.readline

n = int(input())
nums = list(input().rstrip())
ans = 0

print(sum(list(map(int, nums))))

# 아래와 같은 로직
# for i in range(n):
#     ans += int(nums[i])

print(ans)