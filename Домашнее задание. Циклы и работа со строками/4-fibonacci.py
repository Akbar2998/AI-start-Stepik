a = int(input())
x = 0
y = 1
fibbonaci = 1
for i in range(a-1):
    fibbonaci  = x + y
    x = y
    y = fibbonaci
print((fibbonaci)%1000000007)
