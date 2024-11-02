def countNegatives(grid):
    n=len(grid)
    r=0
    c=len(grid[0])-1
    total=0
    while c>=0 and r<n:
        if grid[r][c]<0:
            total+=n-r
            c-=1
        else:
            r+=1
    return total
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))
    
