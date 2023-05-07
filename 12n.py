
# Write a program to find
# the all pair shortest path from a 
# graph using Floyd Warshall’s Algorithm.


INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[0 if i == j else graph[i][j] if graph[i][j] != 0 else INF for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

# example graph represented as an adjacency matrix
# graph = [
#     [0, 3, INF, 7],
#     [8, 0, 2, INF],
#     [5, INF, 0, 1],
#     [2, INF, INF, 0]
# ]

graph = [
    [0, 5, INF, 9],
    [INF, 0, 3, 4],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

distances = floyd_warshall(graph)

print("The all-pairs shortest path distances are:")
for row in distances:
    print(row)
