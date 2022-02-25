import csv
import json


def readCSV(filename):
    with open(filename, newline='', ) as csv_file:
        dataset = csv.reader(csv_file)
        next(dataset)
    
        return np.array(list(dataset))

def readLabelNames(filename):
    with open(filename) as file_data:
        json_data = json.load(file_data)
        label_names = list(json_data.values())
        
        return label_names
