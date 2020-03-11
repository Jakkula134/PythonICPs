A=input()
s=[]
A=A.replace(",","")
for i in A:
  s.append(i)
v=[]
l=len(s)

for i in range(l+1):
  for j in findsubsets(s,i):
    v.append(j)
result=[]
for i in v:
  if i not in result:
    result.append(i)
result.pop(0)
print(result) 