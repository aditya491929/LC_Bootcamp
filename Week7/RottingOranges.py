from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows = len(grid)
        cols = len(grid[0])

        fresh_oranges = 0
        rotten = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    rotten.append((i, j))

        minutes = 0

        while rotten and fresh_oranges:
            minutes += 1

            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_i, new_j = i + dx, j + dy
                    if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == 1:
                        fresh_oranges -= 1
                        grid[new_i][new_j] = 2
                        rotten.append((new_i, new_j))

        return minutes if fresh_oranges == 0 else -1
