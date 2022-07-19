class UnionFind:
    # makeset
    def __init__(self, n):
        self.parent = [node for node in range(n)]
     
    # Traces up the parent links until it finds the root node for A
    # returns parent root
    def find(self, A):
        while A != self.parent[A]:
            A = self.parent[A]
        return A  
    
    # returns True if a merge happened, False if otherwise
    def union(self, A, B):
        # find parent nodes
        root_A = self.find(A)
        root_B = self.find(B)
        # if they share a parent node, then we have found a cycle
        if root_A == root_B:
            return False
        # merge the two sets
        self.parent[root_A] = root_B
        return True
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Option 3: Advanced Graph Theory + Union Find
        Begin with n sets, which can slowly be merged as we find connecting edges
        Union Find:
            Represent each set as a directed tree
        The base idea is the same: a graph is a tree if
            1. The graph has n-1 edges AND
            2. All nodes are connected
        """
        if len(edges) != n-1:
            return False
        
        unionFind = UnionFind(n)
        # Add each edge. If a merge did not happen, return False
        for A, B in edges:
            if not unionFind.union(A, B):
                return False
        return True