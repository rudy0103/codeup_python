a,b,c = input().split()
a,b,c=int(a),int(b),int(c)
m = max([a,b,c])
d = m
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += m
print(d)