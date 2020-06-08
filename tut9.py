class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	
	def talk(self):
		raise NotImplementedError("Subclass must implement abstract method")
	
class Cat(Pet):
	def __init__(self, name, age):
		super().__init__(name, age) #super class method is here
		
	def talk(self):
		return "meowww"	

class Dog(Pet):
	def __init__(self, name, age):
		super().__init__(name, age)
		
	def talk(self):
		return "wooooffff"
		
		
def Main():
	# thePet = Pet("Pet", 1)
	# jess = Cat("jess", 3)
	
	# print("is jess a cat"+ str(isinstance(jess, Cat)))
	# print("is jess a pet"+ str(isinstance(jess, Pet)))
	# print("is pet a cat"+ str(isinstance(Pet, Cat)))
	# print("is pet a pet"+ str(isinstance(thePet, Pet)))
	# print(jess.name)
	
	pets = [Cat("jess", 3), Dog("jack", 2), Cat("Fred", 7), Pet("ThePet", 5)]
	
	for pet in pets:
		print("Name :" + pet.name+",Age :"+ str(pet.age)+ "talks :" + pet.talk())
	
	
if __name__ == '__main__':
	Main()