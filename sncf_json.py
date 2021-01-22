import pprint
import json
import requests
import csv

url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
response = requests.get(url, headers=headers) #pop up for password
raw_data = json.loads(response.text) #dict

# print(response)
# print(type(raw_data)) #dict




# for key, value in raw_data.items():
#     print(f"{key} is {value}")

# PART 1: GETTING ID'S

areas = raw_data["stop_areas"] #list which we assign to the variable areas cause the name of the file is stop_ares!

# print(type(areas))
# print(areas)
print("WARNING")

area = areas[0] #dict
# print(area)
# print(type(area), area)
# print(f"Printing AREAS: {areas}")
# print(f"printing area: {area}")


list_ids = []

for loop_area in areas:
    if type(loop_area) == dict:
        if "id" in loop_area.keys(): #!!!!!!
            local_id = loop_area["id"]
            list_ids.append(local_id)
        else:
            print("Missing key id")
    else:
        print(f"Unexpected format {type(loop_area)}")

# print(len(list_ids))
print(list_ids)

# Part 2: getting URL

list_href = []

for loop_area in areas:
    if "links" in loop_area.keys():
        local_href = loop_area["links"]
        list_href.append(local_href)
    else:
        print("Missing key id")

print(list_href) # 25 empty lists inside a list

list_names = []

for loop_name in areas:
    if "name" in loop_name.keys():
        local_name = loop_name["name"]
        list_names.append(local_name)
    else:
        print("Missing key name")
print(list_names)

# option with try/except:
    # try:
    #     loop_name["name"]
    # except:
    #     list_names.append("")
    # else:
    #     list_names.append(loop_name["name"])

# list_coords = []

# for loop_coord in areas:
#     if "coords" in loop_coord.keys():
#         local_coord = loop_coord["coords"]
#         list_coords.append(local_coord)

# print(list_coords)






#print(area.keys()) # prints all keys of current json: ['codes', 'name', 'links', 'coord', 'label', 'administrative_regions', 'timezone', 'id']

# PART 3: GETTING NAMES









#       1 -  faire un loop in json data
#       2 - json data est un dictionnaire
#       3 - creer  une nouvelle liste
#       4 - append le data obtenu dedans le FOR dans la nouvelle liste
#       5 - creer un dataframe avec panda
#       6 - transformer le dataframe to csv
#       hint:  on peut looper dans un diictionaire