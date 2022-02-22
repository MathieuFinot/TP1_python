#Mathieu Finot
#POO syracuse

f = open("tp1.txt", "r+")
test =[]
test = f.readlines()
n=int(test[0])



while n != 1:
    if n % 2 == 0:
      n=n//2  
    else:
        n=n*3+1
    f.write("\n")
    f.write(str(n))
f.close()