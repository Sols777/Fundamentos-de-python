# imports

import json , beaupy
from datetime import date , datetime


# helpers functions

def loadJSONFile(filename):
    try:
        with open(filename , 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("\nErro: ficheiro não encontrado!\n")
        return []
    except:
        print("\nErro !!!!!!!\n")
        return []
    else:
        return data
    
def saveJSONFile(filename, list):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(list, f, indent=4)
    except FileNotFoundError:
        print("\nErro: não foi possível gravar o ficheiro!\n")
    except:
        print("\nUps, deu erro!")
        
def nextID(list):
    ids = [ele['id'] for ele in list]
    if ids:
        return max(ids)+1
    else:
        return 1
    
def getItemID(list):
    op = int(beaupy.select(list, cursor="->", cursor_style='green', return_index=True))
    return list[op]['id']

def getCrianca(crianca_id):
    listCrianca = loadJSONFile("./listCrianca.json")
    for index , crianca in enumerate(listCrianca):
        if crianca['id'] == crianca_id:
            return crianca , index
    return None , None

def getPediatra(pediatra_id):
    listPediatra = loadJSONFile("./listpediatra.json")
    for index, pediatra in enumerate(listPediatra):
        if pediatra['id'] == pediatra_id:
            return pediatra , index
    return None , None

def getConsulta(consulta_id):
    listConsulta = loadJSONFile("./listConsulta.json")
    for index, consulta in enumerate(listConsulta):
        if consulta['id'] == consulta_id:
            return consulta , index
    return None , None

def calculateAge(dataNascimento):
    birthDate = datetime.strptime(dataNascimento, "%d/%m/%Y").date()
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) <
        (birthDate.month, birthDate.day)) 
    return age

# prints

def printCrianca(listCrianca):
    for crianca in listCrianca:
        print(f'''
                Nome: {crianca['primeiroNome']} {crianca['ultimoNome']}
                Idade: {calculateAge(crianca['dataNascimento'])} anos
            ''')
def printPediatra(listPediatra):
    for pediatra in listPediatra:
        print(f'''
            Nome: {pediatra['primeiroNome']} {pediatra['ultimoNome']}
            Salario: {pediatra['salario']}
        ''')

def printConsultas(listConsulta):
    for consulta in listConsulta:
        crianca , id = getCrianca(consulta['crianca_id'])
        pediatra , id = getPediatra(consulta['pediatra_id'])
        print(f'''
            Data: {consulta['data']}
            Crianca: {crianca['primeiroNome']} {crianca['ultimoNome']}
            Medico: {pediatra['primeiroNome']} {pediatra['ultimoNome']}
            Preco: {consulta['preco']} euros
        ''')
        
        