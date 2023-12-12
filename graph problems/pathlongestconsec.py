def find_longest_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    longest_path = []

    def dfs(i, j, path):
        path.append((i, j))
        nonlocal longest_path
        if len(path) > len(longest_path):
            longest_path = path.copy()
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = i + x, j + y
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0 and (r, c) not in path:
                dfs(r, c, path)
        path.pop()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                dfs(i, j, [])

    return longest_path

grid = [    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1]
]

longest_path = find_longest_path(grid)
print(longest_path)  # should print [(0, 1), (0, 2), (0, 3), (0, 4)]
