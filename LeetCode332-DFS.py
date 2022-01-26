from collections import defaultdict
class Solution:
    answer = []
    flag = False
    def dfs(self, fr, depth, arr, len_tickets, graph, visited):
        if depth == len_tickets:
            self.answer.append(arr)
            self.flag = True
            return
        for i in range(len(graph[fr])):
            if visited[fr][i] == 0:
                visited[fr][i] = 1
                self.dfs(graph[fr][i], depth+1, arr+[graph[fr][i]], len_tickets, graph, visited)
                visited[fr][i] = 0
            if self.flag:
                break
        return 0
    
    def findItinerary(self, tickets):
        ## 그래프 생성
        graph = defaultdict(list)
        visited = defaultdict(list)
        for fr, t in tickets:
            graph[fr].append(t)
            visited[fr].append(0)
        
        for fr, t in graph.items():
            graph[fr].sort()
        
        self.dfs("JFK" , 0, ["JFK"], len(tickets), graph, visited)
        print(self.answer)
        return self.answer

##================== 훨씬 빠르고 좋은 방법 =================##
# import collections
# answer = []
# graph = collections.defaultdict(list)

# def dfs(s):
#     while graph[s]:
#         dfs(graph[s].pop(0))

#     if not graph[s]:
#         answer.append(s)
#         return

# def solution(tickets):
    
#     for a,b in tickets:
#         graph[a].append(b)
#     for a, b in graph.items():
#         graph[a].sort()
        
#     dfs("ICN")

#     return answer[::-1]
##================== 훨씬 빠르고 좋은 방법 =================##