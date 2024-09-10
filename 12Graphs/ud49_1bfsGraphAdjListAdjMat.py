"""
Udemy
Question : Breadth First Traversal/Search

Given an undirected graph stored
 1. As an adjacency list
 2. As an adjacency Matrix
While traversing the graph, store the vertices in an array and return the array
"""




def graphBFS(graph,start):
    bfs = []  # list to save the traversal order
    visited = {}  # to keep track of visited nodes
    queue = [start] # queue to process nodes
    visited[start] = True
    while queue:
        curr = queue.pop(0)
        bfs.append(curr)
        neighbours = graph[curr]
        for nb in neighbours:
            if nb not in visited:
                queue.append(nb)
                visited[nb] = True
    return bfs


'''
Breadth-first search (BFS) has a time complexity of O(V + E), where V is the number of vertices (or nodes) and E is the number of edges in the graph. This is because each node and each edge will be explored once.
The space complexity is O(V) because in the worst-case scenario, all the vertices/nodes might end up in the queue at the same time.
'''


def travBFS(graph,start):
    visited = {}
    bfs = []
    queue = [start]
    visited[start] = True
    while queue:
        curr = queue.pop(0)
        bfs.append(curr)
        currInd = vertex_indices[curr]
        neighbours = graph[currInd]
        for i in range(len(neighbours)):
            if neighbours[i] == 1 and vertices[i] not in visited:
                queue.append(vertices[i])
                visited[vertices[i]] = True
    return bfs


'''
Time Complexity:

Breadth-first search (BFS) has a time complexity of O(V^2) when it is implemented with an adjacency matrix, where V is the number of vertices (or nodes) in the graph. This is because we need to traverse the entire row for each vertex to check for its neighbours in the adjacency matrix. As there are V vertices and each row has V elements, this results in O(V^2) time complexity.

Space Complexity:

The space complexity is O(V) because in the worst-case scenario, all the vertices/nodes might end up in the queue at the same time.
'''


adjacency_list = {
    'A':['B','F'],
    'B':['A','F','C'],
    'C':['B','E','D'],
    'D':['C','E'],
    'E':['D','C','F'],
    'F':['A','B','E']
}

bfs = graphBFS(adjacency_list,'A')
print(bfs)


vertices = ['A','B','C','D','E','F']
vertex_indices = {
    'A':0,'B':1,'C':2,'D':3,'E':4,'F':5
}
adjacency_matrix = [
    [0,1,0,0,0,1],
    [1,0,1,0,0,1],
    [0,1,0,1,1,0],
    [0,0,1,0,1,0],
    [0,0,1,1,0,1],
    [1,1,0,0,1,0]
]


bfs = travBFS(adjacency_matrix,'A')
print(bfs)