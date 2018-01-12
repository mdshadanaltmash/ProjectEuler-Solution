num=2
c=[]
while num>1:
    for i in range(2,num):
            
        if len(c)==10003:
           break
        num+=1
        if (num%i) == 0:
               #print(num,"is not a prime number")
               #print(i,"times",num//i,"is",num)
                break
    else:
            
           #print(num,"is a prime number")
            c.append(num)
#else:
   #print(num,"is not a prime number")
   
print(c)
