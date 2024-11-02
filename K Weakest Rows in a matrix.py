def weakest(mat,k):
    d={}
    key=0
    for i in mat:
        d[key]=sum(i)
        key+=1
    return list(sorted(d,key=lambda x:d[x]))[:k]
mat=[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k=3
print(weakest(mat,k))
