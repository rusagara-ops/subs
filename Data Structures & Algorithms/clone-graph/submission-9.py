"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        oldtonew = {}

        def dfs(node):
            if not node:
                return
            if node in oldtonew:
                return oldtonew[node]

            currentval = node.val
            copy = Node(currentval)
            oldtonew[node] = copy

            for neigh in node.neighbors:
                clonedneighbour = dfs(neigh)
                copy.neighbors.append(clonedneighbour)
                    
            return copy

        return dfs(node)

            

            