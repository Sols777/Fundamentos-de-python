# def campeaoMundo(pais , *args):
#     temp = {}
#     nome = pais
#     campeonatos = args
#     temp = {'nome': nome , 'campeonatos' : campeonatos}
#     return temp
    

# print(campeaoMundo('Espanha',2010,2011))

def campeaoMundo(pais, *args):
    if not args:
        print(f"{pais} conquistou 0 títulos.")
    else:
        print(f"{pais} conquistou títulos no(s) ano(s): ", end='')
        for item in args:
            print(f"{item}", end=' ')
        print()
 
campeaoMundo("Espanha", 2010)
campeaoMundo("Portugal")
campeaoMundo("Argentina", 1978, 1986)
campeaoMundo("Brasil", 1958, 1962, 1970, 1994, 2002)