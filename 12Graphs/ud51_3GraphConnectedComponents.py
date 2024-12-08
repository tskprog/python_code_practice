"""
Udemy
Question: Number of connected components

You are given a graph with n vertices. To indicate the connections in the graph you are given an array edges whose each element is an array of the form [u,v]. [u,v] indicates that there is an edge between u and v where u and v denote two vertices or nodes. Write a function that takes in ‘n’ and the ‘edges’ array and returns the number of connected components in the graph.

"""

def buildAdjList(n, edges):
    adjList = [[] for _ in range(n)]
    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]
        adjList[node1].append(node2)
        adjList[node2].append(node1)
    return adjList


def dfs(graph, vertex, visited):
    visited[vertex] = True
    neighbours = graph[vertex]
    for neighbour in neighbours:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)



def countComponents(n, edges):
    graph = buildAdjList(n, edges)
    print(graph)
    visited = {}
    components = 0
    for v in range(n):
        if v not in visited:
            components += 1
            dfs(graph, v, visited)
    return components

'''
Time complexity explanation:

The time complexity is O(V+E), where V is the number of vertices and E is the number of edges.
Creating the adjacency list will take O(E) time as we're iterating over all edges.
DFS itself also has a time complexity of O(V+E) because we're visiting every vertex once and checking all their neighbours (which corresponds to the edges).

Space complexity explanation:

The space complexity is O(V+E).
The adjacency list will take O(V+E) space. This is because we have a separate list for each vertex, and the total length of all lists is twice the number of edges (since each edge contributes to 2 vertices).
The visited dictionary will take O(V) space as it could potentially store all vertices.
There is also additional O(V) space required for the call stack in the case of a DFS on a connected graph. So, overall, the space complexity is O(V+E).
'''

# print(buildAdjList(5,[[1,2],[3,4]]))

edges1 = [[0,1],[1,2]]
edges2 = edges1 + [[3,4]]
edges3 = edges2 + [[5,6]]
print(countComponents(7, edges3))

'''
Time complexity explanation:
Depth-first search (DFS) has a time complexity of O(V + E) where V is the number of vertices and E is the number of edges.
This is because in the worst-case scenario, we need to visit every vertex and traverse through its neighbors which corresponds to the edges.

Space complexity explanation:
The space complexity of DFS is O(V) where V is the number of vertices.
In the worst-case scenario, you end up going down one single path the length of the graph, so you end up with a call stack the size of V, where V is the vertices.
'''