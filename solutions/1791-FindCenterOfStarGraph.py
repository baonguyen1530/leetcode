class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        #if that node has n-1 edges then it must be the center node?
        edge_count = collections.defaultdict(int)
        for (u,v) in edges:
            edge_count[u] += 1
            edge_count[v] += 1
        
        for key,value in edge_count.items():
            if value == len(edges):
                return key