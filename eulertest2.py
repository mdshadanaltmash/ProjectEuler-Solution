"""Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

a=0
sum=1
s=0
rt=0
count=0
while a<40000 and count<4000000:
    count=sum+s
    if count%2==0:
       rt=rt+count
    s=sum
    sum=count
    a+=1
print (count)
print (rt)
