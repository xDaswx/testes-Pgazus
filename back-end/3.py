#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]


"""

Dependendo da versão do python o algoritmo de sort se altera.
Na versão que utilizo, o atual algoritmo é o timsort (estou usando 3.8.7).
O Python já usa timsort em sorted() e sort(), então utilizo essas funções nativas

o timsort (nativo do python) é melhor nesse caso por causa que uma parte dos numeros da lista já está ordernada.

diferença entre sorted() e sort(): o sorted() cria uma copia da lista, o sort() ordena a lista em si (sem cópia)

"""


#timsort para python 3.1 +
lista.sort()

print("nativo(timsort)", lista)

"""
Aqui abaixo é o bubbleSort, é um algoritmo bem simples mas ao meu ver o algoritmo atual do python é o mais recomendado.
ele funciona comparando o item anterior e então vai subindo o maior numero para o topo
"""
def bubbleSort(lista: list):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1): 
            if lista[j] > lista[j + 1]:  
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  
    return lista


listaSorted = bubbleSort(lista)


print("bubbleSort", listaSorted)