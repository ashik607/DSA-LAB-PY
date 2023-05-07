


# def shortest_path_multistage(graph, stages):
#     n = len(graph)
#     dp = [float('inf')] * n  # initialize all distances to infinity
#     dp[n - 1] = 0  # set the destination node distance to 0

#     # Iterate through all stages in reverse order
#     for i in range(len(stages) - 2, -1, -1):
#         for j in range(n):
#             if j in stages[i]:  # only process nodes in the current stage
#                 dp[j] = min([graph[j][k] + dp[k] for k in range(n) if graph[j][k] != float('inf')])

#     return dp[0]  # return the distance to the source node

# # example graph represented as an adjacency matrix
# graph = [
#     [float('inf'), 1, 2, float('inf'), float('inf'), float('inf')],
#     [float('inf'), float('inf'), float('inf'), 5, 2, float('inf')],
#     [float('inf'), float('inf'), float('inf'), 2, 3, float('inf')],
#     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 2],
#     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 4],
#     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
# ]

# # stages of the multistage graph
# stages = [
#     [0],
#     [1, 2],
#     [3, 4],
#     [5]
# ]

# shortest_path = shortest_path_multistage(graph, stages)

# print("The shortest path in the directed weighted multistage graph is:", shortest_path)


# import math

# def shortest_path_multistage(graph, stages):
#     n = len(graph)
#     dp = [math.inf] * n  # initialize all distances to infinity
#     dp[n - 1] = 0  # set the destination node distance to 0

#     # Iterate through all stages in reverse order
#     for i in range(len(stages) - 2, -1, -1):
#         for j in range(n):
#             if j in stages[i]:  # only process nodes in the current stage
#                 dp[j] = min([edge[1] + dp[edge[0]] for edge in graph[j]])

#     return dp[0]  # return the distance to the source node

# # example graph represented as an adjacency list
# graph = {
#     1: [(2, 3), (3, 1)],
#     2: [(4, 3), (5, 2)],
#     3: [(4, 1), (5, 5)],
#     4: [(6, 2)],
#     5: [(6, 4)],
#     6: []
# }
# stages = [[1], [2, 3], [4, 5], [6]]

# shortest_path = shortest_path_multistage(graph, stages)

# print("The shortest path in the directed weighted multistage graph is:", shortest_path)



# def shortest_path_multistage(graph, stages):
#     n = len(graph)
#     dp = [float('inf')] * n  # initialize all distances to infinity
#     dp[n - 1] = 0  # set the destination node distance to 0

#     # Iterate through all stages in reverse order
#     for i in range(len(stages) - 2, -1, -1):
#         for j in range(n):
#             if j in stages[i]:  # only process nodes in the current stage
#                 dp[j] = min([edge[1] + dp[edge[0]] for edge in graph[j]])

#     return dp[0]  # return the distance to the source node


# # example graph represented as a dictionary of lists
# graph = {
#     0: [(1, 3), (2, 1)],
#     1: [(3, 5), (4, 2)],
#     2: [(3, 1), (4, 3)],
#     3: [(5, 2)],
#     4: [(5, 4)],
#     5: []
# }

# # stages of the multistage graph
# stages = [
#     [0],
#     [1, 2],
#     [3, 4],
#     [5]
# ]

# shortest_path = shortest_path_multistage(graph, stages)

# print("The shortest path in the directed weighted multistage graph is:", shortest_path)


from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, u, v, w):
        # Add an edge to the graph with weight w
        self.edges[u].append(v)
        self.weights[(u, v)] = w

def shortest_path(graph, source, destination):
    # Initialize the distance and parent arrays
    distance = [float("inf")] * graph.vertices
    distance[source] = 0
    parent = [-1] * graph.vertices

    # Perform dynamic programming to find shortest paths
    for i in range(source, graph.vertices):
        for j in graph.edges[i]:
            if distance[j] > distance[i] + graph.weights[(i, j)]:
                distance[j] = distance[i] + graph.weights[(i, j)]
                parent[j] = i

    # Build the shortest path by traversing the parent array
    path = []
    node = destination
    while node != source:
        path.append(node)
        node = parent[node]
    path.append(source)
    path.reverse()

    # Return the shortest path and shortest distance
    return path, distance[destination]

# Example usage
g = Graph(8)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 3)
g.add_edge(1, 4, 2)
g.add_edge(2, 3, 1)
g.add_edge(2, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(4, 5, 2)
g.add_edge(5, 6, 1)
g.add_edge(6, 7, 1)

# Find the shortest path from node 0 to node 7 and print the results
path, distance = shortest_path(g, 0, 7)
print("Shortest path:", path)
print("Shortest distance from source to destination:", distance)