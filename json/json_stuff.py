import json

# f = open('json/sample4.json')

# data = json.load(f)

# print(data)

# f.close()

def loadJSONFile(filename):
    try:
        with open(filename , 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("\nErro: ficheiro não encontrado!\n")
        return []
    except:
        print("\nErro estilo Microsoft: i have no idea what happened!\n")
        return []
    else:
        return data
 
print(loadJSONFile("json/sample4.json"))
print("Terminou")

# with open('json/sample4.json' , 'r') as f:
#     data = json.load(f)
    
# print(data['people'])
    
# for elem in data['people']:
#     print(elem['firstName'])
    
    
def saveJSONFile(filename, list):
    """
    Save a list to a JSON file
    :param filename: the name of the file to save
    :param list: the list to save
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(list, f, indent=4)
    except FileNotFoundError:
        print("\nErro: não foi possível gravar o ficheiro!\n")
    except:
        print("\nUps, something wrong happened!")
 
 
#print(loadJSONFile("json/sample4.json"))
listFormandos = [
    {'id' : 1, 'firstName' : 'Ana', 'lastName' : 'Maria'},
    {'id' : 2, 'firstName' : 'Abel', 'lastName' : 'Gonçalves'},
    {'id' : 3, 'firstName' : 'Sofia', 'lastName' : 'Pereira'},
    {'id' : 4, 'firstName' : 'Rui', 'lastName' : 'Rio'},
    {'id' : 5, 'firstName' : 'Cavaco', 'lastName' : 'Luís'}
]
 
saveJSONFile("json/formandos.json", listFormandos)
print("Terminou")
    
    