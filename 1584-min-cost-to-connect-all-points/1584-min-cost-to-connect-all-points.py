import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def cost(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        adj_lst = [[] for _ in range(n)]
        for i in range(n):
            start = points[i]
            for j in range(i+1, n):
                end = points[j]
                weight = cost(start, end)
                adj_lst[i].append((j, weight))
                adj_lst[j].append((i, weight))
        

        visited = [False for _ in range(n)]
        pri_que = [(0, 0)]
        heapq.heapify(pri_que)
        tot_cost = 0
        while pri_que:
            cost, node = heapq.heappop(pri_que)
            if visited[node]:          
                continue
            visited[node] = True
            tot_cost += cost
            for neigh, weight in adj_lst[node]:
                if not visited[neigh]:
                    heapq.heappush(pri_que, (weight, neigh))
        return tot_cost



        