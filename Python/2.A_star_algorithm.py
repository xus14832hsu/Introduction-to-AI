# 2. A* Algorithm - 簡單網格地圖尋找最短路徑
from heapq import heappop, heappush

def astar(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    def heuristic(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])

    frontier = [(0 + heuristic(start, goal), 0, start, [])]
    visited = set()
    while frontier:
        f, cost, node, path = heappop(frontier)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x, y = node[0]+dx, node[1]+dy
            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0:
                heappush(frontier, (cost+1 + heuristic((x,y), goal), cost+1, (x,y), path))

# 0: path, 1: wall
grid = [[0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]]

print("A* Path:", astar((0,0), (2,2), grid))