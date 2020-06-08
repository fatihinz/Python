def f(x):
	return x+10
	
print(f(8))

def merhaba(para):
	print("merhaba dunya"+str(para))

merhaba("evren")
merhaba(10)

def fib(n):
	a,b=0,1
	while a<n:
		print(a)
		a,b=b,a+b

fib(20)