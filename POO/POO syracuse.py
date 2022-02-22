#Mathieu Finot
#POO syracuse

f = open("tp1.txt", "r+")
test =[]
test = f.readlines()
n=int(test[0])

class operation:
    
	def egale0(n):
		return n//2

	def diffzero(n):
		return n*3+1

while n != 1:
    if n % 2 == 0:
      n=operation.egale0(n)  
    else:
        n=operation.diffzero(n)
    f.write("\n")
    f.write(str(n))
f.close()

