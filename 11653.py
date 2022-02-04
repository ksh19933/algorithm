import sys

input = sys.stdin.readline

prime = [True] * 10001

for i in range(2, 10001):
    if prime[i]:
        for j in range(2*i, 10001, i):
            prime[j] = False

num = int(input())

prime_num = 2

while num != 1:
    if num % prime_num == 0:
        print(prime_num)
        num //= prime_num
    else:
        prime_num += 1
        while not prime_num:
            prime_num += 1

