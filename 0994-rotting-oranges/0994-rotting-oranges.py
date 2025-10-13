from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        queue = deque()
        max_time = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i, j, 0])
        
        def is_valid_cell(x, y):
            return x >= 0 and y >= 0 and x < n and y < m
        
        while queue:
            x, y, z = queue.popleft()
            max_time = max(max_time, z)
            if is_valid_cell(x+1, y) and grid[x+1][y] == 1:
                grid[x+1][y] = 2
                queue.append([x+1, y, z+1])

            if is_valid_cell(x-1, y) and grid[x-1][y] == 1:
                grid[x-1][y] = 2
                queue.append([x-1, y, z+1])

            if is_valid_cell(x, y+1) and grid[x][y+1] == 1:
                grid[x][y+1] = 2
                queue.append([x, y+1, z+1])

            if is_valid_cell(x, y-1) and grid[x][y-1] == 1:
                grid[x][y-1] = 2
                queue.append([x, y-1, z+1])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return max_time

        