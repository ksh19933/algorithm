import sys
input = sys.stdin.readline
str_num = [0] * 26
input_str = input().rstrip()
for i in range(len(input_str)):
    str_num[ord(input_str[i]) - 97] += 1
print(' '.join(map(str, str_num)))