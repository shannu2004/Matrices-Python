def largestLocal(grid):
    n = len(grid)
    res = []
    for i in range(1,n-1):
        temp_row = []
        for j in range(1,n-1):
            temp = 0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    temp = max(temp,grid[k][l])
            temp_row.append(temp)
        res.append(temp_row)
    return res

grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
print(largestLocal(grid))
