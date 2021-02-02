class VendingMachine:
	v = 0

	def __init__(self):
		self.soda = JunkDrink(self)


class JunkDrink:
	v = 0

	def __init__(self, machine):
		self.machine = machine
		self.machine.v += 1
		machine.v += 1
		self.v += 1


a = VendingMachine()
print(a.v)
# 2

print(JunkDrink.v)
# 0

print(a.soda.v)
# 1

x = VendingMachine.__init__(a)
print(x)
# None

print(a.v)
# 4

print(JunkDrink.v)
# 0

print(a.soda.v)
# 1