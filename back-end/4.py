#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

lista = ["   joao   ","   maria   ","  joana  "]

"""
Aqui optei em usar list comprehension novamente (como fiz na pergunta 1 (1.py)) só que nesse caso estou usando strip; 
O strip é o responsável por remover o espaço dos nomes, ele aceita argumentos mas o "espaço" é um argumento default então nem precisei especificar o "espaço";

resumidamente o strip() está sendo utilizado em cada valor da lista de string e removendo o "espaço"


Gostaria de ressaltar que é similar a se fazer um loop de maneira convencional no python só que  menos verboso e simples, é o que eu costumo usar em meus projetos.

"""

listaNova = [item.strip() for item in lista]

print(listaNova)