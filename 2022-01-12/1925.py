import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().rstrip())
num_arr = [] # 3번째줄부터 시작하는 A~Z 값을 담아둘 array
num_stack = [] # 피연산자가 담길 stack
for _ in range(n):
    num_arr.append(int(input()))

for i in range(len(arr)):
    if 65 <= ord(arr[i]) <= 90:
        num_stack.append(num_arr[ord(arr[i]) - 65])
    else:
        tmp1 = num_stack.pop()
        tmp2 = num_stack.pop()

        if arr[i] == "+":
            num_stack.append(tmp2+tmp1)
        elif arr[i] == "-":
            num_stack.append(tmp2-tmp1)
        elif arr[i] == "*":
            num_stack.append(tmp2*tmp1)
        elif arr[i] == "/":
            num_stack.append(tmp2/tmp1)

print('%.2f'%num_stack[0])





