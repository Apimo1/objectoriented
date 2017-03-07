class StudentAccount(BankAccount):
	"""A bank accoount with the following attributes
	deposit
	withdraw
	balance"""
	def __init__(self,name,balance=500.0):
		"""Returns name of the account holderthe minimum amount in the account"""
		self.name=name
		self.balance=balance

	def deposit(self,amount):
		"""Returns integral amount after the deposit"""
		self.balance +=amount
		return self.balance

	def withdraw(self,amount):
		"""Returns intergral amount after withdrawal"""
		if amount>self.balance:
				raise RuntimeError("Withdrawal amount greater than account balance")
		self.balance -=amount
		return self.balance	