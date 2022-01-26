import sys
input = sys.stdin.readline

def dfs(depth, sum):
    global max_energy
    if depth == (n-2):
        max_energy = max(max_energy, sum)
        return
    
    for j in range(1, n-1):
        if not used[j]:
            left, right = j-1, j+1
            while used[left]:
                left -= 1
            while used[right]:
                right += 1
            used[j] = True
            dfs(depth+1, sum + bead[left] * bead[right])
            used[j] = False
    return

n = int(input())
bead = list(map(int, input().split()))
max_energy = 0
used = [False] * n
for i in range(1, n-1):
    used[i] = True
    dfs(1, bead[i-1] * bead[i+1])
    used[i] = False

print(max_energy)

## used를 사용하지 않고 arr element를 제거하는 방법도 가능: del bead[i] 활용