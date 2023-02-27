# n = int(inpuy())
# a = [int(x) for x in input().split()]

def find(n,a):
    maxCount=0
    newcount=1
    for i in range(n-1):
        if a[i+1]>a[i]:
            newcount+=1
        else:
            maxCount=max(maxCount,newcount)
            newcount=1
    return max(maxCount,newcount)

if __name__ == "__main__":
    print(find(5,[1,2,3,4,5]))