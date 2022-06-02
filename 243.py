# (A)
# シミュレート法の方が良い。
V, A, B, C = map(int,input().split())
WHEN_USE = ""
while True:
    if V < A:
        WHEN_USE = "F"
        break
    V -= A
    if V < B:
        WHEN_USE = "M"
        break
    V -= B
    if V < C:
        WHEN_USE = "T"
        break
    V -= C
print(WHEN_USE)

# (B)
N = int(input())
A = list(input().split())
B = list(input().split())
i = 0
j = 0

for _ in range(N):
    if A[_] == B[_]:
        i += 1
    if (A[_] != B[_]) and (A[_] in B):
        j += 1
print(i)
print(j)

# --別解--
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ans1 = sum(a == b for a,b in zip(A,B))
ans2 = len(set(A) & set(B)) - ans1
print(ans1)
print(ans2)
