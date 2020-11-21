#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def sieveOfEratosthenes(N):

    #code here 
    ans=[]
    prime=[True for i in range(N+1)]
    p=2
    while p**2<=N:
        if prime[p]:
            for i in range(p**2,N+1,p):
                prime[i]=False
        p+=1
    
    for p in range(2, N+1): 
        if prime[p]: 
            ans.append(p)
    return sum(ans)

n=int(input("Enter the Number upto which you want the sum of all prime numbers: "))
print(sieveOfEratosthenes(n))
