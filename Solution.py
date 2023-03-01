from collections import deque

class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph

    def output_distances(self):
        queue = deque([self.start_node])
        visited = set([self.start_node])
        distarray = [-1] * (list(self.graph.keys())[-1]+1)

        distarray[self.start_node] = 0

        while queue:
            pnode = queue.popleft()
            graph = self.graph[pnode]
            for node in graph:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)
                    distarray[node] = (distarray[pnode] + 1)

        return distarray
