import math
def solution(progresses, speeds):
    answer = []
    tmp = 0
    for i in range(len(progresses)):
        progresses[i] = math.ceil((100 - progresses[i]) / speeds[i])
        if not answer or progresses[i] > tmp:
            answer.append(1)
            tmp = progresses[i]
        else:
            answer[-1] += 1
    return answer

print(solution([96,94],[3,3]))