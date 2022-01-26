import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    ps = input().rstrip()
    stack  = []
    flag  = True
    for i in range(len(ps)):
        if ps[i] == ")":
            if not stack:
                flag = False
                break
            else:
                stack.pop()
        else:
            stack.append("(")
    if not stack and flag:
        print("YES")
    else:
        print("NO")