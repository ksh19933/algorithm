import sys
input = sys.stdin.readline
stack = list(input().rstrip())
tmp = []
n = int(input())

for i in range(n):
    order_ = list(input().rstrip().split())
    if order_[0] == "P":
        stack.append(order_[1])
    elif order_[0] == "L":
        if stack:
            tmp.append(stack.pop())
    elif order_[0] == "B":
        if stack:
            stack.pop()
    else:
        if tmp:
            stack.append(tmp.pop())

for i in range(len(stack)):
    print(stack[i], end="")

for j in range(len(tmp)-1, -1, -1):
    print(tmp[j], end= "")