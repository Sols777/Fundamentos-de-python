# [4:03 PM] Pedro Mendonça - FORMADOR PRT
import json
 
# HelperFunctions
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
 
 
 
# functions
def addCar():
    # matricula, modelo, marca, preco, cor
    print("\nAdicionar automóvel:\n")
    matricula = input("Matricula: ")
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    cor = input("Cor: ")
    preco = eval(input("Preço: "))
    return {'matricula' : matricula, 'modelo' : modelo, 'marca' : marca, 'cor' : cor, 'preco' : preco}
 
 
def addCars(carList, filename):
    while True:
        op = input("Deseja introduzir mais automóveis? (s/n) ")
        if op.lower() == "s":
            carList.append(addCar())
            saveJSONFile(filename, carList)
        elif op.lower() == "n":
            break
        else:
            print("\nErro: deverá introduzir s ou n!\n")
 
def printAutomovel(automovel):
    print(f'''
          Matricula: {automovel['matricula']}
          Modelo: {automovel['modelo']}
          Marca: {automovel['marca']}
          Preço: {automovel['preco']}€
          Cor: {automovel['cor']}
          ''')
 
def printAutomoveis(listAutomoveis, msg):
    print(msg)
    if len(listAutomoveis)>0:
        for automovel in listAutomoveis:
            printAutomovel(automovel)
    else:
        print("\nErro: Ainda não foram adicionados automóveis\n")
 
def searchCars(carList, **kwargs):
    cor = kwargs.get("cor", None)
    precoMin = kwargs.get("precoMin", None)
    precoMax = kwargs.get("precoMax", None)
   
    if cor and precoMin and precoMax:
        searchList = [car for car in carList if precoMin <= car['preco'] <= precoMax and car["cor"].lower() == cor.lower()]
        printAutomoveis(searchList, f'Listagem de Automóveis cujo preço está no intervalo [{precoMin}:{precoMax}] e com a cor {cor}: ')
    elif cor:
        searchList = [car for car in carList if car["cor"].lower() == cor.lower()]
        printAutomoveis(searchList, f'Listagem de Automóveis cuja cor é {cor}: ')
    elif precoMin and precoMax:
        searchList = [car for car in carList if precoMin <= car['preco'] <= precoMax]
        printAutomoveis(searchList, f'Listagem de Automóveis cujo preço está no intervalo [{precoMin}:{precoMax}]: ')
 
# globals
filename = "ex23_.json"
 
# Importa do ficheiro ex_23.json todos os automóveis registados
carList = loadJSONFile(filename)
addCars(carList, filename)
#searchCars(carList, cor="Preto")
#searchCars(carList, precoMin=eval(input("Preço mínimo: ")), precoMax=eval(input("Preço máximo: ")))
searchCars(carList, cor="Preto", precoMin=eval(input("Preço mínimo: ")), precoMax=eval(input("Preço máximo: ")))