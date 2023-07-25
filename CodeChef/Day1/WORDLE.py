for i in range(int(input())):
    S = input()
    T = input()
    for k,j in zip(S,T):
        if k == j:
            print("G",end="")
        else:
            print("B",end="")
    print()
