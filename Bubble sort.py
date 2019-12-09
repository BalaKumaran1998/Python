l=[9,2,10]
nm=len(l)
for i in range(0,nm):
  for j in range(0,nm):
    if(l[i]< l[j]):
      l[i],l[j]=l[j],l[i]
      print(l)
		

	
