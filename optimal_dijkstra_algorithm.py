import heapq


def dijkstra(source, adjacent):
    vertex_count = len(adjacent)
    distances = [float("inf")] * vertex_count
    checked = [False] * vertex_count
    prev_nodes = [-1] * vertex_count

    distances[source] = 0

    minimum_distances = [(0, source)]
    while minimum_distances:
        minimum_distance, minimum_node = heapq.heappop(minimum_distances)
        if checked[minimum_node]:
            continue
        checked[minimum_node] = True
        for neighbor, weight in adjacent[minimum_node]:
            if minimum_distance + weight < distances[neighbor]:
                distances[neighbor] = minimum_distance + weight
                prev_nodes[neighbor] = minimum_node
                heapq.heappush(minimum_distances, (distances[neighbor], neighbor))
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
    adjacent = [[] for _ in range(vertex_count)]

    for _ in range(edge_count):
        start, end, value = map(int, input().split())
        adjacent[start].append((end, value))
    source = int(input())
    distances, prev_nodes = dijkstra(source, adjacent)
    for i in range(vertex_count):
        path = generate_path(prev_nodes, i)
        print(path)
