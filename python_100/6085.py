w,h,b = input().split()


num = int(w) * int(h) * int(b) / 8 /1024 /1024

f = round(num,2)

print('%.2f'%f,"MB")