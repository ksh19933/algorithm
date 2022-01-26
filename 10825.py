import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    stack = list(input().split())
    for j in range(len(stack)):
        # for k in range(len(stack[j])):
        print(stack[j][::-1], end=" ")
    print()