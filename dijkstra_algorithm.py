def dijkstra(matrix: list[list[int]], source: int) -> tuple[list[float], list[int]]:
    vertex_count: int = len(matrix)
    distances = [float("inf")] * vertex_count
    prev_nodes = [-1] * vertex_count
    visited = [False] * vertex_count
    distances[source] = 0
    for _ in range(vertex_count):
        minimum_node = -1
        minimum_distance = float("inf")
        for i in range(vertex_count):
            if distances[i] < minimum_distance and not visited[i]:
                minimum_distance = distances[i]
                minimum_node = i
        if minimum_node == -1:
            break
        visited[minimum_node] = True
        for i in range(vertex_count):
            if matrix[minimum_node][i] > 0 and minimum_distance + matrix[minimum_node][i] < distances[i]:
                distances[i] = minimum_distance + matrix[minimum_node][i]
                prev_nodes[i] = minimum_node
    return distances, prev_nodes


def make_path(prev_nodes: list[int], destination: int) -> list[int]:
    curr = destination
    path: list[int] = []
    while curr != -1:
        path.append(curr)
        curr = prev_nodes[curr]
    path.reverse()
    return path


if __name__ == "__main__":
    vertex_count, edge_count = map(int, input().split())
    matrix = [[0] * vertex_count for _ in range(vertex_count)]
    for _ in range(edge_count):
        start, end, value = map(int, input().split())
        matrix[start][end] = value
    source = int(input())
    minimum_distances, prev_nodes = dijkstra(matrix, source)
    print(minimum_distances)
