from flask import request


class Utils():
	
	@staticmethod
	def getDevice():
		# device = request.user_agent.platform
		# if device == 'windows' or device == 'linux' or device == 'macos':
		# 	return 'horizontal'
		# else:
		return 'vertical'