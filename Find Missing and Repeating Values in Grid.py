def Missingrepeating(arr):
    arr=[num for sublist in arr for num in sublist]
    n=len(arr)
    count=[0]*(n+1)
    for num in arr:
        count[num]+=1
    missing=-1
    repeating=-1
    for i in range(1,n+1):
        if count[i]==2:
            repeating=i
        elif count[i]==0:
            missing=i
    return repeating, missing
arr=[[9,1,7],[8,9,2],[3,4,6]]
print(Missingrepeating(arr))

