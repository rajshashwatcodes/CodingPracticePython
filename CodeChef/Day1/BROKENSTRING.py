for i in range(int(input())):
    n = int(input())
    s = input()
    if n % 2 == 1:
        print("NO")
    else:
        s1 = s[0:(n//2)]
        s2 = s[(n//2):n]
        if s == s2+s1 and s == s1+s2:
            
            print("YES")
        else:
            print("NO")
