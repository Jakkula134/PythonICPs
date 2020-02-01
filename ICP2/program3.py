f= open("testing","r")
d={}
for line in f:
    line=line.strip()
    line=line.lower()
    word=line.split(" ")
    for w in word:
      if w not in d:
         d[w] =1
      else:
          d[w]=d[w]+1

for key in list(d.keys()) :
    print(key,":",d[key])

