import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
circle = [i for i in range(1, n+1)]
result = []

idx = 0
for i in range(n):
    idx += m-1
    if idx >= len(circle):
        idx %= len(circle)
    result.append(circle.pop(idx))

print("<", end= "")
print(', '.join(map(str, result)), end= "")
print(">")

