def find_nearest_exit(board, start_row, start_col):
    q = []
    q.append((start_row, start_col))

    visited = set()
    while q:

        current_node = q.pop(0)
       
        visited.add(current_node)
      
        if(current_node[0] == 0 or current_node[0] == len(board)-1 or current_node[1] == 0 or current_node[1] == len(board[0])-1) and (current_node != (start_row, start_col)):
            return current_node[0], current_node[1]

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dr, dc in directions:
            new_row = current_node[0]+dr
            new_col = current_node[1]+dc
          
            if(0 <= new_row < len(board)): 
               
                if 0 <= new_col < len(board[0]) :
                
                   if board[new_row][new_col] == '0':
                   
                        if (new_row, new_col) not in visited:
                          
                            q.append((new_row, new_col))
    return -1, -1


# Test case
board = [
    ['0', '0', '0', '+', '+'],
    ['+', '+', '0', '+', '+'],
    ['0', '0', '0', '0', '+'],
    ['+', '+', '+', '0', '+'],
    ['+', '+', '0', '0', '0'],
    ['+', '+', '+', '+', '0']
]

start_row = 2
start_col = 0

exit_row, exit_col = find_nearest_exit(board, start_row, start_col)
print(f"Nearest exit: ({exit_row}, {exit_col})")
