import json
import requests
import pprint
import datetime
from dateutil import parser

url = 'https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025'
headers = {'Authorization': "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
responseParisLyon = requests.get(url, headers=headers) # pop up for password
dataParisLyon = json.loads(responseParisLyon.text) # dict


# pprint.pprint(dataParisLyon)

# print(dataParisLyon.keys()) # <class 'dict'>

# print(dataParisLyon.keys()) #dict_keys(['tickets', 'links', 'journeys', 'disruptions', 'notes', 'feed_publishers', 'context', 'exceptions'])

# for loop_key in dataParisLyon.keys():
#     print(type(dataParisLyon[loop_key]), loop_key)

''' prints:
<class 'list'> tickets
<class 'list'> links
<class 'list'> journeys
<class 'list'> disruptions
<class 'list'> notes
<class 'list'> feed_publishers
<class 'dict'> context
<class 'list'> exceptions
''' 


journeys = dataParisLyon['journeys']
# print(type(journeys)) # list

journey = journeys[0]
# print(journey)
# print(type(journey)) # dict

# print(len(journeys)) # 1
# print(journeys)

# for loop_keys in journey:
#     print(loop_keys)

# dict_keys(['status', 'distances', 'links', 'tags', 
# 'nb_transfers', 'durations', 'arrival_date_time', 'calendars', 
# 'departure_date_time', 'requested_date_time', 'fare', 
# # 'co2_emission', 'type', 'duration', 'sections'])

# for loop_key in journey.keys():
#     print(type(journey[loop_key]), loop_key)

'''
<class 'str'> status
<class 'dict'> distances
<class 'list'> links
<class 'list'> tags
<class 'int'> nb_transfers
<class 'dict'> durations
<class 'str'> arrival_date_time
<class 'list'> calendars
<class 'str'> departure_date_time
<class 'str'> requested_date_time
<class 'dict'> fare
<class 'dict'> co2_emission
<class 'str'> type
<class 'int'> duration
<class 'list'> sections
'''

# going throw all dict:
# distances = journey["distances"]
# print(distances)
# durations = journey["durations"]
# print(durations)
# fare = journey["fare"]
# print(fare)
# co2_emission = journey["co2_emission"]
# print(co2_emission)

# ints

# print(journey["nb_transfers"]) #0
# transfers = []
# for loop_transf in journeys:
#     if type(loop_transf) == dict:
#         if "nb_transfers" in loop_transf.keys():
#             local_transf = loop_transf["nb_transfers"]
#             transfers.append(local_transf)

# print(transfers)    

# print(journey["duration"]) # 8220
#0

# duration = []

# for loop_duration in journeys:
#     if type(loop_duration) == dict:
#         if "duration" in loop_duration.keys():
#             local_duration = loop_duration["duration"]
#             duration.append(local_duration) # 8220

#print(duration)

# lists

sections = journey["sections"]
# print(type(sections)) # list
# print(len(sections)) # 3 (list section has 3 dicts)

section = sections[1] # second dict in sections list

# pprint.pprint(section)
# print(type(section)) # dict


# for loop_key in section.keys():
#     print(type(section[loop_key]), loop_key)
'''
<class 'dict'> from
<class 'list'> links
<class 'str'> arrival_date_time
<class 'list'> additional_informations
<class 'dict'> co2_emission
<class 'dict'> display_informations
<class 'dict'> to
<class 'str'> base_arrival_date_time
<class 'str'> base_departure_date_time
<class 'str'> departure_date_time
<class 'dict'> geojson
<class 'int'> duration
<class 'str'> type
<class 'str'> id
<class 'str'> data_freshness
<class 'list'> stop_date_times

'''

stop_date_times = section["stop_date_times"]
# pprint.pprint(stop_date_times)
# print(type(stop_date_times)) # list
# print(len(stop_date_times))

# prints nicely in the terminal the parts of stop_date_time
print("ENUMERATE")
for i in enumerate(stop_date_times):
    print(i)
    print("\n")


nmb_stations = len(stop_date_times) - 2

# print(nmb_stations)

station_paris_lyon = []

# for stop in stop_date_times:
#     if "stop_point" in stop.keys():
#         local_name_station = stop["stop_point"]["label"]
#         station_paris_lyon.append(local_name_station)

# print(station_paris_lyon)
# ['Paris-Gare-de-Lyon (Paris)', 'Creusot - TGV (le) (Écuisses)', 
# 'Mâcon-Loché-TGV (Mâcon)', 'Lyon-Part-Dieu (Lyon)', 'Lyon-Perrache (Lyon)']



#Durée d'attente entre chaque arrêt: arrival_date_tim - departure_date_time  > je reste dans ma stops liste 
stations_arrival_time = []
stations_departure_time = []

# for stop in stop_date_times: 
#     if "arrival_date_time" in stop.keys():
#         arrival = stop["arrival_date_time"]
#         stations_arrival_time.append(arrival)
# print(stations_arrival_time)

# for stop in stop_date_times: 
#     if "departure_date_time" in stop.keys():
#         departure = stop["departure_date_time"]
#         stations_departure_time.append(departure)
# print(stations_departure_time)

# transform the info received in normal date time etc like temps d'arret:  0:03:00


stop_times = []

for key, stop in enumerate(section['stop_date_times']):#<class 'dict'>

#print(type(stop))#<class 'dict'>
#print(stop['stop_point'])#dict
#print(stop['stop_point']['name'])
#print(cle)

    if key != 0 and key != (len(section['stop_date_times']) -1):
        stop_name  = stop['stop_point']['name']

        station_paris_lyon.append(stop_name)      

        arrival_time = stop["arrival_date_time"]
        departure_time = stop["departure_date_time"]

        arrival_converted = parser.parse(arrival_time) #<class 'datetime.datetime'> datetime.datetime(2021, 1, 25, 19, 13)
        departure_converted = parser.parse(departure_time) #<class 'datetime.datetime'>

        result_time = departure_converted - arrival_converted

print(stop_times)

stop_times.append([stop_name, str(result_time)])

print('There are ', nmb_stations, ' stops : ',station_paris_lyon)

#---- combien de temps d’arrêt à chacune d’elles ?

print("Time between stops: ", stop_times)
































# def searchStation(to, from):
#     url = journeysUrl
#     api_key = token_auth
#     destination1 = from
#     destination2 = to
#     json_obj = urllib.urlopen()
#     final_url =  url + "?from" + destination1 + "&to" + destination2 

# arrival_date_time = journey[0]["arrival_date_time"]

# print(type(arrival_date_time)) # str
# print(len(arrival_date_time)) # 15
# print(arrival_date_time) # 20210125T080900




