import json, beaupy
#
def loadJSONFile(filename):
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
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(list, f, indent=4)
    except FileNotFoundError:
        print("\nErro: não foi possível gravar o ficheiro!\n")
    except:
        print("\nUps, something wrong happened!")
 
def nextID(listCaros):
    ids = [carro['id'] for carro in listCaros]
    if ids:
        return max(ids)+1
    else:
        return 1

def addCar():
    print("\nAdicionar Carro: \n")
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    preco = input("Preco: ")
    cor = input("Cor: ")
    id = nextID(listCaros)
    return {'id' : id, 'modelo' : modelo, 'marca' : marca, 'preco': preco, 'cor': cor}
 
def findCar():
    print("\nProcurar Carro: \n")
    while True:
        op = beaupy.select(menuPesquisa, cursor="->", cursor_style='green', return_index=True)+1
        match op:
            case 1:
                cor = input("Cor a pesquisar: ")
                carCor = [ car for car in listCaros if car['cor']== cor]
                print( carCor if carCor else "Não existem carros dessa cor!")
            case 2:
                marca = input("Marca a pesquisar: ")
                carMarca = [ car for car in listCaros if car['marca']== marca]
                print(carMarca if carMarca else "Não existem dessa marca!")
            case 3:
                precoMin = min(car['preco'] for car in listCaros)
                carMin = [car for car in listCaros if car['preco'] == precoMin]
                print(carMin if carMin  else "Não existem carros adicionados!")
            case 4:
                precoMax = max(car['preco'] for car in listCaros)
                carMax = [car for car in listCaros if car['preco'] == precoMax]
                print(carMax if carMax else "Não existem carros adicionados!")
            case 5:
                break
            case _:
                print('Erro , try again!')
                break
            
def multiFind():
    print("\nProcura avancada: \n")
    while True:
        op = [beaupy.select_multiple(menuPesquisa, tick_character ="->", tick_style ='green', return_indices= True)+1]
        match op:
            case 1:
                print('1 test')
            case 2:
                print('2 test')
            case 3:
                print('3 test')
            case 4:
                print('4 test')
            case 5:
                break
            case 6:
                print('Erro!!!!!!!!!!!')
                break
#####

filename = "ex23_.json"
listCaros = loadJSONFile(filename)
listaMenus = ["1 - Listar   Carros", "2 - Inserir Carro", "3 - Pesquisa" , "4 - Pesquisa Avancada(test)" , "5 - Sair"]
menuPesquisa= ["1 - Por cor", "2 - Marca", "3 - Preco Min" , "4 - Preco Max" , "5 - Sair"]
 
while True:
    op = beaupy.select(listaMenus, cursor="->", cursor_style='green', return_index=True)+1
    match op:
        case 1:
            print(listCaros if listCaros else "Não existem carros adicionados!")
        case 2:
            listCaros.append(addCar())
            saveJSONFile(filename, listCaros)
        case 3:
            findCar()
            saveJSONFile(filename, listCaros)
        case 4:
            multiFind()
            saveJSONFile(filename, listCaros)
        case 5:
            break
 
# nextID(listCaros)
 