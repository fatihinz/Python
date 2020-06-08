class araba:
	hiz =0
	renk=""
	def hizlan(self):
		self.hiz = self.hiz+1

x = araba()
x.hiz=100
x.hizlan()
print("arabanin hizi",x.hiz)

y=araba()
print(y.hiz)
y.hiz =70
y.hizlan()

print(y.hiz)
print(x.hiz)