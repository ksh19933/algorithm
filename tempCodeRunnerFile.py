import sys

input = sys.stdin.readline

n = int(input())
nums = list(input().rstrip())
print(sum(list(map(int, nums))))