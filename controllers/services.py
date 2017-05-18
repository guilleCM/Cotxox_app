import requests
from flask import jsonify

class ProviderAPI:

	@staticmethod
	def getRideDistanceAndTime(startPoint, endPoint):
		API_KEY = "AIzaSyBYu65s-BcSNwfqQuEAZMq8RqUM-D8yb-4" 
		url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+startPoint+"&destinations="+endPoint+"&key="+API_KEY
		r = requests.get(url)
		datajson = r.json()
		distance = datajson['rows'][0]['elements'][0]['distance']['text']
		distance = distance[:-3]
		time = datajson['rows'][0]['elements'][0]['duration']['text']
		time = time[:-5]
		output = jsonify({'distance': float(distance), 'time': int(time)})
		return output