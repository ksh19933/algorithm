import sys
input = sys.stdin.readline
n, m = input().split()
A = set(map(int, input().split()))
B = set(map(int, input().split()))
ans = len(A) + len(B) - 2 * len(A & B)
print(ans)