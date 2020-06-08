def fact(n):
	a=1
	sonuc =1
	while(a<=n):
		sonuc=sonuc*a
		a=a+1
	return sonuc
fact(5)
print(fact(5))

def facto(n):
	if(n==0):
		return 1
	return n*facto(n-1)
	
print(facto(5))

def fibo(n):
	if(n==0): return 1
	if(n==1): return 1
	return fibo(n-1)+fibo(n-2)
	
print("fibo")
print(fibo(7))