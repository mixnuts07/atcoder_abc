#(A)
a, b, c, d = input().split()
Takahashi = a+b
Aoki = c+d+str(1)
print("Takahashi" if Takahashi < Aoki else "Aoki")

#(B)
n = int(input())
An =set(list(map(int,input().split())))
for _ in range(0,n+1):
    if _ not in An:
        print(_)
        break
