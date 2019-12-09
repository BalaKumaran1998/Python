l=[9,2,10]
n=len(l)
for i in range(0,n):
  for j in range(0,n):
    if(l[i]< l[j]):
      l[i],l[j]=l[j],l[i]
      print(l)
		

	