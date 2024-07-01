#



#
def findWord(item):
    while True:
        word = input('Qual palavra deseja procurar? ( Insira 0 para sair)\n- ')
        if word == '0':
            print(f'A sair.....')
            break
        if word.casefold() in item.casefold():
            print(f'found the word - {word}')
        else:
            print(f'nao encontrei')

#
noticia = input(f'Insira um resumo de uma noticia:\n- ')
autor = input(f'Insira o nome do autor desta noticia:\n- ')

noticianLen = len(noticia)


findWord(noticia)