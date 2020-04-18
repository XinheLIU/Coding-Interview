#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node, m):
            if not node:
                return None
            if node.val in m:
                return m[node.val]
            root = Node(node.val, [])
            m[node.val] = root
            for n in node.neighbors:
                root.neighbors.append(dfs(n, m))
            return root
        return dfs(node, {})
# @lc code=end
'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {}
        queue = collections.deque([node])
        visited[node] = Node(node.val, [])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
'''

