import sys
input = sys.stdin.readline
n = int(input())
stack = []
result = []
count = 1
flag = True
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        count += 1
        result.append("+")
    if(stack[-1] == num):
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(-1)

for i in range(len(result)):
    print(result[i])