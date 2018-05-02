# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.)
#
# You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
#
#
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]
#
# Given the above grid, return 0.
#

# Note: The length of each dimension in the given grid does not exceed 50.


from typing import List


class Solution:
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        max_area = 0

        m = len(grid)
        n = len(grid[0])

        stack = set()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_area = 0
                    stack.add((i, j))

                    while stack:
                        pos_i, pos_j = stack.pop()

                        grid[pos_i][pos_j] = 0
                        cur_area += 1

                        for d in directions:
                            adj_i, adj_j = pos_i + d[0], pos_j + d[1]
                            if 0 <= adj_i < m and 0 <= adj_j < n and grid[adj_i][adj_j] == 1:
                                stack.add((adj_i, adj_j))

                    max_area = max(max_area, cur_area)

        return max_area
