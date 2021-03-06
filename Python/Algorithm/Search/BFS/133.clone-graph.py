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
        visited = {node: Node(node.val, [])}
        queue = collections.deque([node])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
'''

'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node, visited):
            if not node:
                return None
            if node in visited:
                return visited[node]
            node_ = Node(node.val, [])
            visited[node] = node_
            for n in node.neighbors:
                node_.neighbors.append(dfs(n, visited))
            return node_
        return dfs(node, {})
'''
