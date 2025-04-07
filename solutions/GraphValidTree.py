class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = collections.defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)
            for q in adj[i]:
                if q == prev:
                    continue
                if not dfs(q, i):
                    return False
            return True
        
        return dfs(0,-1) and len(visit) == n