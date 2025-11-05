from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(1, 0), (-1, 0), (0,1), (0, -1)]
        queue = deque([])
        max_time = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        while queue:
            x, y, z = queue.popleft()
            max_time = max(max_time, z)
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0<=nx<n and 0<=ny<m and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny, z+1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return max_time

        