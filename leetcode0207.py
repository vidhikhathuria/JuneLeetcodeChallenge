# Problem Link : https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def solve(adj, cost, src, dst, k, fare, totcost, visited):
            # print(src, dst, k, totcost, fare)
            if k < -1:
                return fare
            if src == dst:
                # print(totcost, fare)
                fare = min(fare, totcost)
                return fare
            visited[src] = 1
            for i in range(len(adj[src])):
                if adj[src][i] == 1 and visited[i] == 0 and totcost + cost[src][i] < fare:
                    fare = solve(adj, cost, i, dst, k - 1, fare, totcost + cost[src][i], visited)
            visited[src] = 0
            return fare
        
        adj = [[0 for i in range(n)] for j in range(n)]
        cost = [[float("inf") for i in range(n)] for j in range(n)]
        for flight in flights:
            adj[flight[0]][flight[1]] = 1
            cost[flight[0]][flight[1]] = flight[2]
        
        
        fare = float("inf")
        visited = [0] * n
        
        fare = solve(adj, cost, src, dst, k, fare, 0, visited)
        
        if fare == float("inf"):
            return -1
        return fare
        