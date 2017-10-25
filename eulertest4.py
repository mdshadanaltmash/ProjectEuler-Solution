"""a=int(input("enter a number "))
rev=0
n=[]
temp=a
while (a>0):
    d=a%10
    rev=(rev*10)+d
    a=a//10
    
if temp==rev:
    n.append(rev)
print (n)"""


def palin(n):
    temp=n
    rev=0
    while (n>0):
        d=n%10
        rev=(rev*10)+d
    if rev==temp:
        c.append(rev)
    n=n//10
#n=int(input("enter a number"))

c=[]
for i in range(100,1000):
    for j in range(100,1000):
        n=i*j
        palin(n)
#c.sort()
print(c)
print(c[-1])
