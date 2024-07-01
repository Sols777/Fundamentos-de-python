import csv , beaupy

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


def saveCSVFile(filename, listVal):
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
    
    
def addPerson():
    print("\nAdicionar Carro: \n")
    bi = input("Bi: ")
    nome = input("Nome: ")
    idade = input("Idade: ")
    id = nextID(listPessoas)
    return {'id' : id, 'bi' : bi, 'nome' : nome, 'idade': idade}


def nextID(listPessoas):
    ids = [pessoa['id'] for pessoa in listPessoas]
    if ids:
        return max(ids)+1
    else:
        return 1
    
    

#
filename = None
data =  None
listPessoas = loadCSVFile(filename)
listaMenus = ["1 - Criar lista", "2 - Preencher lista", "3 - Mostrar lista" , "4 - Sair"]

# Menu 
while True:
    op = beaupy.select(listaMenus, cursor="->", cursor_style='green', return_index=True)+1
    match op:
        case 1:
            filename= input('Filename:\n- ')
            if not filename.endswith('.csv'):
                filename += '.csv'
            saveCSVFile(filename , data)
        case 2:
            listPessoas.append(addPerson())
            saveCSVFile(filename , listPessoas)
        case 3:
            print(listPessoas if listPessoas else "Não existem pessoas adicionadas!")
        case 4:
            break
        case _:
            print('eRRO !!!!!!!!!')