import sys
input = sys.stdin.readline
stack = list(input().rstrip())
tmp = []
n = int(input())

##커서가 왼쪽으로 이동: stack[-1]가 tmp로 이동
##커서가 오른쪽으로 이동: tmp[-1]가 stack으로 이동
##출력순서는 stack은 정방향 tmp는 역방향
for _ in range(n):
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

## 아래의 for문을 다음과 같이 대체 가능
## print(''.join(stack + list(reversed(tmp))))
for i in range(len(stack)):
    print(stack[i], end="")

for j in range(len(tmp)-1, -1, -1):
    print(tmp[j], end= "")
    
