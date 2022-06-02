# A
def Tshirt():
    A, B, C, X = map(int, input().split())
    if X <= A:
        return 1
    if A < X <= B:
        return C / (B - A)
    return 0
print(Tshirt())
# B
S = list(input())
print(('').join(sorted(S)))
