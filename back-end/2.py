#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}



"""
Aqui decidi criar uma função para localizar o produto. Como na pergunta #1 usei um loop for para percorrer a lista de produtos na chave produtos e 
novamente utilizei .get() para garantir que o código não quebre.
se um produto com o nome fornecido for encontrado, ele é retornado.
"""

def localizarProduto(produtoName: str):
    # for loop vai percorrendo os produtos de responsejson (variavel já definida)
    for produto in responsejson.get("produtos", []):
        # achou o produto baseado no nome então retorna ele
        if produto.get("nome") == produtoName:
            return produto

produto = localizarProduto("Produto B")


# condicional foi usada para verificar se o produto foi encontrado ou não 
if produto:
    print(f"Preço do produto: {produto.get('preço', None)}R$")
else:
    print("Produto não encontrado.")