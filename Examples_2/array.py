l=[1,2,3,4]
print(l)
l.append(55)
print(l)
l.insert(2,111)
l.insert(2,111)
l.insert(2,111)
l.insert(2,111)
print(l)
l.remove(111)
print(l)
print(l.pop())
print(l)
print(l.index(4))
print(l.count(111))
l2=[3,4,5]
l.extend(l2)
print(l)
l.sort()
print(l)
l.clear()
print(l)
l3=l2
print(l3)
l3.append(3)
print(l2)
print(l3)
l4=l2.copy()
l2.append(4)
print(l4)
print(l2)