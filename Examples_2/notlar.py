l = []
for x in range(10):
	l.append(x**2)
print(l)
print(x)

squares = list(map (lambda y: y**2,range(10)))

print(squares)


def f(x):
	return x+5

l2=(2,8,3)

print(list(map(f,l2)))
print(list(map(lambda x:x+5,l2)))

l3= [x**2 for x in range(10)]
print(l3)