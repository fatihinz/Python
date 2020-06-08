f= open('workfile.txt','w')
f.write('fatih yavuzyilmaz!!@#\n')
f.close()

f= open('workfile.txt','r')
print(f.read())
f.close()