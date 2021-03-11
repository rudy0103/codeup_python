r,g,b = input().split()


for i in range(int(r)):
    for j in range(int(g)):
        for k in range(int(b)):
            print(i,j,k)

print(int(r)*int(g)*int(b))