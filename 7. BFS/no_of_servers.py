from typing import List

def countServers(self, grid: List[List[int]]) -> int:
        total_count=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        visited=set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    for dr,dc in directions:
                        cur_count=0
                        cur_i=i+dr
                        cur_j=j+dc
                        while(0<=cur_i<len(grid) and 0<=cur_j<len(grid[0]) and (cur_i,cur_j) not in visited):
                            if(grid[cur_i][cur_j]==1):
                                cur_count+=1
                                visited.add((cur_i,cur_j))
                            cur_i=cur_i+dr
                            cur_j=cur_j+dc
                        if(cur_count>0):
                            if (i,j) not in visited:
                                # print("if ",visited)
                                # print(dr,dc,i,j)
                                visited.add((i,j))
                                total_count+=cur_count+1
                            else:
                                # print("else ",visited)
                                # print(dr,dc,i,j)
                                total_count+=cur_count
        
        return total_count

print(countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))