#Q3:
li3=[1,-2,3,4,-7,-8]
def posit(number):
    if number<0:
        return True
    else:
        return False
newLis1=filter(posit,li3)
l4=[]
for i in newLis1:
    l4.append(abs(i))
print(l4)

#Q4:
#Q5:
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
x=zip(lst1,lst2)
#for i in x:
#print(i)

y=dict(x)
print('Following Dictionary:  ',y)
