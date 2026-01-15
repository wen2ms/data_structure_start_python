def dijskstra(source, graph):
    vertex_count = len(graph)
    distances = [float("inf")] * vertex_count
    checked = [False] * vertex_count
    prev_nodes = [-1] * vertex_count
    distances[source] = 0
    for _ in range(vertex_count):
        minimum_distance = float("inf")
        minimum_node = -1
        for i in range(vertex_count):
            if distances[i] < minimum_distance and not checked[i]:
                minimum_distance = distances[i]
                minimum_node = i
        if minimum_node == -1:
            break
        if checked[minimum_node]:
            continue
        checked[minimum_node] = True
        for i in range(vertex_count):
            if graph[minimum_node][i] > 0 and minimum_distance + graph[minimum_node][i] < distances[i]:
                distances[i] = minimum_distance + graph[minimum_node][i]
                prev_nodes[i] = minimum_node
    return distances, prev_nodes


def generate_path(prev_nodes, destination):
    curr = destination
    path = []
    while curr != -1:
        path.append(curr)
        curr = prev_nodes[curr]
    path.reverse()
    return path


if __name__ == "__main__":
    vertex_count, edge_count = map(int, input().split())
    graph = [[0] * vertex_count for _ in range(vertex_count)]
    for _ in range(edge_count):
        start, end, value = map(int, input().split())
        graph[start][end] = value
    source = int(input())
    distances = dijskstra(source, graph)
    print(distances)
