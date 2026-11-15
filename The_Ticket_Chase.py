n,p=[int(x)for x in input().split()]
def f(x):
 if x<2:return 0
 for i in range(2,int(x**0.5)+1):
  if x%i==0:return 0
 return 1
r=-1
for k in range(1,n):
 if f(p+k):
  r=k-1
  break
print(r)
