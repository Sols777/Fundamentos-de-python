import json , csv
# # ternerary operator / one liner 
# val = 15
# <10 negativa 10 e 15 positiva > 15 bom
# print("Negativa" if val<10 else "Positiva" if val < 16 else "Bom")

# # tuples
# from random import randint

# def generateRandomTuple():
#     temp = ()
#     for _ in range(5):
#         temp += (randint(1,100),)
#     return temp

# tupla = generateRandomTuple()
# print(f"Máximo: {max(tupla)}")
# print(f"Mínimo: {min(tupla)}")
# [Friday 2:17 PM] Pedro Mendonça - FORMADOR PRT
# # tuplos
# tuplo = (3, "Palavra", True) # listas = [ele, dfgdfg]
# #print(type(tuplo))
# tuplo2 = ("5",) # minimo 2 valores
# #print(type(tuplo2))
 
# print(tuplo[0]) # primeiro
# print(tuplo[-1]) # último
 
# #tuplo[0] = 5 # erro!!!
# #tuplo.append("dsfgdfg") # erro
# def qqcoisa():
#     return 1,2
 
# print(type(qqcoisa()))
# [Friday 2:23 PM] Pedro Mendonça - FORMADOR PRT
# tuplo = (3, "Palavra", True) # listas = [ele, dfgdfg]
# tuplo = tuplo + ("Lucas",)
# print(tuplo)
 
# tuplo2 = (7,2,6,3,8,5)
# tuplo2 = sorted(tuplo2)
# print(tuplo2[0:2])
# [Friday 2:37 PM] Pedro Mendonça - FORMADOR PRT
# myTuple = ('João', 'Artur', 'Sofia', 'Rui', 'Mónica')
 
# while True:
#     try:
#         numAluno = int(input(f"Indique o número do aluno [1-{len(myTuple)}]: "))
#     except:
#         print("\nErro: introduza um valor inteiro!!\n")
#     else:
#         if 1 <= numAluno <= len(myTuple):
#             print(myTuple[numAluno-1])
#             break
#         else:
#             print("\nErro: aluno fora do intervalo!\n")
# [Friday 3:55 PM] Pedro Mendonça - FORMADOR PRT
# moedasNotas = (50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01) # 123.23
# quantia = eval(input("Indique uma quantia: "))
 
# for val in moedasNotas: # 50
#     count = 0
#     while quantia >= val: # 123.23 > 50
#         count += 1
#         quantia -= val
#     if count:
#         if val>2:
#             print(f"Nota: {val}€: {count}")
#         else:
#             print(f"Moeda: {val}€: {count}")
# [Friday 3:59 PM] Pedro Mendonça - FORMADOR PRT
# lista = [3,4,5,1,2,3,7,4,8]
# listaNaoRepetidos = list(set(lista))
# print(listaNaoRepetidos)
# [Friday 4:11 PM] Pedro Mendonça - FORMADOR PRT
 
# # dicionários de dados
# animal = {
# #     key      value
#     "tipo" : "cão",
#     "raca" : "rafeiro",
#     "peso" : 12.23
# }
 
# print(animal['tipo'])
 
# if "comprimento" not in animal:
#     animal["comprimento"] = 1.45
 
# if "tipo" not in animal:
#     animal["tipo"] = "Macaco" # replace se existir
 
# print(animal)
 
# for key in animal:
#     print(f"{key}: {animal[key]}")
# [Friday 4:14 PM] Pedro Mendonça - FORMADOR PRT
# # dicionários de dados
# animal = {
# #     key      value
#     "tipo" : "cão",
#     "raca" : "rafeiro",
#     "peso" : 12.23
# }
 
# listKeys = list(animal.keys())
 
# for key in animal.keys():
#     print(key)
 
# for val in animal.values():
#     print(val)
# [Friday 4:18 PM] Pedro Mendonça - FORMADOR PRT
# # dicionários de dados
# animal = {
# #     key      value
#     "tipo" : "cão",
#     "raca" : "rafeiro",
#     "peso" : 12.23,
#     "hobbies" : ["Roer", "Estragar", "Comer", "Lamber", "Perder Pêlo"]
# }
 
# animal["hobbies"].append("Passear")
# print(animal["hobbies"][0])
# [Friday 4:24 PM] Pedro Mendonça - FORMADOR PRT
# DAX
# [Friday 4:30 PM] Pedro Mendonça - FORMADOR PRT
 
# obj1 = {
#     "nome" : "Máquina de cortar cabelo",
#     "funcionalidade" : "Cortar cabelo para quem o tem",
#     "preco" : 123.11,
#     "peso" : 0.987,
#     "cheiro" : "Mal"
# }
# obj2 = {
#     "nome" : "Aspirador",
#     "funcionalidade" : "Aspira até as meias dos garotos",
#     "preco" : 49.99,
#     "peso" : 6.23
# }
 
# listaObjetos = []
# listaObjetos.append(obj1)
# listaObjetos.append(obj2)
# print(listaObjetos[0]['preco'])
 
# for obj in listaObjetos:
#     if obj['preco'] >= 100:
#         print(obj)
# [Friday 4:32 PM] Pedro Mendonça - FORMADOR PRT
# O sr manel tem a mania de analisar as propriedades das cenouras. Identifica 3 propriedades e cria
# 3 cenouras utilizando inputs. Estas devem ser adicionadas a uma lista.
# No final deverão ser impressas todas as cenouras e a cenoura maior (em comprimento)
# [Friday 5:01 PM] Pedro Mendonça - FORMADOR PRT
# """
# O sr manel tem a mania de analisar as propriedades das cenouras. Identifica 3 propriedades e cria
# 3 cenouras utilizando inputs. Estas devem ser adicionadas a uma lista.
# No final deverão ser impressas todas as cenouras e a cenoura maior (em comprimento)
# """
# def addProduct():
#     comprimento = eval(input("Comprimento: "))
#     peso = eval(input("Peso: "))
#     cor = input("Cor: ")
#     return {
#         "comprimento" : comprimento,
#         "peso" : peso,
#         "cor" : cor
#     }
 
# def fillProducts(listProducts):
#     print("\nInserir 3 produtos\n")
#     for _ in range(3):
#         listProducts.append(addProduct())
 
# def printProduct(product):
#     print(f"""
#     Dados do produto:
#     Comprimento -> {product['comprimento']}
#     Peso -> {product['peso']} Cor -> {product['cor']}
#     """)
 
# def printProducts(listProducts):
#     print("\nListagem de produtos\n")
#     if(listProducts):
#         for product in listProducts:
#             printProduct(product)
#     else:
#         print("\nNão foram encontrados produtos!\n")
 
# def getBiggestProduct(listProducts):
#     print("Produto maior:")
#     if(listProducts):
#         biggestProduct = listProducts[0].copy()
#         for product in listProducts:
#             if product['comprimento'] > biggestProduct['comprimento']:
#                 biggestProduct = product.copy()
       
#         printProduct(biggestProduct)
#     else:
#         print("\nNão foram encontrados produtos!\n")
 
# listProducts = []
# fillProducts(listProducts)
# printProducts(listProducts)
# print("*" * 100)
# getBiggestProduct(listProducts)

# [10:10 AM] Pedro Mendonça - FORMADOR PRT
# def addNewContact():
#     print("\nNovo contacto\n")
#     name = input("Nome: ")
#     phone = int(input("Telefone: "))
#     return {'name' : name, 'phone' : phone}
 
# def printContact(contact):
#     print(f"Nome: {contact['name']} Telefone: {contact['phone']}")
 
# def printAllContacts(contactList):
#     print("Listagem de contactos: ")
#     if contactList:
#         for contact in contactList:
#             printContact(contact)
#     else:
#         print("\nNão existem contactos adicionados!\n")
 
# def searchContact(name):
#     print(f"Pesquisa de contactos de pessoas com o nome {name}: ")
#     if contactList:
#         count = 0
#         for contact in contactList:
#             if contact['name'].lower() == name.lower():
#                 printContact(contact)
#                 count+=1
#         else:
#             if not count: # if count == 0
#                 print("\nNão foram encontrados contactos com o perfil indicado!\n")
#     else:
#         print("\nNão existem contactos adicionados!\n")    
 
# def main():
#     while True:
#         op = input("Deseja inserir mais contactos? s/n: ")
#         if op.lower() == "s":
#             contactList.append(addNewContact())
#         elif op.lower() == "n":
#             printAllContacts(contactList)
#             if contactList:
#                 searchContact(input("Nome a pesquisar: "))
#             break
#         else:
#             print("\nErro: opção inválida!\n")
 
# contactList = []
# main()
# def soma(*args): # multiplos argumentos
#     print(type(args))
#     for item in args:
#         print(item)
 
# print(soma(3,4,4,5,6,7,8,9,9))


# def soma(n1, n2=3): # valores por defeito
#     return n1+n2
 
# print(soma(2))
# print(soma(2,7))

# def multiplos(**kwargs):
#     for item in kwargs:
#         print(item, kwargs[item])
 
# multiplos(idade=3, nome = "Maria", cachorro = None)

# dicionarios e kwargs

# [9:41 AM] Pedro Mendonça - FORMADOR PRT
# import beaupy
 
# # schema
# # brand: id brand
# # model: id brand_id model
# def fillInitialBrand():
#     temp = []
#     temp.append({'id' : 1, 'brand' : 'Renault'})
#     temp.append({'id' : 2, 'brand' : 'Peugeot'})
#     temp.append({'id' : 3, 'brand' : 'Audi'})
#     temp.append({'id' : 4, 'brand' : 'Mercedes'})
#     return temp
 
# def fillInitialModels():
#     temp = []
#     temp.append({'id' : 1, 'brand_id' : 1, 'model' : 'clio'})
#     temp.append({'id' : 2, 'brand_id' : 2, 'model' : '3008'})
#     temp.append({'id' : 3, 'brand_id' : 3, 'model' : 'A3'})
#     temp.append({'id' : 4, 'brand_id' : 4, 'model' : 'GLA'})
#     temp.append({'id' : 5, 'brand_id' : 1, 'model' : 'Kaptur'})
#     temp.append({'id' : 6, 'brand_id' : 2, 'model' : '308'})
#     temp.append({'id' : 7, 'brand_id' : 3, 'model' : 'R8'})
#     return temp
 
 
 
# def printAllModelsFromBrand(brand_id):
#     print("Listagem de modelos:")
#     count = 0
#     for model in modelList:
#         if model['brand_id'] == brand_id:
#             print(model['model'])
#             count+=1
#     else:
#         if not count:
#             print("\nNão foram encontrados modelos da marca selecionada\n")
#     print()
 
 
# # def showBrands(brandList, showModels = False):
# #     print("\nListagem de marcas:\n")
# #     if brandList:
# #         for brand in brandList:
# #             print(f"{brand['brand']}")
# #             if showModels:
# #                 print("Modelos")
# #     else:
# #         print("Ainda não foram adicionadas marcas")
 
# def showBrands(brandList, **kwargs):
#     showModels = kwargs.get('showModels', False)
#     print("\nListagem de marcas:\n")
#     if brandList:
#         for brand in brandList:
#             print(f"{brand['brand']}")
#             if showModels:
#                 printAllModelsFromBrand(brand['id'])
#     else:
#         print("Ainda não foram adicionadas marcas")
 
# def searchModelFromBrand(brandList, modelList):
#     print("\nSelecione a marca desejada:\n")
#     menuBrandList = [brand['brand'] for brand in brandList]
#     op = beaupy.select(menuBrandList, cursor="->", cursor_style='green', return_index=True) # returns index
#     #print(brandList[op]['id'])
#     printAllModelsFromBrand(brandList[op]['id'])
   
 
# brandList = fillInitialBrand()
# modelList = fillInitialModels()
# # Listar todas as marcas
# # listar todas as marcas E respetivos modelos
# #showBrands(brandList)
# #print("*" * 100)
# #showBrands(brandList, showModels=True)
# # Listar todos os modelos de uma marca selecionada
# searchModelFromBrand(brandList, modelList)
# #op = beaupy.select(menuList, cursor="->", cursor_style='green', return_index=True)


# list compreehension
# [10:06 AM] Pedro Mendonça - FORMADOR PRT
# fruits = ["Pera", "Banana", "Maracujá", "Manga", "Kiwi"]
 
# listFruitsA = []
# for fruit in fruits:
#     if "a" in fruit.lower():
#         listFruitsA.append(fruit)
 
# print(listFruitsA)
 
# listFruitsA2 = [fruit for fruit in fruits if "a" in fruit.lower()]
# print(listFruitsA2)

########
# CSV'S stuff
with open('./exemplos.csv' , 'r') as f:
    # reader = list(csv.reader(f))
    reader = list(csv.DictReader(f))
    print(reader)