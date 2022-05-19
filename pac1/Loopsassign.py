n=5
   #leftTriangle(decreasing space, increasing *)
for i in range(n):
      for j in range(i,n):
         print(' ',end=' ')
      for j in range(i):
         if(j==0):
            print('*',end=' ')
         else:
            print(' ',end=' ')
      for j in range(i+1):
         if(j==i):
            print('*',end=' ')
         else:
            print(' ',end=' ')

      print()
print(('* '*2*n)+'* ')