def solves(N,S):
    stack = []
    pairs_count = 0
    nested_count = 0

    for char in S:
        if char == '(':
            if nested_count == 0:
                stack.append(char)
            nested_count = 1
        elif char == ')':
            nested_count = 0
            if len(stack) > 0 and nested_count == 0:
                stack.pop()
                pairs_count += 1

    return pairs_count
# Example usage
T = int(input())
for i in range(T):
    N = int(input())
    S = input()
    OUT = solves(N,) 
    print(OUT)
