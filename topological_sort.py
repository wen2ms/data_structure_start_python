from collections import deque


def topological_sort(adjacent):
    vertex_count = len(adjacent)
    indegrees = [0] * vertex_count
    topo = []
    for i in range(vertex_count):
        for end in adjacent[i]:
            indegrees[end] += 1
    zeros = deque()
    for i in range(vertex_count):
        if indegrees[i] == 0:
            zeros.append(i)
    while zeros:
        index = zeros.popleft()
        topo.append(index)
        for neighbor in adjacent[index]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                zeros.append(neighbor)
    if len(topo) != vertex_count:
        return None
    return topo


if __name__ == "__main__":
    vertex_count = 6
    adjacent = [[] for _ in range(vertex_count)]
    adjacent[5].append(2)
    adjacent[5].append(0)
    adjacent[4].append(0)
    adjacent[4].append(1)
    adjacent[2].append(3)
    adjacent[3].append(1)
    topo = topological_sort(adjacent)
    print(topo)
