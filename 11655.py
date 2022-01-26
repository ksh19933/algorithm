import sys
input = sys.stdin.readline

string = list(input().rstrip())
for i in range(len(string)):
    if string[i].isupper():
        tmp = ord(string[i]) + 13
        if tmp > 90:
            tmp -= 26
        string[i] = chr(tmp)
    elif string[i].islower():
        tmp = ord(string[i]) + 13
        if tmp > 122:
            tmp -= 26
        string[i] = chr(tmp)

print(''.join(map(str, string)))
