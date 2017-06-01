import unittest

from services import *

class TestServices(unittest.TestCase):
	def test_getExpectedPrice(self):
		distance = 7.75
		time = 10
		expected = 13.9625
		self.assertEqual(expected, Tax.getExpectedPrice(distance, time))
	def test_getExpectedPricePalmaMagaluf(self):
		distance = 18
		time = 23
		expected = 32.35
		self.assertEqual(expected, Tax.getExpectedPrice(distance, time))
	def test_getExpectedPricePalmaManacor(self):
		distance = 50.6
		time = 47
		expected = 84.76
		self.assertEqual(expected, Tax.getExpectedPrice(distance, time))
	def test_getExpectedPriceMinPrice(self):
		distance = 2
		time = 3
		expected = 5.0
		self.assertEqual(expected, Tax.getExpectedPrice(distance, time))
	def test_getDistanceWithMeters(self):
		string = "12 m"
		expected = 0.012
		self.assertEqual(expected, ProviderAPI.getDistance(string))
	def test_getDistanceWithKm(self):
		string = "125 km"
		expected = 125
		self.assertEqual(expected, ProviderAPI.getDistance(string))
	def test_getDistanceWithKmWithComma(self):
		string = "18.0 km"
		expected = 18.0
		self.assertEqual(expected, ProviderAPI.getDistance(string))
	def test_getTimeMinute(self):
		string = "1 minut"
		expected = 1
		self.assertEqual(expected, ProviderAPI.getTime(string))
	def test_getTimeMinutes(self):
		string = "17 minuts"
		expected = 17
		self.assertEqual(expected, ProviderAPI.getTime(string))
	def test_getTimeHourAndMinut(self):
		string = "1 hour 1 minut"
		expected = 61
		self.assertEqual(expected, ProviderAPI.getTime(string))
	def test_getTimeHoursAndMinutes(self):
		string = "2 hours 23 minuts"
		expected = 143
		self.assertEqual(expected, ProviderAPI.getTime(string))


if __name__ == '__main__':
	unittest.main()