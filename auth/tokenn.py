import json
from datetime import datetime


# function to add to JSON
def write_json(new_data, filename='token.json'):
	with open(filename,'r+') as file:
		# First we load existing data into a dict.
			file_data = json.load(file)
			# Join new_data with file_data inside emp_details
			file_data["token"].append(new_data)
			# Sets file's current position at offset.
			file.seek(0)
			# convert back to json.
			json.dump(file_data, file, indent = 4)

def token_generate(token):
		now = datetime.now()
		date = now.strftime("%m-%d-%y")
		y = {date:token}
		try:
			write_json(y)
		except:
			pass
