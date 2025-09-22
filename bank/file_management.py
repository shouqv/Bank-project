import csv 


class FileManagement():
    def __init__(self,file_name):
        self.file_name = file_name
        self.data_list = []
        self.fields = []
        self.load_data()
        
    def is_number(self, string):
        # crediting https://www.geeksforgeeks.org/python/python-check-if-given-string-is-numeric-or-not/
        try:
            float(string)
            return True
        except ValueError:
            return False



    def load_data(self):
        # from https://www.geeksforgeeks.org/python/working-csv-files-python/
        with open(self.file_name, mode='r') as file:
            csv_reader = csv.DictReader(file)  

            for row in csv_reader:
                self.data_list.append(row)

            # to convert the read values to numbers 
            for row in self.data_list:
                for key,value in row.items():
                    if self.is_number(value):
                        row[f"{key}"] = int(value)

            self.fields = [key for key in self.data_list[0]]


    def write_to_file(self):
        # from https://www.geeksforgeeks.org/python/working-csv-files-python/
        with open(self.file_name, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(self.data_list)



    def get_row(self,customer_id):
        for data in self.data_list:
            if data["account_id"] == customer_id:
                return data

        return -1 #could raise a customized error here

    def add_row(self , **kwargs):
        for key in kwargs:
            if key not in self.fields:
                return #could rise an error here
        
        self.data_list.append(kwargs)
        self.write_to_file()

    def update_row(self,customer_id, field , new_value):
        for i in range(len(self.data_list)):
            if self.data_list[i]["account_id"] == customer_id:
                self.data_list[i][field] = new_value
        self.write_to_file()



# file = FileManagement("data/bank.csv")
