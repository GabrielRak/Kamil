import os 
import json 
import csv
from functools import wraps
from openpyxl import load_workbook

class Service:

    def __init__(self, extension, folder):
        self.extension = extension
        self.folder = folder


    def save_data(self, data,filename):
        FILE_TO_SAVE = self.folder + '/' + filename + '.' + self.extension
        os.makedirs(os.path.dirname(FILE_TO_SAVE), exist_ok=True)
        with open(FILE_TO_SAVE, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("Data saved to file: ", FILE_TO_SAVE)


    def file_checker_decorator(func):
            @wraps(func)
            def wrapper(self, directory):
                files = os.listdir(directory)
                print(f"Files in directory: {files}")
                return func(self, files,directory)  
            return wrapper

    @file_checker_decorator
    def load_data_from_files(self, files,directory):
        data = {}
        for file in files:
            try:
                file_path = os.path.join(self.folder, file)
                with open(file_path, "r") as f:
                    if file.endswith(".json"):
                        data[file] = json.load(f)
                        print(f'Data frm {file} \n\ {data[file]}')
                    elif file.endswith(".csv"):
                        reader = csv.reader(f)
                        data[file] = list(reader)
                    elif file.endswith(".xlsx"):
                        workbook = load_workbook(file_path)
                        print(f'Type of workbook: {type(workbook)}')
                        data[file] = {sheet.title: list(sheet.values) for sheet in workbook}
                        print(type(data[file]))
                        print(f'Data frm {file} \n\ {data[file]}')
            except Exception as e:
                print(f"Error loading {file}: {e}")

        return data
    
