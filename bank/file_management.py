import csv 

data_list = []  
file_name = ""
fields = []

def is_number(string):
    # crediting https://www.geeksforgeeks.org/python/python-check-if-given-string-is-numeric-or-not/
    try:
        float(string)
        return True
    except ValueError:
        return False



def open_file(given_file_name):
    global fields
    global file_name
    global data_list
    # from https://www.geeksforgeeks.org/python/working-csv-files-python/
    with open(given_file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)  

        file_name = given_file_name
        for row in csv_reader:
            data_list.append(row)
        
        # to convert the read values to numbers 
        for row in data_list:
            for key,value in row.items():
                if is_number(value):
                    row[f"{key}"] = int(value)
                    
        fields = [key for key in data_list[0]]


def write_to_file():
    # from https://www.geeksforgeeks.org/python/working-csv-files-python/
    with open(file_name, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data_list)
        


def get_row(customer_id):
    for data in data_list:
        if data["account_id"] == customer_id:
            return data
        
    return -1 #could raise a customized error here



def update_row(customer_id , field , new_value):
    
    for i in range(len(data_list)):
        if data_list[i]["account_id"] == customer_id:
            data_list[i][field] = new_value
    write_to_file()





