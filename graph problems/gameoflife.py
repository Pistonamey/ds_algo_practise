from typing import List

def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows=len(board)
        cols=len(board[0])
        new_board=[[0]*cols for i in range(rows) ]
        for i in range(rows):
            for j in range(cols):
                new_board[i][j]=board[i][j]
        def bfs(i,j):
            if 0>i>=rows and 0>j>=cols:
                return
            
            cur_cnt=0
            dirs=((0,1),(1,0),(0,-1),(-1,0),(-1,1),(-1,-1),(1,1),(1,-1))
            for dr,dc in dirs:
                cur_r=i+dr
                cur_c=j+dc
                if(0<=cur_r<rows and 0<=cur_c<cols):
                   
                    if(board[cur_r][cur_c]==1):
                        cur_cnt+=1
           
            if(board[i][j]==1):
                if(cur_cnt<2):
                    new_board[i][j]=0
                elif(cur_cnt==2 or cur_cnt==3):
                    
                    new_board[i][j]=1
                else:
                    new_board[i][j]=0
            else:
                if(cur_cnt==3):
                    new_board[i][j]=1
            
            return
        
        for row in range(rows):
            for col in range(cols):
                bfs(row,col)
        for i in range(rows):
            for j in range(cols):
                board[i][j]=new_board[i][j]

gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])