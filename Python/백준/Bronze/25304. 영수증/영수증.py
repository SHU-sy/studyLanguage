t=int(input())
c=int(input())
s=0
for i in range(c):
    a,b = map(int,input().split())
    s+=a*b
if t==s:
    print("Yes")
else:
    print("No")