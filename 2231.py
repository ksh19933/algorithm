import sys

num = int(sys.stdin.readline().rstrip())
num_len = len(str(num))
if num  < 20:
    for i in range(1, num):
        small_num = sum(map(int, str(i)))
        if(i + small_num == num):
            print(i)
            exit(0)
else:
    min_num = abs(num-num_len*9)
    flag = False
    for i in range(min_num, num):
        small_num = sum(map(int, str(i)))
        if(i + small_num == num):
            print(i)
            exit(0)

print(0)