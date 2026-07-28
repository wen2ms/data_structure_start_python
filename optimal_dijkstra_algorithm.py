import heapq


def dijkstra(adjacency: list[list[tuple[int, int]]], source: int) -> tuple[list[float], list[int]]:
    vertex_count: int = len(adjacency)
    distances = [float("inf")] * vertex_count
    minimum_distances = [(0, source)]
    prev_nodes = [-1] * vertex_count
    distances[source] = 0
    while minimum_distances:
        minimum_distance, minimum_node = heapq.heappop(minimum_distances)
        if distances[minimum_node] < minimum_distance:
            continue
        for neighbor, weight in adjacency[minimum_node]:
            if minimum_distance + weight < distances[neighbor]:
                distances[neighbor] = minimum_distance + weight
                prev_nodes[neighbor] = minimum_node
                heapq.heappush(minimum_distances, (minimum_distance + weight, minimum_node))
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
    vertex_count, edges_count = map(int, input().split())
    adjacency: list[list[tuple[int, int]]] = [[] for _ in range(vertex_count)]
    for _ in range(edges_count):
        start, end, value = map(int, input().split())
        adjacency[start].append((end, value))
    source = int(input())
    minimum_distances, prev_nodes = dijkstra(adjacency, source)
    for i in range(vertex_count):
        path = make_path(prev_nodes, i)
        print(path)
