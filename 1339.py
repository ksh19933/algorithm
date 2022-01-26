import sys
input = sys.stdin.readline
n = int(input())

alpha_list = [] 
alpha_dict = {}
num_list = []

## 단어들을 받는다.
for i in range(n):
    alpha_list.append(input().rstrip())

for i in range(n):
    for j in range(len(alpha_list[i])):
        try:
            alpha_dict[alpha_list[i][j]] += 10 ** (len(alpha_list[i])-j-1)
        except: 
            alpha_dict[alpha_list[i][j]] = 10 ** (len(alpha_list[i])-j-1)


## 위에서 구한 값을 num_list에 저장
for val in alpha_dict.values():
    num_list.append(val)

## 큰 수부터 높은 수를 받을 수 있게 내림차순 정렬
num_list.sort(reverse=True)

sum = 0
## 가장 큰 수부터 9, 8, 7, 6 순으로 곱해준다. 그리고 이 것을 결과값과 더한다.
for i in range(len(num_list)):
    sum += num_list[i] * (9 - i)

print(sum)




