def bastir (*a):
	print(a)
	for i in a:
		print(i)

bastir(1,2,3,4,5)






def toplab(b,*a):
	sonuc=b
	for i in a:
		sonuc=sonuc+i
	return sonuc
	
print(toplab(12,3,5))

def fonksiyon (**a):
	for i in a:
	print (i+a[i])
fonksiyon(a=2,b=3,c=4)


