

import csv 

data_list = []  

def open_file(file_name):
    # from https://www.geeksforgeeks.org/python/working-csv-files-python/
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)  


        for row in csv_reader:
            data_list.append(row)
            


