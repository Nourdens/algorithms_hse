f = open("text.txt", "r")
x = f.readline().split()
m = x[0]
y = x[1]
xx = f.readline().split()
nn = xx[0]
mm = xx[1]
print(m,"   ",y, "_", nn, "  ", mm)
