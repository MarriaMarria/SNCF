import pprint
import json
import requests
import csv

url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
headers = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
response = requests.get(url, headers=headers) #pop up for password
raw_data = json.loads(response.text) #dict

# PART 1: GETTING ID'S

areas = raw_data["stop_areas"] #list which we assign to the variable areas cause the name of the file is stop_ares!

print(len(areas)) # 25

# checking which elements we have inside our stop_areas nested list
# for loop_list in areas:
#     for element in areas:
#         print(f" {element} \n")

area = areas[0] #dict
# id = area["id"] 
# print(type(id)) # str

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

print(list_ids)

# PART 2: GETTING NAMES/LABELS

list_labels = []

for loop_label in areas:
    if type(loop_label) == dict:
        if "label" in loop_label.keys():
            local_label = loop_label["label"]
            list_labels.append(local_label)
        else:
            print("Missing key label")
    else:
        print(f"Unexpected format {type(loop_label)}")

print(list_labels)

# for label in list_labels:
#     print(label)

# PART 3: GETTING URL:s

links = raw_data['links'] # 11 dict with 1 href in each
# print(links)
link = links[0]
# print(link) # prints 1 href (first)
# print(link.keys()) # prints href, type, rel, templated
# print(area.keys())

# print(raw_data)
# Part 2: getting URL

# print(link)

list_hrefs = []

for loop_link in links:
    if type(loop_link) == dict:
        if "href" in loop_link.keys():
            local_href = loop_link["href"]
            list_hrefs.append(local_href)
        else:
            print("Missing key id")
    else:
        print(f"Unexpected format {type(loop_link)}")


# print(len(list_hrefs)) # 11
print(list_hrefs) # prints 11 hrefs from 11 dict from one list called links



