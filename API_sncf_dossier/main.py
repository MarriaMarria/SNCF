from classes2 import ReadSncfApi

# def main():

sncf = ReadSncfApi() # object of ReadSncfApi() class
sncf.read_json() # I call read.json() function on my class object sncf
sncf.save_links()
sncf.get_endpoints()
sncf.get_ids()
sncf.save_csv_href()
sncf.get_names()

# sncf.list_labels # checking list
# print(sncf.my_labels())


# if __name__ == 'main':
#     print("HELLO")
#     main()