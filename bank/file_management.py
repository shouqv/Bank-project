import csv 

data_list = []  
file = ""

def is_number(string):
    # crediting https://www.geeksforgeeks.org/python/python-check-if-given-string-is-numeric-or-not/
    try:
        float(string)
        return True
    except ValueError:
        return False



def open_file(file_name):
    # from https://www.geeksforgeeks.org/python/working-csv-files-python/
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)  

        file = file_name
        for row in csv_reader:
            data_list.append(row)
        
        # to convert the read values to numbers 
        for row in data_list:
            for key,value in row.items():
                if is_number(value):
                    row[f"{key}"] = int(value)



def get_row(customer_id):
    
    for data in data_list:
        if data["account_id"] == customer_id:
            return data
        
    return -1 #could raise a customized error here


# open_file("data/bank.csv")
# print(get_row(10004))



