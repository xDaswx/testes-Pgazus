#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO


"""
Aqui tem uma breve representação da metodologia fifo em uma list do python.

fifoLista.append(1) é a adição do item na list.
fifoLista.pop(0) pop() com o argumento 0 indica que o item de index 0 (primeiro item, no caso o item 1) será removido
"""

fifoLista = []
fifoLista.append(1) # primeiro item adicionado
fifoLista.append(2) # segundo item adicionado
fifoLista.append(3) # terceiro item adicionado


print("Fifo", fifoLista)


# primeiro item será sendo removido da lista, pois ele foi o primeiro a entrar e então vai ser o ultimo a sair
fifoLista.pop(0)
print("Fifo pop(0)", fifoLista)

