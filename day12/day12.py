from collections import defaultdict


def read_input(filename):
    with open(filename) as f:
        graph = defaultdict(set)
        for line in f.readlines():
            v1, v2 = line.strip().split("-")
            graph[v1].add(v2)
            graph[v2].add(v1)

        return graph


def dfs(graph):
    global total_paths
    total_paths = 0
    def run_dfs(graph, node, visited):
        global total_paths
        if node == "end":
            total_paths += 1
        elif node not in visited:
            if not node.isupper():
                visited.add(node)
            for neighbor in graph[node]:
                run_dfs(graph, neighbor, visited.copy())

    run_dfs(graph, "start", set())
    return total_paths


def _has_double(visited):
    return len(visited) != len(set(visited))

def dfs_part_2(graph):
    global total_paths
    total_paths = 0
    def run_dfs(graph, node, visited):
        global total_paths
        if node == "end":
            total_paths += 1
        elif node not in visited:
            if not node.isupper():
                visited.append(node)
            for neighbor in graph[node]:
                run_dfs(graph, neighbor, visited.copy())
        elif not _has_double(visited):
            if node != "start":
                visited.append(node)
                for neighbor in graph[node]:
                    run_dfs(graph, neighbor, visited.copy())

    run_dfs(graph, "start", [])
    return total_paths


graph = read_input('input.txt')
total = dfs(graph)

print(f"Problem 1: {total}")

total = dfs_part_2(graph)

print(f"Problem 2: {total}")
