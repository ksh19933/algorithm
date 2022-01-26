import sys
input = sys.stdin.readline

arr = input().rstrip()
result = 0
tmp = 0
for i in range(len(arr) -1):
    if arr[i] == "(":
        if arr[i+1] == ")":
            result += tmp
        else:
            result += 1
            tmp += 1
    else:
        if tmp > 0 and arr[i-1] != "(":
            tmp -= 1
    # print("i: {}, tmp: {}, result: {}".format(i, tmp, result))
print(result)

## tmp를 stack으로하여 푸는 방법도 있다.