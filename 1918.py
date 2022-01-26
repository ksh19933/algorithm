import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
stack = []
# 각 연산자의 우선순위를 담아둘 dictionary
# 괄호의 경우 원래라면 우선순위가 가장 높지만 괄호의 처리는 다른 케이스로 처리하기 때문에 priority를 0으로 주었다
priority = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
for i in range(len(arr)):
    # 피연산자 일 경우 그대로 출력 // 아스키 코드를 써도 된다.
    if "A" <= arr[i] <= "Z":
        print(arr[i], end = "")
    else:
        # 닫는 괄호일 경우 여는 괄호가 나올때까지 연산자 stack을 pop하면서 print
        if arr[i] == ")":
            while stack and stack[-1] != "(":
                print(stack.pop(), end = "")
            stack.pop()
        # 여는 괄호는 stack에 그대로 넣는다.
        elif arr[i] == "(":
            stack.append("(")
        else:
            # 만약 우선순위가 같거나 낮을 경우 stack을 pop하고 print한 후 해당 연산자를 stack에 넣는다.
            while stack and (priority[arr[i]] <= priority[stack[-1]]):
                print(stack.pop(), end = "")
            stack.append(arr[i])

# stack에 남은 연산자들을 출력
while stack:
    print(stack.pop(), end = "")

