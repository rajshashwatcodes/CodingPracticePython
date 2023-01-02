if __name__ == '__main__':
    N = int(input())
    t = []
    for i in range(N):
        X = input().split()
        #print(X)
        if X[0] == 'insert':
            #print(X[1],X[2])
            t.insert(int(X[1]),int(X[2]))
        elif X[0] == 'print':
            print(t)
        elif X[0] == 'remove':
            t.remove(int(X[1]))
        elif X[0] == 'append':
            t.append(int(X[1]))
        elif X[0] == 'sort':
            t.sort()
        elif X[0] == 'pop':
            t.pop()
        else:
            t.reverse()
