
import heapq

def minecraft_water_flow(grid, coords):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    priority_queue = [(0, coords[0], coords[1])]  # (time, x, y)
    visited = set()
    flow_out = []

    while priority_queue:
        time, x, y = heapq.heappop(priority_queue)
        
        # If water flows out of the grid
        if x < 0 or x >= rows or y < 0 or y >= cols:
            flow_out.append([[x, y], time / 4])
            continue

        # If already visited, skip
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Calculate flow weights and propagate
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                # Weight is the height difference (or 1 if flat)
                weight = max(1, abs(grid[x][y] - grid[nx][ny]))
                heapq.heappush(priority_queue, (time + weight, nx, ny))

    return flow_out if flow_out else -1


# Test Case 2
grid2 = [
    [3, 4, 6, 4],
    [5, 7, 1, 6],
    [8, 9, 1, 2]
]
coords2 = [1, 1]
print(minecraft_water_flow(grid2, coords2))
