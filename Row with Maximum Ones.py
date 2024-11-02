def Row(mat):
    ans=[0,0]
    for i, row in enumerate(mat):
        one=row.count(1)
        if one>ans[1]:
            ans[0]=i
            ans[1]=one
    return ans
mat = [[0,0,0],[0,1,1]]
print(Row(mat))
