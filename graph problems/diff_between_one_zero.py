from typing import List

def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff=[]
        ones_row=[]
        zeros_row=[]
        ones_col=[]
        zeros_col=[]
        
        for i in range(len(grid)):
            ones_row.append(grid[i].count(1))
            zeros_row.append(grid[i].count(0))
        
        for j in range(len(grid[0])):
            cur_one=0
            cur_zero=0
            for i in range(len(grid)):
                if(grid[i][j]==1):
                    cur_one+=1
                else:
                    cur_zero+=1
            ones_col.append(cur_one)
            zeros_col.append(cur_zero)
        
        for i in range(len(grid)):
            cur=[]
            for j in range(len(grid[0])):
                elem=ones_row[i]+ones_col[j]-zeros_row[i]-zeros_col[j]
                cur.append(elem)
            diff.append(cur)

        return diff

print(onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))