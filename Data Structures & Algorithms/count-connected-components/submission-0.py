class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        numComp = 0
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                numComp += 1
        return numComp
        