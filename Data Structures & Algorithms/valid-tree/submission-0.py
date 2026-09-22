class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = set()
        adj = [[] for _ in range(n)]
        if len(edges) != n - 1:
            return False

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)


        def dfs(node, parent):

            if node in visited:
                return False

            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False

            return True

        if not dfs(0, -1):
            return False
        
        return len(visited) == n

        

