class Driver:
	def __init__(self, name='', carLicense='', carModel='', rates=[], isBusy=False, averageRate=4.0)
	self.name = name
	self.carLicense = carLicense
	self.carModel = carModel
	self.rates = rates
	self.isBusy = isBusy
	self.averageRate = averageRate

	# SETTERS
	def setCarLincense(carLicense):
		self.carLicense = carLicense

	def setCarModel(carModel):
		self.carModel = carModel

	def setIsBusy(status):
		self.isBusy = status

	def setAverageRate(rate):
		self.averageRate = rate

	# GETTERS
	def getRates():
		return self.rates

	def isBusy():
		return self.isBusy

	def getName():
		return self.name

	def getCarModel():
		return self.carModel

	def getCarLicense():
		return self.carLicense

	def getAverageRate():
		return self.averageRate

	# METHODS
	def setRate(stars):
		pass

	def sumOfRates():
		total = 0
		return total