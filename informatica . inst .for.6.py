n=eval(input("dati n="))
s=0
for i in range(0,n,1):
    i=i+1
    s=s+i
print("S1=",s)
n=eval(input("dati n="))
s=0
for i in range(0,n,1):
    b=i*(i+1)
    s=s+b 
print("S2=",s)
n=eval(input("dati n="))
s=0
p=1
for i in range(0,n,1):
    p=p*(i+1)
    s=s+p
print("S3=",s)
n=eval(input("dati n="))
s=0
for i in range(12,n,1):
    i=i+1
    d=(n*10)+2
    if i==d:
        break
    elif (i-2)%10==0:
        s=s+i
print("S4=",s)
n=eval(input("dati n="))
s=0
b=0
for i in range(0,n,1):
    if i ==n/(n+1):
        break
    else:
        b=b+1
        s=s+(b/(b+1))
print("S5=",s)
n= eval(input("dati n(numar <=9)="))
b=0
s=0
for i in range(2,n+1,1):
    i=i+20
    b=b+i
    if n==9:
        break
    s=1+2+b
print("S6=",s)