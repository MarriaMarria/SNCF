import pprint
import json
import requests
import csv
import pandas as pd
from collections import OrderedDict

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

#print(list_ids)

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

#print(list_labels)

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
# print(list_hrefs) # prints 11 hrefs from 11 dict from one list called links

my_dict = {}
my_dict = dict(zip(list_labels, zip(list_ids, list_hrefs))) 
print(my_dict)
print(type(my_dict))


# def write_csv(data):
#     with open('data_file.csv', 'a') as file:
#         writer = csv.writer(file)

#         writer.writerow([data['id'], data['label'], data['url']])


# d= {'id', 'label', 'url'}

# l = [d, list_ids, list_labels, list_hrefs]

# for item in l:
#     write_csv(item)

def write_csv(data):
    with open('data_csv.csv', 'a') as file:
        order = ['id', 'label', 'url']
        writer = csv.DictWriter(file, fieldnames = order)

        writer.writerow(data)

d= {'id', 'label', 'url'}
l = [d, list_ids, list_labels, list_hrefs]

for item in l:
    write_csv(item)




# with open('data_file.csv', "w") as f:
#     for key in my_dict():
#         f.write("%s,%s\n"%(key, my_dict[key]))


# csv_columns = ['label','id','href']
# csv_file = "data_file.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for data in my_dict:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")






# d = {}
# d['id'] = list_ids
# d['labels'] = list_labels
# d['hrefs'] = list_hrefs

# for key, value in d.items():
#     print(key, value)

# print(d)
# print(type(d))

# my_dict = {}
# my_dict = zip(list_ids, list_hrefs)

# my_dict = dict(zip(list_labels, zip(list_ids, list_hrefs)))
# my_dict = dict(zip(list_labels, zip(map(int, list_ids), map(int, list_hrefs))))
# my_dict = dict(zip(list_labels, map(list, zip(map(int, list_ids), map(int, list_hrefs)))))

# print(my_dict)


# STEP 4: CREATING CSV FILE

# file_csv = pd.DataFrame(d)
# d.to_csv("data_file.csv")



# csv_file = pd.DataFrame(list_ids)
# csv_file.to_csv("data_file.csv")
# csv_file = pd.DataFrame(list_labels)
# csv_file.to_csv("data_file.csv")
# csv_file = pd.DataFrame(list_hrefs)
# csv_file.to_csv("data_file.csv")

# header = ['id', 'label', 'url']
# rows = [[list_ids],
#         [list_labels],
#         [list_hrefs]]

# with open("data_file.csv", "w") as f:
#     write = csv.writer(f)
#     write.writer.writerow(header)
#     write.csvwriter.writerow(rows)

