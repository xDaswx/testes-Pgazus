#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]

"""
Utilizei pop() nessa pergunta pois é uma função nativa das listas, onde enviamos o index do item que queremos remover como argumento;
e então o item é removido e pode ser acessível na variavel referenciada.
"""


removed = lista.pop(1) # pop() recebe 1 como argumento pois 1 é o index do segundo item da lista.

print(lista) # imprime a lista com a alteração do pop em tipo list.

print(removed) # imprime o valor removido da lista, como o valor removido é um inteiro/number o tipo da varíavel removed vai ser int.