import csv
# CSV'S stuff
# with open('./exemplos.csv' , 'r') as f:
#     # reader = list(csv.reader(f))
#     reader = list(csv.DictReader(f))
#     print(reader)
    
    
#

def loadCSVFile(filename):
    """
    Load a CSV file and return the data
    :param filename: the name of the file to load
    :return: the data in the file
    """
    try:
        with open(filename , 'r') as f:
            data = list(csv.DictReader(f))
    except FileNotFoundError:
        return []
    except:
        return []
    else:
        return data


def writeCSVFile(filename,data):
    try:
        with open(filename , 'w') as f:
            csv_writer = csv.writer(csvfile)
    except FileNotFoundError:
        return []
    except:
        return []
    else:
        return csv_writer.writerows(data)

def saveJSONFile(filename, listVal):
    """
    Save a list to a JSON file
    :param filename: the name of the file to save
    :param list: the list to save
    """
    try:
        with open(filename, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(listVal[0])
            for item in listVal:
                writer.writerow(list(item.values()))
    except FileNotFoundError:
        print("\nErro: não foi possível gravar o ficheiro!\n")
    except:
        print("\nUps, something wrong happened!")

data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
    ["Bob", 35, "Chicago"]
]

filename = "data.csv"

with open(filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)