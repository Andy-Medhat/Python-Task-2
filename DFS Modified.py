def dfs(graph, start):
    visited = {node: False for node in graph}
    stack = [start]
    traversal_path = []  # List to collect the order of visited nodes

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            traversal_path.append(current)  # Add to path when visited
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    
    print("DFS traversal path:", traversal_path)

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1],
    4: [1, 2]
}

dfs(graph, 0)

l = [1, 2, 3]
print("the goal is: ", l[-1])
