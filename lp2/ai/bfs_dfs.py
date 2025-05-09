def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node):
    queue = []
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph.get(s, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    n = int(input("Enter number of vertices: "))  # Vertices can be from 0 to n-1
    e = int(input("Enter number of edges: "))

    graph = {i: [] for i in range(n)}  # Initialize graph with 0-based indexing

    print(f"Enter {e} edges (u v):")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # For undirected graph

    start = int(input("Enter starting vertex for DFS and BFS: "))

    print("\nDFS traversal:")
    dfs(set(), graph, start)

    print("\n\nBFS traversal:")
    bfs(set(), graph, start)

if __name__ == "__main__":
    main()
















































































































'''
Enter number of vertices: 5
Enter number of edges: 4
Enter 4 edges (u v):
0 1
0 2
1 3
1 4
Enter starting vertex for DFS and BFS: 0




def dfs(visited, graph, node):
    # Recursive Depth-First Search
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph.get(node, []):
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node):
    # Iterative Breadth-First Search using a queue
    queue = []
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph.get(s, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    # Input number of vertices and edges
    n = int(input("Enter number of vertices: "))  # Vertices are 0-indexed (0 to n-1)
    e = int(input("Enter number of edges: "))

    # Initialize an empty adjacency list for each vertex
    graph = {i: [] for i in range(n)}

    # Input edges and build the graph (undirected)
    print(f"Enter {e} edges (u v):")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Ask user to enter starting vertex
    start = int(input("Enter starting vertex for DFS and BFS: "))

    print("\nDFS traversal:")
    dfs(set(), graph, start)

    print("\n\nBFS traversal:")
    bfs(set(), graph, start)

if __name__ == "__main__":
    main()

'''




