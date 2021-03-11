
n = int(input())

for i in range(1, n+1):
    s = str(i)
    count = 0
    for c in s:
        if c in ['3','6','9']:
            count +=1
    if count == 0:
        print(s,end="")


    print("X"*count,end="")
    count = 0

    print(' ',end="")