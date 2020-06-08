l=[1,2,3]
m=[[1,2,3],[3,4,5],l]

print (m)

del(m[1])

l[1]=100
print(m)

print(len(l))


mt = [[row[i] for row in m] for i in range(3)]

print(mt)
