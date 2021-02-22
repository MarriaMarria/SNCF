import json
import requests
import csv
import pandas as pd
import pprint
import os
import unittest
import logging

class ReadSncfApi():

    
    logging.basicConfig(filename = "sncf.log", 
    level= logging.INFO, 
    format='%(asctime)s - %(name)s -%(levelname)s - %(message)s')

    def __init__(self):
        self.url_stop_areas = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        self.headers_stop_areas = {"Authorization": "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}
        self.list_hrefs = []
        self.data = None
        self.filename_json = 'stop_areas_maria' # we don't put .json; local copy of url
        self.filename_csv = 'TEST_csv'
        self.list_ids = []
        self.list_labels = []

        self.url_Paris_Lyon = 'https://api.sncf.com/v1/coverage/sncf/journeys?from=stop_area:OCE:SA:87686006&to=stop_area:OCE:SA:87722025'
        self.headers_Paris_Lyon = {'Authorization': "e3f2b3a6-caa9-47d7-98ee-1f67379e654b"}

    def read_json(self):  # reads and saves a local copy of json / stop_areas_maria.json

        logging.info('Requesting API: start')
        try:
            response = requests.get(self.url_stop_areas, headers=self.headers_stop_areas) 
            #headers1 is a name of the parameter, second = my real header attribute

            with open(self.filename_json + '.json', mode="w") as file:
                json.dump(response.json(), file) # to write a local copy of json
                
        except OSError:
            logging.info('Error: cannot access the file')

            
        logging.info('Requesting API: end')

    def save_links(self):

        logging.info('Reading json from API: start')

        try:
            with open(self.filename_json + '.json') as json_stop_areas_file:
                data = json.load(json_stop_areas_file) # data is all stop_areas file we got from url
            self.data = data
            logging.info("all good")
        except Exception as e:
            logging.info(f"Error: couldn't save the file, {e}")  

        # print(data) 
        # print(type(data))   
        # print(data.keys())
        # links = data['links'] # list
        # print(type(links))
        # link = links[0]
        # print(f'printing {link}')
        logging.info('Reading json from API: end')

    def get_endpoints(self):
    
        logging.info('Getting list of links: start')
        
        links = self.data['links']
        print(links)
        print(type(links)) #list
        # link = links[0]

        for loop_link in links: # looping throw the links to find "href"

            if type(loop_link) == dict:
                if "href" in loop_link.keys():
                    local_href = loop_link["href"]
                    self.list_hrefs.append(local_href)
                else:
                    print("Missing key id")
            else:
                print(f"Unexpected format {type(loop_link)}") 
        logging.info('Getting list of links: end')

    def get_ids(self):

        logging.info("Saving id's to csv: start")

        # try: 
        #     with open(self.filename_json + '.json') as json_stop_areas_file:
        #         data = json.load(json_stop_areas_file)

        areas = self.data['stop_areas']  #dict
        # print(areas) test
        for loop_area in areas:

            if type(loop_area) == dict:
                if "id" in loop_area.keys(): 
                    local_id = loop_area["id"]
                    self.list_ids.append(local_id)
                    # print(self.list_ids)
                else:
                    print("Missing key id")
                    
            else:
                print(f"Unexpected format {type(loop_area)}")

        logging.info("Saving id's to csv: end")

    def save_csv_href(self): # open stop_areas_maria

        logging.info('Saving links to csv: start')

        try:
            with open(self.filename_csv + '.csv', mode="w", newline='') as f: # I named my file maria.csv
                csv_writer = csv.writer(f, delimiter=';')

                if type(self.list_hrefs) == list:
                
                    for item in self.list_hrefs:
                        csv_writer.writerow([item])

                else: 
                    print("Unexpected input")
                    print("csv ok") # test

        except Exception as e:
            logging.info(f"Saving links to csv: end; Error, code is {e}")


    def get_names(self):

        logging.info("Saving station names: start")
        areas = self.data['stop_areas']
        for loop_label in areas:
            if type(loop_label) == dict:
                if "label" in loop_label.keys():
                    local_label = loop_label["label"]
                    self.list_labels.append(local_label)
                    # print(self.list_labels)
                else:
                    print("Missing key label")
            else:
                print(f"Unexpected format {type(loop_label)}")
        logging.info("Saving station names: end")

