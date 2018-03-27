# read data based by parameter
import json
def Open(nama):
	file = open(nama+'.txt','r+')
	return json.load(file)