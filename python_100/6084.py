h, b, c, s = input().split()


num = int(h) * int(b) * int(c) * int(s) / 8 /1024 /1024

f = round(num,1)

if f < num:
    f+=0.1
print(f,"MB")