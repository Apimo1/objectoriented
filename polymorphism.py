class Animal:
	"""showing talk polymorphic behaviour of animals"""
	def __init__(self,name):
		self.name=name
class dog(Animal):
	def sound_type(self):
		return"bark"
class snake(Animal):
	def sound_type(self):
		return"hiss"
class cork(Animal):
	def sound_type(self):
		return"crow"