import heapq

class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))
        
        dist = [float('inf')] * n
        dist[0] = 0
        

        pq = [(0, 0)]
        
        
        while pq:
            current_cost, u = heapq.heappop(pq)
            
          
            if current_cost > dist[u]:
                continue
            
           
            if u == n - 1:
                return current_cost
            
            
            for v, weight in adj[u]:
                next_cost = current_cost + weight
                
                if next_cost < dist[v]:
                    dist[v] = next_cost
                    heapq.heappush(pq, (next_cost, v))
                    
   
        return -1 if dist[n-1] == float('inf') else dist[n-1]