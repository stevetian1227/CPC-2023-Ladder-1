t=int(input())
for i in range(t):
    n=int(input())
    a = [int(x) for x in input().split()]
    b = [k+1 for k in range(n)]
    if n==1:
        print(-1)
        continue
    for j in range(n-1):
        if a[j]==b[j]:
            b[j],b[j+1]=b[j+1],b[j]
    if a[-1]==b[-1]:
        b[-1],b[-2]=b[-2],b[-1]
    for m in range(n):
        print(b[m],end=" ")
    print("\n",end="")


# n=5
# a=[2,3,4,5,1]
# b=[k+1 for k in range(n)]

# for j in range(n-1):
#     if a[j]==b[j]:
#         b[j],b[j+1]=b[j+1],b[j]
# if a[-1]==b[-1]:
#     b[-1],b[-2]= b[-2],b[-1]
# print(b)

