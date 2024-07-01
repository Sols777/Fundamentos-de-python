#variaveis
formandos = []
# func
def values():
    temp1= {
            'Nome' : "Luis",
            'Sexo' : "Masc",
            'Localidade' : "Porto",
            'Curso' : "Data"   
        }
    temp2= {
            'Nome' : "Ola",
            'Sexo' : "Fem",
            'Localidade' : "Lisboa",
            'Curso' : "Python" 
            }
    temp3= {
        'Nome' : "Manuel",
        'Sexo' : "Masc",
        'Localidade' : "Aveiro",
        'Curso' : "Data" 
        }
    return temp1, temp2 , temp3

def Registo():
    for formando in values():
        formandos.append(formando)
        
def printFormando(list):
    for formando in list:
        if formando:
            print(f"\nInfo Formando:\n")
            print(f"Nome: {formando['Nome']}")
            print(f"Sexo: {formando['Sexo']}")
            print(f"Localidade: {formando['Localidade']}")
            print(f"Curso: {formando['Curso']}")

def numFormandos(list):
    count = 0
    if list:
        print(f'\nNum de formandos: {len(list)}\n')
        for formando in list:
            if formando['Curso'].lower() == 'Python'.lower():
                count +=1
                print(f'Num de alunos no curso de Python: {count}')
            

#      
Registo()        
printFormando(formandos)
numFormandos(formandos)