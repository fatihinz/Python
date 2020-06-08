def fibo(n):
	if(n==0): return 1
	if(n==1): return 1
	return fibo(n-1)+fibo(n-2)
	
print("fibo")
print(fibo(7))

def g(x,y=3):
	return x+5*y
print g(2)