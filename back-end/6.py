#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]


"""

Para as versões de hoje em dia para esses casos de interar e alterar o valor com base no index da lista é
utilizado enumerate por conta que o enumerate é utilizado para retornar o index onde a interação está + o valor, dessa forma posso saber tranquilamente em qual
index o loop vai aplicar condições e etc.

No meu caso uso o valor que o enumerate me retorna no loop para então fazer a alteração dos indexes que possui o valor como "joao" e então altera-los 
para "maria".

Com enumerate, o código é mais legível e evita o uso de range();
"""


for i, nome in enumerate(lista): #enumerate(lista) retorna um par (índice, valor)
    if nome == "joao":
        
        # i representa o index, lista[i] = "maria" indica que é feito uma alteração na lista baseado no index, 
        # no caso temos o index de "joao" então trocamos o valor "joao" para "maria"
        lista[i] = "maria" 


print(lista)