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
		distance = datajson['rows'][0]['elements'][0]['distance']['text']
		distance = distance[:-3]
		time = datajson['rows'][0]['elements'][0]['duration']['text']
		time = time[:-5]
		cost = Tax.getExpectedPrice(float(distance), int(time))
		output = jsonify({'distance': float(distance), 'time': int(time), 'cost':round(cost,2)})
		return output