def Modifymatrix(mat):
    r=len(mat)
    c=len(mat[0])
    ans = mat.copy()
    for j in range(c):
        mx=max(mat[i][j] for i in range(r))
        for i in range(r):
            if mat[i][j]==-1:
                ans[i][j]=mx
    return ans
mat=[[1,2,-1],[4,-1,6],[7,8,9]]
print(Modifymatrix(mat))



            

