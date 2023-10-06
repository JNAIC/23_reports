z = 2
m = 1
x = 0
for i in range(20):
    x += z/m
    a = m
    m = z
    z = z+a
print(x)
