######## MAIN APP
### imports
import json , beaupy
from helpers import *


##### VARIES GLOBAIS
pediatrafilename = "./listpediatra.json"
criacafilename = "./listCrianca.json"
consultafilename = "./listConsulta.json"
# loads
listPediatra = loadJSONFile(pediatrafilename)
listCrianca = loadJSONFile(criacafilename)
listConsulta = loadJSONFile(consultafilename)
## menus
# inserir
listaInsert = ["1 - Inserir Pediatras", "2 - Inserir crianca", "3 - Criar consulta", "4 - Voltar atras"]
# pesquisa
listaPesquisa = ["1 - Procurar todos os Pediatras", "2 - Procurar todas as criancas", "3 - Procurar todas consultas", "4 - Pesquisa avancada","5 - Voltar atras"]
# pesquisa Avancada
listaPesquisaAvancada = ["1 - Procurar por data(dd/mm/yyyy)", "2 - Total faturado entre datas", "3 - Histórico de consultas de uma criança", "4 - Voltar atras"]
#Edicao
listaEdicao = ["1 - Editar Pediatra", "2 - Editar crianca", "3 - Editar consulta", "4 - Voltar atras"]
# Main menu
listaMenu = ["1 - Inserir dados", "2 - Pesquisar dados", "3 - Editar dados", "4 - Sair"]
####FUNCTIONS MAIN
# ADD FUNCTIONS
# Pediatras
def addMedico():
    print("\nAdicionar Pediatra: \n")
    primeiroNome = input("Insira o primeiro nome: ")
    ultimoNome = input("Insira o ultimo nome: ")
    salario = input("Insira o Salario: ")
    id = nextID(listPediatra)
    return {'id' : id, 'primeiroNome' : primeiroNome, 'ultimoNome' : ultimoNome, 'salario': salario}
# Criancas
def addCrianca():
    print("\nAdicionar Crianca: \n")
    primeiroNome = input("Insira o primeiro nome: ")
    ultimoNome = input("Insira o ultimo nome: ")
    dataNascimento = input("Insira a data nascimento: ")
    id = nextID(listCrianca)
    return {'id' : id, 'primeiroNome' : primeiroNome, 'ultimoNome' : ultimoNome, 'dataNascimento': dataNascimento}
# Consultas
def addConsulta():
    print("\nNova Consulta: \n")
    data = input("Insira a data: ")
    crianca_id = getItemID(listCrianca)
    pediatra_id = getItemID(listPediatra)
    preco = input("Insira o valor: ")
    id = nextID(listConsulta)
    return {'id' : id, 'data' : data, 'crianca_id' : crianca_id, 'pediatra_id': pediatra_id , 'preco': preco}
# SEARCH FUNCTIONS
#by date
def findByDate(data):
    find = [ consulta for consulta in listConsulta if consulta['data'] == data]
    if find:
        printConsultas(find)
    else:
        print('Nao existe consultas para essa data!')
# faturado entre dates
def findFaturado(date1,date2):
    if not date1 or not date2:
        print("Both dates must be provided")
        return 0
    date_format = "%d/%m/%Y"
    start_date = datetime.strptime(date1, date_format)
    end_date = datetime.strptime(date2, date_format)
    total_faturado = 0
    hoje = datetime.today()
    if end_date > hoje:
        end_date = hoje
        print(f'Insiriu uma data superior a de hoje , data de fim sera a de hoje - {date.today()}')
    for consulta in listConsulta:
        consulta_data = datetime.strptime(consulta["data"], date_format)
        if start_date <= consulta_data <= end_date:
            total_faturado += int(consulta["preco"])
    if total_faturado > 0 :
        print(f"Total faturado entre {date1} e {date2}: {total_faturado} euros")
    else:
        print('Nada faturado entre essas datas!')
# historia crianca por nome
def findCrianca():
    crianca_id = getItemID(listCrianca)
    find = [ consultas for consultas in listConsulta if consultas['crianca_id'] == crianca_id]
    if find:
        printConsultas(find)
    else:
        print('Nao existe consultas para essa crianca!')
# getting pediatra com id        

    return None
# edit pediatra especifico com id
def editPediatra(pediatra_id):
    pediatra , index = getPediatra(pediatra_id)
    print("\nEditar Pediatra: \n")
    print(f"A editar pediatra {pediatra['primeiroNome']} {pediatra['ultimoNome']}")
    edit_primeiroNome = input("[A EDITAR]Insira o novo primeiro nome (deixar em branco se nao pretende alterar): ")
    edit_ultimoNome = input("[A EDITAR]Insira o novo ultimo nome (deixar em branco se nao pretende alterar): ")
    edit_salario = input("[A EDITAR]Insira o novo Salario (deixar em branco se nao pretende alterar): ")
    # checkar se tem valores novos
    pediatra['primeiroNome'] = edit_primeiroNome if edit_primeiroNome else  pediatra['primeiroNome'] 
    pediatra['ultimoNome'] = edit_ultimoNome if edit_ultimoNome else pediatra['ultimoNome']
    pediatra['salario'] = edit_salario if edit_salario else pediatra['salario']
    # save na file
    listPediatra[index] = pediatra
    saveJSONFile(pediatrafilename, listPediatra)
            
def editCrianca(crianca_id):
    crianca , index = getCrianca(crianca_id)
    print("\nEditar crianca: \n")
    print(f"A editar crianca {crianca['primeiroNome']} {crianca['ultimoNome']}")
    edit_primeiroNome = input("[A EDITAR]Insira o novo primeiro nome (deixar em branco se nao pretende alterar): ")
    edit_ultimoNome = input("[A EDITAR]Insira o novo ultimo nome (deixar em branco se nao pretende alterar): ")
    edit_dataNascimento = input("[A EDITAR]Insira a nova data de nascimento(dd/mm/yyyy) (deixar em branco se nao pretende alterar): ")
    
    # checkar se tem valores novos
    crianca['primeiroNome'] = edit_primeiroNome if edit_primeiroNome else  crianca['primeiroNome'] 
    crianca['ultimoNome'] = edit_ultimoNome if edit_ultimoNome else crianca['ultimoNome']
    crianca['dataNascimento'] = edit_dataNascimento if edit_dataNascimento else crianca['dataNascimento']
    # save na file
    listCrianca[index] = crianca
    saveJSONFile(criacafilename, listCrianca)
    
def editConsulta(consulta_id):
    consulta , index = getConsulta(consulta_id)
    print("\nEditar consulta: \n")
    print(consulta)
    edit_pediatra = getItemID(listPediatra)
    edit_data = input("[A EDITAR]Insira a nova data(dd/mm/yyyy) (deixar em branco se nao pretende alterar): ")
    edit_preco = input("[A EDITAR]Insira o novo preco (deixar em branco se nao pretende alterar): ")
    
    # checkar se tem valores novos
    consulta['pediatra_id'] = edit_pediatra if edit_pediatra else  consulta['pediatra_id'] 
    consulta['data'] = edit_data if edit_data else consulta['data']
    consulta['preco'] = edit_preco if edit_preco else consulta['preco']
    # save na file
    listConsulta[index] = consulta
    saveJSONFile(consultafilename, listConsulta)
# FUNC MENUS 
# Menu inserir
def menuInsert():
    while True:
        op = beaupy.select(listaInsert, cursor="->", cursor_style='green', return_index=True)+1
        match op:
            case 1: # Pediatra
                listPediatra.append(addMedico())
                saveJSONFile(pediatrafilename, listPediatra)
            case 2: #crianca
                listCrianca.append(addCrianca())
                saveJSONFile(criacafilename, listCrianca)
            case 3: # Consulta
                listConsulta.append(addConsulta())
                saveJSONFile(consultafilename, listConsulta)
            case 4:
                break
            case _:
                print('Deu erro ! Tenta outra vez!!')
# Menu pesquisa
def menuPesquisaAvancada():
    while True:
        op = beaupy.select(listaPesquisaAvancada, cursor="->", cursor_style='green', return_index=True)+1
        match op:
            case 1: # por data
                findByDate(input('Data: '))
            case 2: # faturado entra data
                findFaturado(input('Data comeco: '), input('Data fim: '))
            case 3: # historico nome crianca
                findCrianca()
            case 4: # saIR
                break
            case _:
                print('Deu erro ! Tenta outra vez!!')

def menuPesquisa():
    while True:
        op = beaupy.select(listaPesquisa, cursor="->", cursor_style='green', return_index=True)+1
        match op:
            case 1: # todos Pediatra
                print('\nPediatras: \n')
                printPediatra(listPediatra) if listPediatra else print("Não existem pediatra adicionados!")
            case 2: # todas crianca
                print('\nCriacas: \n')
                printCrianca(listCrianca) if listCrianca else print("Não existem criancas adicionadas!")
            case 3: # todas Consulta
                print('\nConsultas: \n')
                printConsultas(listConsulta) if listConsulta else print("Não existem consultas adicionadas!")
            case 4: # pesquisa avancada
                menuPesquisaAvancada()
            case 5: # saIR
                break
            case _:
                print('Deu erro ! Tenta outra vez!!')
# Menu edicao        
def menuEdicao():
    while True:
        op = beaupy.select(listaEdicao, cursor="->", cursor_style='green', return_index=True)+1
        match op:
            case 1: # Pediatra
                pediatra_id = getItemID(listPediatra)
                editPediatra(pediatra_id)
            case 2: #crianca
                crianca_id = getItemID(listCrianca)
                editCrianca(crianca_id)
            case 3: # consulta
                consulta_id = getItemID(listConsulta)
                editConsulta(consulta_id)
            case 4: # sair
                break
            case _:
                print('Deu erro ! Tenta outra vez!!')  

# MAIN MENU

def menu():
    while True:
        op = beaupy.select(listaMenu, cursor="->", cursor_style='green', return_index=True)+1
        match op:
            case 1: # Inserir novo
                menuInsert()
            case 2: #procurar
                menuPesquisa()
            case 3: # editar
                menuEdicao()
            case 4:
                break
            case _:
                print('Deu erro ! Tenta outra vez!!')
###CALL functions

menu()