"""
Udemy
Question 2:Course Scheduler / Topological sort

You have to take a total of n courses leabled from 0 to n-1. Before you can take some courses you need to take it’s prerequisite courses. You are given an array prerequisites where each element [x,y] indicates that to take course x you have to take y first. E.g. [2,3] indicates that to take course 2 one has to first take course 3. Write a function that takes in n and the prerequisite array and returns true if you can complete all courses, else return false.

"""

def buildAdjList(n, prereqs):
    adjList = [[] for _ in range(n)]
    for prereq in prereqs:
        # [1,2] --> 2 should be done first; 2->1
        toTake, firstTake = prereq[0], prereq[1]
        adjList[firstTake].append(toTake)
    return adjList


def checkCycleBFS(vertex, graph):
    queue = [] #Using array just for time and linkedlist is the optimised approach
    visited = {}
    neighbours = graph[vertex]
    for neighbour in neighbours:
        queue.append(neighbour)
    while queue:
        curr = queue.pop()
        visited[curr] = True
        if curr == vertex:
            return True
        neighbours = graph[curr]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
    return False


def checkFinish(n, prereqs):
    adjList = buildAdjList(n, prereqs)
    print(adjList)
    for v in range(n):
        hasCycle = checkCycleBFS(v, adjList)
        if hasCycle:
            return False
    return True


'''
Time Complexity Explanation:
BuildAdjList: O(n + p) where p is the number of prerequisites.
checkCycleBFS: O(E + n) (where n is the number of vertices and E is the number of edges)
CheckFinish: O(n+p + n*(E+n)) = O(p + n^2 + nE)

Space Complexity Explanation:
BuildAdjList: O(n + p), as it needs to store 'p' prerequisites
checkCycleBFS: O(n), as queue and visited dictionary can hold at max 'n' vertices.
CheckFinish: O(n + E), as we need space for the adjacency list (for storing the prerequisite pairs) and for storing 'n' vertices.
'''

# TOPOLOGICAL SORT METHOD

def topoHelper(n, prereqs):
    adjList = [[] for _ in range(n)]
    inDegree = [0 for _ in range(n)]
    for prereq in prereqs:
        [toTake,firstTake] = prereq
        adjList[firstTake].append(toTake)
        inDegree[toTake] += 1
    return [adjList, inDegree]


def checkIfCanFinish(n, prereqs):
    stack = []
    [adjList, inDegree] = topoHelper(n, prereqs)
    print(adjList, inDegree)
    for i in range(n):
        if inDegree[i] == 0:
            stack.append(i)
    count = 0
    while stack:
        curr = stack.pop()
        count += 1
        neighbours = adjList[curr]
        for neighbour in neighbours:
            inDegree[neighbour] -= 1
            if inDegree[neighbour] == 0:
                stack.append(neighbour)
        print(inDegree)
    return count == n
        
'''
Time Complexity
topoHelper: O(n + p), as we are iterating over n vertices and p prerequisites
CheckIfCanFinish: O(n + E) where E is the total number of edges in the graph
Final time complexity of checkIfCanFinish: O(p + n + E) 
This includes building of adjacency list, degree list and traversing the graph

Space Complexity
topoHelper: O(n + E), as the adjacency list can hold up to E edges and n vertices
Space complexity: O(n), as the maximum possible size of stack is n
Final space complexity of checkIfCanFinish: O(n + E), 
This includes space for adjacency list, in-degree list and the stack.
'''


# INPUT
n1 = 2
prereqs1 = [[0,1], [1,0]]
n2 = 5
prereqs2 = [[1,0], [1,3], [2,0], [3,2], [4,2]]
n3 = 8
prereqs3 = prereqs2+ [[5,6], [7,5], [6,7]]
print(checkFinish(n3, prereqs3))
print(checkIfCanFinish(n3, prereqs3))