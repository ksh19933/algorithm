from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        ## 그래프 생성
        answer =  []
        graph = defaultdict(list)
        for fr, t in tickets:
            graph[fr].append(t)
        
        for fr, t in graph.items():
            graph[fr].sort()
        que = ["JFK"]
        while que:
            if not graph:
                answer.append(que.pop())
            else:
                que.append(graph[que[-1]].pop(0))
        print(answer)
        return answer[::-1]