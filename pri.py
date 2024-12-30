def prime(n):
    fc=0
    for i in range(1,n+1):
        if(n%i==0):
            fc+=1
    if(fc==2):
       return True
    else:
       return false
def prime_range(s,e):
    for i in range(s,e+1):
        if(prime(i)==True):
           print(i,end='')
s,e=int(input()),int(input())
primerange(s,e)
