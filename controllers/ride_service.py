class Ride:
	def __init__(self, creditCard, startPoint='', endPoint='', distance=0.0,
		expectedTimeMin=0, cost=5.0, tip=0.0, driver=None):
		self.creditCard = creditCard
		self.startPoint = startPoint
		self.endPoint = endPoint
		self.distance = distance
		self.expectedTimeMin = expectedTimeMin
		self.cost = cost
		self.tip = tip
		self.driver = driver

	# SETTERS
	def setStartPoint(startPoint):
		self.startPoint = startPoint

	def setDistance(distance):
		self.distance = distance

	def setExpectedTimeMin(minutes):
		self.expectedTimeMin = minutes

	def setCost(cost):
		self.cost = cost

	def setTip(tip):
		self.tip = tip

	def setDriver(driver):
		self.driver = driver

	# GETTERS
	def getCreditCard():
		return self.creditCard

	def getStartPoint():
		return self.startPoint

	def getEndPoint():
		return self.endPoint

	def getDistance():
		return self.distance

	def getExpectedTimeMin():
		return self.expectedTimeMin

	def getCost():
		return self.cost

	def getTip():
		return self.tip

	def getDriver():
		return self.driver

	# METHODS
	def getExpectedCost():
		return Price.getExpectedCost(getDistance(), getExpectedTimeMin())

	def assignDriver(DriversPool):
		setDriver(DriversPool.assignDriver)

	def payFor(amount):
		setCost(amount)

	def setDriverFree()
		getDriver.setBusy(False)