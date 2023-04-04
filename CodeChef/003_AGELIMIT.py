T=int(input())
for i in range(T):
    X,Y,A=map(int,input().split())
    print("YES") if A>=X and A<Y else print("NO")
