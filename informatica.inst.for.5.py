n = int(input("dati n="))
s=0
for i in range(1,n,1):
    if ((i%3==0) and (i%5==0)):
        s=s+i
print(s)