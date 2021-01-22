import pprint
import json
import requests
import csv

# a_dict = {"station": "Saint Petersbourg"}

# a_dict = {}

json_data = None
with open("stop_areas.json", "r+") as f:
    file = f.read()
    json_data = json.loads(file) #json.loads() takes a json string and converts it to a python object
    # json_data.update(a_dict)
    f.seek(0)
    json.dump(json_data, f) #json.dumps() takes a python object and converts it to a string

pprint.pprint(json_data)

# stop_areas: ["Saint Petersbourg"]





# data_file = open('data_file.csv', 'w') # open file for writing
# csv_writer = csv.writer(data_file) # create csv writer object















