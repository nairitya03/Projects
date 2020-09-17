n = int (input())
a = []
result = 0
for i in range(0,n):
    a = list(map(int, input().split()))
    result += a[i] - a[- 1 - i]
print(abs(result))

