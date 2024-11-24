#11-crie uma lista e adicione um item novo a ela utilizando a metodolofia LIFO

"""
A diferença entre o fifoList e lifoLista é apenas a maneira que o pop() vai atuar.

lifoLista.append(1) é a adição do item na list.
lifoLista.pop() pop() sem argumento indica que o ultimo item da lista será removido
"""

lifoLista = []
lifoLista.append(1) # primeiro item adicionado
lifoLista.append(2) # segundo item adicionado
lifoLista.append(3) # terceiro item adicionado


print("Lifo", lifoLista)


# o ultimo item será removido da lista
lifoLista.pop()
print("Lifo pop()", lifoLista)
