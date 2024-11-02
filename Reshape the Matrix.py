def matrixReshape(mat,r,c):
    flat=[]
    new=[]
    for row in mat:
        for num in row:
            flat.append(num)
    if r*c!=len(flat):
        return mat
    else:
        for i in range(r):
            new.append(flat[i*c : i*c+c])
        return new
mat=[[0,1,2,3],[4,5,6,7],[8,9,10,11]]
r=2
c=6
print(matrixReshape(mat,r,c))
