from queue import Queue

def bfs(graph, start):
    q = Queue()
    q.put(start)
    visited = {node: False for node in graph}
    visited[start] = True
    traversal_path = []  
    
    while not q.empty():
        node = q.get()
        traversal_path.append(node)  
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.put(neighbor)
    
    # Print the  path
    print(f" path: {traversal_path}")

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}
bfs(graph, 0)
