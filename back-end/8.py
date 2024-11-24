#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra


import requests

"""

Aqui faço uma demonstração simples de como é possível realizar um fetch em alguma api disponível na internet.
Usei get() de requests pois não estou enviando dados para o endpoint da api em questão, estou querendo receber dados então usei get()

Decidi criar um padrão de respostas com a variavel resMapping, onde é um dicionario que vai ter as informações consultadas.
o uso do dicionario com as keys em questão ajuda ao código ser mais prático.

"""


def getTasksInfo():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    resMapping = {"completed": 0, "pending": 0} # dicionario em questão que cria um padrão de respostas na função 
    """

    a lógica vai ser aplicada apenas se o status_code for 200 (OK) que indica que 
    a resposta não tem nenhum erro (status_code são setados pelos próprios desenvolvedores da aplicação)
    
    """
    if response.status_code == 200: 
        tasks = response.json()
        
        completed = 0 # para armazenar valores de tasks completadas
        pending = 0 # para armazenar valores de tasks não completadas (pendentes)
        
        for task in tasks:
            isTaskCompleted = task.get("completed")

            """

            Para evitar que a condição seja incorreta eu utilizo isinstance para esperar apenas bool, sendo True ou False
            Assim posso evitar que eu aceite valores do tipo errado da response e que isso acabe afetando algo na minha aplicação.

            isinstance é basicamente "é uma instancia?" então uso bool como argumento pois estou esperando por bool então é basicamente "é uma instancia do tipo bool?"
            
            """
            
            # "completed" retorna True ou False, então quando a condição for True ela vai ser de acordo com a condição abaixo
            if isinstance(isTaskCompleted, bool) and isTaskCompleted:
                completed += 1 # encontrou uma task marcada como "completed"

            # "completed" é False, então vai ser aplicado a condição abaixo 
            elif isinstance(isTaskCompleted, bool) and not isTaskCompleted:
                pending += 1
            
            # não existe isTaskCompleted do tipo bool 
            else:
                print(f"Não foi encontrado valores de tipo bool: status:{response.status_code} response: {response.text}") # uso response.text para ver o que a aplicação deu como resposta
                return resMapping
            
        resMapping["completed"] = completed
        resMapping["pending"] = pending
        return resMapping 
    else:
        print(f"Error, status:{response.status_code} response:{response.text}")
        return resMapping

tasksInfo = getTasksInfo()
print(tasksInfo)