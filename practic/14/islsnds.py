from collections import deque

def num_islands(grid):
    if not grid:
        return 0

    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    islands = 0

    def bfs(i, j):
        q = deque()
        q.append((i, j))
        visited[i][j] = True

        while q:
            x, y = q.popleft()
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny]==1:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                islands += 1

    return islands

grid = [
    [1,1,0,0,0],
    [1,1,0,1,1],
    [0,0,0,1,1],
    [0,0,0,0,0],
    [1,0,1,0,1]
]

print(num_islands(grid))