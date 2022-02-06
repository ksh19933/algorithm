import sys
input = sys.stdin.readline
n = input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(' '.join(map(str, sorted(A+B))))