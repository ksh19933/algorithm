import sys
input = sys.stdin.readline

s = input().rstrip()
flag = 0
answer = ""
tmp = ""


for c in s:
    if flag == False:
        if c == "<":
            flag = True
            tmp += c
        elif c == " ":
            tmp += c
            answer += tmp
            tmp = ""
        else:
            tmp = c + tmp ## tmp 앞에 c를 넣는다 ex) "abc"가 있고 "d"가 들어오는 상황이면 "d" + "abc"

    else:
        tmp += c
        if c == ">":
            flag = False
            answer += tmp
            tmp = ""

print(answer + tmp)