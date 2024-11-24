#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 

response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

print(f"Antes: {response}\n")

"""

No contexto da pergunta, o for loop abaixo filtra os produtos baseado no value de preço. Usei list comprehension pois para
mim é a maneira menos verbosa e simples que sei.
E mesmo que se a loja não tiver nenhum produto o código vai funcionar corretamente pois eu lido com a ausencia de 
chaves e valores usando .get() do python.

"""

# for loop vai percorrendo todas as lojas da response.
for shop in response:
    produtos = shop.get('produtos', []) # e então obtem a lista de produtos da loja que está no loop.

    """
    e é usado list comprehension que para mim é uma forma mais simples de percorrer os produtos em uma lista
    juntamente com um uso de uma condicional if (para fins de comparação de preço) focado em retornar apenas produtos que o preço seja menor do que 30.
    """
    shop["produtos"] = [produto for produto in produtos if produto.get("preço", 0) < 30] 

print(f"Depois: {response}")