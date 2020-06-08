l4= [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

print (l4)

liste = list(map(lambda x:[x, x+1, x+2, x+3], range(1, 5)))
print(liste)