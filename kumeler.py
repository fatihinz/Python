l= [1,2,3,1,2,3,4] #liste
t= (1,2,3) #kayit
k={1,2,3,1,2,3,1} #kume tekrar etmez

print(k)

k2= set(l)

print(k2)

k4=set('yavuzyilmaz')
k5=set('Fatih')

print(k4)
print(k5)

print(k4|k5) #birlesim kumesi

print(k4-k5) # kume farki 
print(k5-k4)
print(k4&k5) #kume kesisimi
print(k4^k5) #exor iki kumenin sadece birinde yer alanlar
