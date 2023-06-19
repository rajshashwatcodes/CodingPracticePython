def binaryQueries(n: int, a: List[int], q: int, queries: List[List[int]]) -> List[int]:
    # write your code here
    B = []

    for q in queries:
        L, R, X = q
        Z = 0
        for i in range(L, R + 1):
            a[i] = a[i] ^ X
            Z |= a[i]
        B.append(Z)
    return B
