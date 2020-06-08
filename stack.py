from collections import deque

l2 = [44,55,66]
l2.append(77)
print(l2)
l2.pop(0)
print(l2)

l3=deque([11,23,45])
print(l3)
l3.append(67)
print(l3.popleft())
print(l3)