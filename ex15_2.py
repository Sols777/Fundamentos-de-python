list_a = (1 , 2 , 3 , 4)
list_b = (2 , 3 , 4 , 5)

list_ab = [val for val in list_a if  val in list_b]
print(list_ab)

texto = "O IPO do Porto está na primeira linha na participação em projetos europeus relacionados com o Plano Europeu de Luta Contra o Cancro Estamos envolvidos em mais de uma dezena de projetos e estudos, a maior parte deles na área da investigação em oncologia Mas alguns deles estão relacionados"
list_text = [val for val in texto.split() if len(val) <= 4]

print(list_text)
print(list(set(list_text)))