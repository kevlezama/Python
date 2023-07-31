
a = 1
b = 1
c = 1
n = 2

res = [[x1,y1,z1] for x1 in range(a+1) for y1 in range(b+1) for z1 in range(c+1) if x1+y1+z1 != n]

print(res)