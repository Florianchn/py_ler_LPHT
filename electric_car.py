class Car():
	"""Car simulieren"""
	
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' +self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
			
	def increment_odometer(self, miles):
		self.odometer_reading += miles

class Battery():
	"""Battery simulieren"""
	
	def __init__(self, battery_size=70):
		"""reset die Eigenschaften der Battery"""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""drucken eine Information"""
		print("This car has a " + str(self.battery_size) + "kWh battery.")	
	
	def get_range(self):
		"""zusaetzliche verfuegbare Distanz"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
				
		message = "This car can go approxximately " + str(range)
		message += " miles on a full charge."
		print(message)
				
class ElectricCar(Car):
	"""Die Besonderheit des electricCar"""
	
	def __init__(self, make, model, year):
		"""reset die Eigenschaft des Vater"""
		super().__init__(make, model, year)
		self.battery = Battery()
#		self.battery_size =70
	
#	def describe_battery(self):
#		"""
#		drucken eine Information ueber die kapazitaet
#		des Battery
#		"""
#		print("This car has a " + str(self.battery_size) + "-kwh battery.")
#	def fill_gas_tank():
#		"""Eletrische Auto hast kein Tank"""
#		print("This car doesn't need a gas tank!")
			
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()