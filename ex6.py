#variaveis
listaTele = []
# func
def Menu():
    while True:
        op =input('''
            Menu\n
            Deseja inserir um novo contacto?\n
            s - para continuar
            n - para sair
            ''')
        if op.lower() == 'n':
            'byeeeee'
            break
        if op.lower() == 's':
            nome = input(f'Introduza um nome para o contacto:\n- ')
            tele = input(f'Introduza o contacto:\n- ')
            temp= {
                'Nome' : nome,
                'Telefone' : tele
            }
            listaTele.append(temp)
        else:
            print('Erro!!!!!!!!')
#
def Menuask():
    while True:
        op = input(f"Escreva o nome da pessoa que deseja procurar ( n para sair)\n- ")
        if op.lower() == 'n':
            print('bye byeeeee')
            break
        else:
            for pessoa in listaTele:
                if op.lower() == pessoa['Nome'].lower():
                    print(f"A pessoa {pessoa['Nome']} existe ,  tem o contacto {pessoa['Telefone']}")
                else:
                    print(f'A pessoa com o nome {op} nao existe :(')

# ## input/calls
# menu contacto novo
Menu()
for pessoa in listaTele:
    print(f"{pessoa['Nome']} com o contacto {pessoa['Telefone']}")
#menu conttacto a procurar
Menuask()
 

