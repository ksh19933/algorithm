import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
stack = []
priority = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
for i in range(len(arr)):
    if "A" <= arr[i] <= "Z":
        print(arr[i], end = "")
    else:
        if arr[i] == ")":
            while stack and stack[-1] != "(":
                print(stack.pop(), end = "")
            stack.pop()
        elif arr[i] == "(":
            stack.append("(")
        else:
            while stack and (priority[arr[i]] <= priority[stack[-1]]):
                print(stack.pop(), end = "")
            stack.append(arr[i])

while stack:
    print(stack.pop(), end = "")

