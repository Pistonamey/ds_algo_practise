# Write a function to find the shortest distance between two points consisting of only 0's in a 2D grid of 1 and 0.

def shortest_distance(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = [(start[0], start[1], 1)]
    while queue:
        row, col, distance = queue.pop(0)
        if (row, col) == end:
            return distance
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for drow, dcol in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + drow, col + dcol
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, distance + 1))
    return -1


# Example test case
grid = [[0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]]
start = (0, 0)
end = (0, 4)
print(shortest_distance(grid, start, end))
