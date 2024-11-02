def Greatest(arr):
    for row in arr:
        row.sort()
    return sum(max(col) for col in zip(*arr))
arr=[[1,2,4],[3,3,1]]
print(Greatest(arr))




def deletegreatestvalue(grid):
    length=len(grid)
    result=0
    while True:
        if len(grid[0])==0:
            break
        current_max=[]
        for row in range(length):
            max_ele=max(grid[row])
            grid[row].remove(max_ele)
            current_max.append(max_ele)
        result=result+max(current_max)
    return result
grid=[[1,2,4],[3,3,1]]
print(deletegreatestvalue(grid))



