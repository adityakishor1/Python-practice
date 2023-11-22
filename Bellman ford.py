def min_path(G, N, start, end):
    distance = [float('inf') for _ in xrange(N+1)]
    distance[start] = 0

    for _ in xrange(N-1):
        for mid, dis in enumerate(distance):
            if dis==float('inf'): continue
            for dis_to_nei, nei in G[mid]:
                distance[nei] = min(distance[nei], dis+dis_to_nei)
    return distance[end]


G = {
    0: [(-2, 1), (4, 2)],
    1: [(5, 2)],
    2: [(12, 3), (5, 4)],
    3: [(-8, 4)],
    4: []
}
N = 4 #nodes count
start = 0
end = 4
print min_path(G, N, start, end)
