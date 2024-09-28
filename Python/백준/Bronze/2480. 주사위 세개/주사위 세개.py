a,b,c = map(int, input().split())
r=0
if a==b and b==c:
    r= 10000+a*1000
elif a==b or b==c or a==c:
    s = a if a==b or a==c else b
    r = 1000+s*100
else:
    r=max(a,b,c)*100
print(r)