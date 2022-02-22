#Mathieu Finot
#POO syracuse

f = open("tp1.txt", "rw")
n=f.readlines()

print(n)
while n != 1:
    if n % 2 == 0:
      n=n//2  
    else:
        n=n*3+1
    i=i+1
    print(n)
f.close()