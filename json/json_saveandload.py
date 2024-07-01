
import json, beaupy
 
def loadJSONFile(filename):
    """
    Load a JSON file and return the data
    :param filename: the name of the file to load
    :return: the data in the file
    """
    try:
        with open(filename , 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except:
        return []
    else:
        return data
 
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
 
def nextID(listFormandos):
    ids = [formando['id'] for formando in listFormandos]
    return max(ids)+1
 
def addFormando():
    print("\nAdicionar formando: \n")
    firstName = input("Nome próprio: ")
    lastName = input("Apelido: ")
    id = nextID(listFormandos)
    return {'id' : id, 'firstName' : firstName, 'lastName' : lastName}
 
 
#print(loadJSONFile("json/sample4.json"))
# listFormandos = [
#     {'id' : 1, 'firstName' : 'Ana', 'lastName' : 'Maria'},
#     {'id' : 2, 'firstName' : 'Abel', 'lastName' : 'Gonçalves'},
#     {'id' : 3, 'firstName' : 'Sofia', 'lastName' : 'Pereira'},
#     {'id' : 4, 'firstName' : 'Rui', 'lastName' : 'Rio'},
#     {'id' : 5, 'firstName' : 'Cavaco', 'lastName' : 'Luís'}
# ]
filename = "json/formandos.json"
listFormandos = loadJSONFile(filename)
listaMenus = ["1 - Listar formandos", "2 - Inserir formando", "3 - Sair"]
 
 
while True:
    op = beaupy.select(listaMenus, cursor="->", cursor_style='green', return_index=True)+1
    match op:
        case 1:
            print(listFormandos if listFormandos else "Não existem formandos adicionados!")
        case 2:
            listFormandos.append(addFormando())
            saveJSONFile("json/formandos.json", listFormandos)
        case 3:
            break
 
nextID(listFormandos)
 