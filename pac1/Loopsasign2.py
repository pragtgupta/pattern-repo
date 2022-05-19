
n=5
for i in range(n):
   for j in range(i):
      print(' ',end=' ')
   for j in range(i,n):
      if(j==i or i==0 or j==n-1):
           print('*',end=' ')
      else:
         print(' ',end=' ')

   print()