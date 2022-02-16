#Mathieu Finot
#POO syracuse

with open("tp1.txt", "r") as f:
    contenu = f.read()


a=int(input())
n=int(input())
i=0
print(n)
while i < a:
    if n % 2 == 0:
      n=n//2  
    else:
        n=n*3+1
    i=i+1
    print(n)

