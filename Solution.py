from collections import deque

class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph

    def output_distances(self):
        queue = deque([self.start_node])                     # init queue
        visited = set([self.start_node])                     # init visited set
        distarray = [-1] * (list(self.graph.keys())[-1]+1)   # init distance array with -1 for nodes not visited

        distarray[self.start_node] = 0                       # updated start node distance with 0

        while queue:
            pnode = queue.popleft()                          # pop first element in queue
            graph = self.graph[pnode]
            for node in graph:
                if node not in visited:                      # if cc of node hasn't been visited 
                    queue.append(node)                       # append to queue
                    visited.add(node)                        # add to visited set
                    distarray[node] = (distarray[pnode] + 1) # update distance with parent nodes distance + 1

        return distarray
