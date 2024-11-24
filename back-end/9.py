#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra


import requests


"""

Aqui é demostrado quase a mesma coisa que é feita na pergunta passada (#8)
A diferença é que apenas faço um parse simples e armazeno os dados em usersParsedMapping que é uma lista vazia
Se não tiver usuários ou se acontecer algum erro no fetch a função retorna um array vazio.

"""


def getUsersParsed():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    usersParsedMapping = [] # se por acaso tudo ocorrer bem, essa list vai ter valores parseados do tipo dict 

    if response.status_code == 200: 
        users = response.json()
        
        for user in users:
            rua = user.get("address") # armazenando o dicionario/json do loop do momento aqui a fim de deixar o código mais légivel.
            #append faz a adição do user parseado para usersParsedMapping
            
            usersParsedMapping.append({
                "nome": user.get("name"),
                "username": user.get("username"),
                "email": user.get("email"),
                "rua": rua.get("street"),
                "numero": rua.get("suite") # considerei utilizar o numero da residência 
            })
            

        return usersParsedMapping 
    else:
        print(f"Error, status:{response.status_code} response:{response.text}")
        return usersParsedMapping

usersParsed = getUsersParsed()
print(usersParsed)