"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""


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
