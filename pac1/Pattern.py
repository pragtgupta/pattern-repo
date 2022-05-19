n=5
#top hill(removing last row)
for i in range(n-1):
   #left triangle(decrease space, increase *)
   for j in range(i,n):
      print(' ',end=' ')
   for j in range(i+1):
      print('*',end=' ')
   #right triangle(increasing *)
   for j in range(i):
      print('*',end=' ')
   print()

#bottom hill
for i in range(n):
   #left triangle(increasing space, decreasing *)
   for j in range(i+1):
      print(' ',end=' ')
   for j in range(i,n):
      print('*',end=' ')
   #right side triangle(decreasing *)
   for j in range(i+1,n):
      print('*',end=' ')
   print()