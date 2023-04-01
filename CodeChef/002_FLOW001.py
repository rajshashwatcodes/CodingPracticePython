# FLOW001
# Add two numbers

T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    if X+Y>6:
        print("YES")
    else:
        print("NO")
