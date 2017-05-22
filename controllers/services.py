import requests
from flask import jsonify

class Tax:
	costPerKm = 1.35
	costPerMin = 0.35
	minCost = 5.0
	percentageCotxox = 0.20
	#Methods
	@staticmethod
	def getDistanceCost(distanceInKm, costPerKm=costPerKm):
		return costPerKm*distanceInKm

	@staticmethod
	def getTimeCost(timeMin, costPerMin=costPerMin):
		return costPerMin*timeMin

	@staticmethod
	def getExpectedPrice(distanceInKm, timeMin, minCost=minCost):
		total = Tax.getDistanceCost(distanceInKm)+Tax.getTimeCost(timeMin)
		if total < minCost:
			total = minCost
		return total

class ProviderAPI:

	@staticmethod
	def getRidePreview(startPoint, endPoint):
		API_KEY = "AIzaSyBYu65s-BcSNwfqQuEAZMq8RqUM-D8yb-4" 
		url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+startPoint+"&destinations="+endPoint+"&key="+API_KEY
		r = requests.get(url)
		datajson = r.json()
		distance = datajson['rows'][0]['elements'][0]['distance']['text'] #outputExample = u'12.1 km'
		distance = ProviderAPI.getDistance(str(distance))
		time = datajson['rows'][0]['elements'][0]['duration']['text']
		time = ProviderAPI.getTime(time)
		cost = Tax.getExpectedPrice(distance, time)
		output = jsonify({'distance': distance, 'time': time, 'cost':round(cost,2)})
		return output

	@staticmethod	
	def getDistance(string):
		output = ''
		measure = ''
		for letter in string:
			if letter.isdigit() or letter == '.':
				output += letter
			elif letter.isalpha():
				measure += letter
		if ',' in output:
			output = output.replace(',','.')
		output = float(output)
		if measure == 'm':
			output = output / 1000
		return output

	@staticmethod
	def getTime(string):
		values = []
		output = ''
		if ',' in string:
			values = string.split(",")
		if len(values) != 2:
			for letter in string:
				if letter.isdigit():
					output += letter
			output = int(output)
		else:
			hours = ''
			for letter in values[0]:
				if letter.isdigit():
					hours += letter
			output = int(hours) * 60
			minuts = ''
			for letter in values[1]:
				if letter.isdigit():
					minuts += letter
			output += int(minuts)
		return output