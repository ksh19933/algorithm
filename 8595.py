import sys

ans = 0
n = int(sys.stdin.readline())
words = list(sys.stdin.readline().rstrip())
tmp = "0"
for i in range(n):
    if "0" <= words[i] <= "9":
        tmp += words[i]
    else:
        ans += int(tmp)
        tmp = "0"

ans += int(tmp)
print(ans)
