#Mathieu Finot


n=int(input ("Conjecture de Syracuse: "))

print(n)
while n != 1:
    if n % 2 == 0:
      n=n//2  
    else:
        n=n*3+1
    i=i+1
    print(n)