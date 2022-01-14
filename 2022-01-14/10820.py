import sys

while True:
    strings = sys.stdin.readline().rstrip('\n')
    result = [0] * 4

    if not strings:
        break
    for s in strings:
        if 'a' <= s <= 'z':	# 대문자
            result[0] += 1
        elif 'A' <= s <= 'Z':	# 소문자
            result[1] += 1
        elif "0" <= s <= "9":	# 숫자
            result[2] += 1
        else:	# 공백
            result[3] += 1
    print(' '.join(map(str, result)))

# isdisit, isupper, islower, isspace를 이용할 수 있음