"""
Udemy
Question : Depth First Traversal/Search

Given an undirected graph stored as an adjacency list. Traverse with DFS approach
 1. Recursively
 2. Iteratively
While traversing the graph, store the vertices in an array and return the array
"""



# Recursive function for Depth-first search (DFS)
def travDFS(graph,vertex,dfs,visited):
    dfs.append(vertex)  # Append the current vertex to the output
    visited[vertex] = True  # Mark the current vertex as visited
    neighbours = graph[vertex] # Get all neighbors of the current vertex
    for neighbour in neighbours:
        if neighbour not in visited:  # If the neighbor has not been visited yet
            travDFS(graph,neighbour,dfs,visited)  # Recursively perform DFS on the neighbor
    return dfs


'''
Time complexity explanation:
Depth-first search (DFS) has a time complexity of O(V + E) where V is the number of vertices and E is the number of edges.
This is because in the worst-case scenario, we need to visit every vertex and traverse through its neighbors which corresponds to the edges.

Space complexity explanation:
The space complexity of DFS is O(V) where V is the number of vertices.
In the worst-case scenario, you end up going down one single path the length of the graph, so you end up with a call stack the size of V, where V is the vertices.
'''


def travDFSIterative(graph,start):
    # Initialize the visited dictionary, output list and stack
    visited = {}
    dfs = []
    stack = [start]
    visited[start] = True # Mark the start node as visited
    while stack:
        curr = stack.pop()  # Pop a node from the stack- to get child before neighbour
        dfs.append(curr)    # Append the current node to the output
        neighbours = graph[curr]
        for neighbour in neighbours:
            if neighbour not in visited:  # If the neighbour has not been visited yet
                stack.append(neighbour)  # Push the neighbour to the stack
                visited[neighbour] = True
    return dfs

'''
Time complexity explanation:
Depth-first search (DFS) has a time complexity of O(V + E) where V is the number of vertices and E is the number of edges.
This is because in the worst-case scenario, we need to visit every vertex and traverse through its neighbours which corresponds to the edges.

Space complexity explanation:
The space complexity of DFS is O(V) where V is the number of vertices.
The 'output' list, 'visited' dictionary, and 'stack' store V elements in the worst case, contributing to the O(V) space complexity.
'''


adjacency_list = {
    'A':['B','F'],
    'B':['A','C'],
    'C':['B','E','D'],
    'D':['C','E'],
    'E':['D','C','F'],
    'F':['A','E']
}

dfs = travDFS(adjacency_list,'A',[],{})
print(dfs)

dfsi = travDFSIterative(adjacency_list,'A')
print(dfsi)