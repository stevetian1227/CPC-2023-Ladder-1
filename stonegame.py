def stonegame(n,a):
    indexOfMax=-1
    indexOfMin=-1
    maxNum=-1
    minNum=100000
    for i in range(n):
        if a[i]>maxNum:
            maxNum=a[i]
            indexOfMax=i
        if a[i]<minNum:
            minNum=a[i]
            indexOfMin=i
    return(min(max(indexOfMax,indexOfMin)+1,max(n-indexOfMax,n-indexOfMin),indexOfMax+n-indexOfMin+1,indexOfMin+n-indexOfMax+1))

if __name__=='__main__':
    print(stonegame(8,[4,2,3,1,8,6,7,5]))


tests = int(input())

for i in range(tests):
    n = int(input())
    a = [int(x) for x in input().split()]

    indexOfMax = a.index(max(a))
    indexOfMin = a.index(min(a))

    print((min(max(indexOfMax,indexOfMin)+1,max(n-indexOfMax,n-indexOfMin),indexOfMax+n-indexOfMin+1,indexOfMin+n-indexOfMax+1)))