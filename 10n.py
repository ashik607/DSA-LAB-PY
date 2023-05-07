



# define the graph as an adjacency list
graph = {
    'A': [('B', 4), ('H', 8)],
    'B': [('A', 4), ('C', 8), ('H', 11)],
    'C': [('B', 8), ('D', 7), ('F', 4), ('I', 2)],
    'D': [('C', 7), ('E', 9), ('F', 14)],
    'E': [('D', 9), ('F', 10)],
    'F': [('C', 4), ('D', 14), ('E', 10), ('G', 2)],
    'G': [('F', 2), ('H', 1), ('I', 6)],
    'H': [('A', 8), ('B', 11), ('G', 1), ('I', 7)],
    'I': [('C', 2), ('G', 6), ('H', 7)]
}

# define a function to find the parent of a node in the disjoint set
def find_parent(parent, node):
    if parent[node] == node:
        return node
    return find_parent(parent, parent[node])

# define a function to perform the union of two sets in the disjoint set
def union(parent, rank, node1, node2):
    parent1 = find_parent(parent, node1)
    parent2 = find_parent(parent, node2)
    if rank[parent1] < rank[parent2]:
        parent[parent1] = parent2
    elif rank[parent1] > rank[parent2]:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2
        rank[parent2] += 1

# define the function to implement Kruskal's algorithm
def kruskal(graph):
    edges = []
    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((weight, node, neighbor))
    edges.sort() # sort the edges by weight
    parent = {}
    rank = {}
    for node in graph:
        parent[node] = node
        rank[node] = 0
    mst = []
    for edge in edges:
        weight, node1, node2 = edge
        if find_parent(parent, node1) != find_parent(parent, node2):
            union(parent, rank, node1, node2)
            mst.append(edge)
    return mst

# call the kruskal function to find the minimum spanning tree of the given graph
minimum_spanning_tree = kruskal(graph)

# print the minimum spanning tree
print("The minimum spanning tree for the given graph is:")
for edge in minimum_spanning_tree:
    print(edge[1], "-", edge[2], ":", edge[0])
