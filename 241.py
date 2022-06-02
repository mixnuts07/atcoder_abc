# # A
a = list(map(int,input().split()))
k = 0
display_number = a[k]
display_number = a[display_number]
display_number = a[display_number]
print(display_number)
# --別解--
A = list(map(int,input().split()))
print(A[A[A[0]]])
# --別解--
A = list(map(int,input().split()))
ans = 0
for _ in range(3):
    ans = A[ans]
print(ans)

# B
N, M = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
flag = True
for i in range(M):
    if B[i] not in A:
        flag = False
        break
    else:
        A.remove(B[i])

print("Yes" if flag else "No")

# 別解 --
# Counter ...　リスト,タプル,辞書,文字列などの中の要素の数を取得できる！
from collections import Counter
def solve():
    N, M = map(int, input().split())
    A = Counter(list(map(int, input().split())))
    B = Counter(list(map(int, input().split())))
    C = A - B  # 個数が0の要素はCounterから削除される
    return not C  # Cが空ならTrueを返す
print("Yes" if solve() else "No")
