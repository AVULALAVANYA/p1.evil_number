n=376
sql=n**2
count=len(str(n))
rem=sql%(10**count)
if (n==rem):
    print('automorphic')
else:
    print('not automorphic')