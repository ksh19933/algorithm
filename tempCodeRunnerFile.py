import sys

num = int(sys.stdin.readline().rstrip())
num_len = len(str(num))
min_num = abs(num-num_len*9)
flag = False
for i in range(min_num, num):
    small_num = sum(map(int, str(i)))
    if(i + small_num == num):
        flag = True
        num = i
        break

# while (min_num != num_len and min_num > 0):
#     small_num = sum(map(int, str(min_num)))
#     if(min_num + small_num == num):
#         flag = True
#         break
#     min_num += 1

if flag:
    print(num)
else:
    print(0)