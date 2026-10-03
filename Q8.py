def dfs(graph, start):
    visited = set()

    def explore(node):
        if node in visited:
            return

        visited.add(node)

        for neighbour in graph[node]:
            explore(neighbour)

    explore(start)

    return visited


graph = {
    'A': {'B', 'C'},
    'B': {'D'},
    'C': {'D'},
    'D': {'E'},
    'E': set()
}

print(dfs(graph, 'A'))