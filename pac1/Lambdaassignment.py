#Q1:
sol=lambda a,b,c,x:(a*(x*x)+b*x+c)
print(sol(1,2,3,4))



#Q2:
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
l1=['A','r','k','a']
def cn(li1):
    return li1.count("a")
print(cn(l1))
for i in lst1:
    print('Occurance of A in string %s is'%(i),cn(i)) #placeholder, use %s