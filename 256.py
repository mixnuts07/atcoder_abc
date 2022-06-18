# A
# N = int(input())
# print(2 ** N)

# B
N = int(input()) - 1
A = list(map(int,input().split()))
P = 0
x = []
x.append(A[0])
A = A[1:]

for a in A:
    x.append(a-1)
    X = [element + a for element in x]
    # N以上とそれ以外で分ける
    OverN = list(filter(lambda x : x > N, X))
    X = list(filter(lambda x : x <= N, X))
    P += len(OverN)
    OverN = []
print(P)


