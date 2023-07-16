def tub(n):
    k=2
    s=0
    while k*k<=n:
        if n%k==0:
            s+=1
        k+=1
    if s==0:
        return True
    else:
        return False
    
n=2
mass=[]
while n<=2000:
    if tub(n):
        mass.append(n):
        n+=1
print(mass)