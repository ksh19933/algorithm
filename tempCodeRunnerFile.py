import sys
input = sys.stdin.readline
n = input()
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(sorted(list(A.union(B))))