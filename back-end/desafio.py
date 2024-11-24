#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta


"""

no script do desafio criei 2 classes, uma é a classe do Banco, que é responsável por ações na conta, a outra é a classe conta;
self.contas = [] pode ser considerado o banco de dados do banco em questão, lá é onde tem todas as contas criadas no banco juntamente com suas informações,
que podem ser consultadas pela interface.
cada conta tem o id unico, cpf unico que facilita as transações e identificação das contas, em um banco real o usuário não pode criar uma conta com um cpf já existente.

a class Interface é apenas responsável pela logica de interação no banco, essa foi a maneira mais simples que pensei em fazer isso.
"""

class Banco:
    """
    Responsável por movimentar as contas.
    """
    def __init__(self):
        self.contas = []

    def criarConta(self, nome, cpf):
        # check se o cpf já tem alguma conta existente
        for conta in self.contas:
            if conta.cpf == cpf:
                print("Outra conta já está usando este CPF", conta.perfil())
                return None  

        id = len(self.contas) + 1  # responsável pelo auto incremento do id
        nova_conta = Conta(id, nome, cpf)
        self.contas.append(nova_conta)
        perfil = nova_conta.perfil()
        print(f"Conta criada com sucesso! \n-Informações da nova conta\n-{perfil}")
        print("<___________________________>")
        return nova_conta


    #função para encontrar conta com base no id unico
    def encontrarConta(self, id_conta):
        for conta in self.contas:
            if conta.id == id_conta:
                return conta
        raise ValueError("Conta não encontrada.")

    def realizarDeposito(self, id_conta, valor):
        conta = self.encontrarConta(id_conta)
        conta.depositar(valor)

    def realizarSaque(self, id_conta, valor):
        conta = self.encontrarConta(id_conta)
        conta.sacar(valor)

    def exibirConta(self, id_conta):
        conta = self.encontrarConta(id_conta)
        print(conta.perfil())

class Conta: 
    """
    class que é responsável pela conta do usuario, dentro de banco pode ter varias contas que representa alguém
    as maneiras de identificação é por id unico, a conta do usuário tem id unico e cpf unico
    é possível sacar/depositar o dinheiro da conta.
    """
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0.0

    def sacar(self, valor):
        if valor <= 0:
            return print("O valor do saque deve ser maior que zero.")
        if valor > self.saldo:
            return print("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor
        print(f"{valor:.2f}R$ sacado com sucesso da conta [{self.id}]-{self.nome}.")
    
    def depositar(self, valor):
        if valor <= 0:
            return print("O valor do depósito deve ser maior que zero.")
        self.saldo += valor
        print(f"Depósito de {self.saldo:.2f}R$ realizado com sucesso para a conta [{self.id}]-{self.nome}.")

    def perfil(self):
        return f"[Conta {self.id}]: ID: {self.id} Nome: {self.nome} CPF: {self.cpf} Saldo: R${self.saldo}"




class Interface:
    def __init__(self):
        self.banco = Banco()

    def iniciar(self):
        while True:
            """
             sei que existe opções melhores de criar paineis em python mas ao meu ver não seria necessário utilizar, o uso de interfaces reais
             usando frameworks como o Qt é mais recomendado para criação de interfaces
            """
            print(" ___-[ Banco Pegazus ]-___")
            print("|                         |")
            print("| 1. Criar Conta          |")
            print("| 2. Depositar            |")
            print("| 3. Sacar                |")
            print("| 4. Contas no sistema    |")
            print("| 5. Sair                 |")
            print("|                         |")
            print("|___-------------------___|")
            opcao = input("Escolha uma opção: ")

            try:
                if opcao == "1":
                    self.interfaceCriarConta()
                elif opcao == "2":
                    self.interfaceDepositar()
                elif opcao == "3":
                    self.interfaceSacar()
                elif opcao == "4":
                    self.interfaceContasInfo()
                elif opcao == "5":
                    print("Obrigado por usar o Banco Pegazus!")
                    break
                else:
                    print("Opção inválida, tente novamente.")
            except ValueError as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")

    def interfaceCriarConta(self):
        nome = input("[Criação de conta] Nome: ")
        cpf = input("[Criação de conta] CPF (Cadastro de Pessoa Física documento): ")
        self.banco.criarConta(nome, cpf)
    
    def interfaceContasInfo(self):
        print("\nContas no sistema:")
        for conta in self.banco.contas:
            print(conta.perfil())

    def interfaceSacar(self):
        print("__Área de Saque__")
        while True:
            try:
                id_conta = int(input("Digite o ID da conta: "))
                self.banco.exibirConta(id_conta)
                confirma = int(input("Confirma que essa é a conta que você quer sacar?\n1. Sim\n2. Não\n3. Ir para o menu principal\nDigite: "))

                if confirma == 1:
                    valor = float(input("Digite o valor do saque: "))
                    self.banco.realizarSaque(id_conta, valor)
                    break
                elif confirma == 2:
                    print("Por favor, digite o ID da conta novamente.")
                elif confirma == 3:
                    print("Voltando ao menu principal.")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Certifique-se de digitar números válidos para ID e valores.")
            except Exception as e:
                print(f"Erro inesperado: {e}.")

    def interfaceDepositar(self):
        print("__Local de depósito__")
        while True:
            id_conta = int(input("Digite o ID da conta: "))
            self.banco.exibirConta(id_conta)
            confirma = int(input("Confirma que essa é a conta que você quer depositar?\n1. Sim \n2. Não\n3. Ir para o menu principal\nDigite: "))

            if confirma == 1:
                valor = float(input("Digite o valor do depósito: "))
                self.banco.realizarDeposito(id_conta, valor)
                break
            elif confirma == 2:
                print("Por favor, digite o ID da conta novamente.")
            elif confirma == 3:
                print("Voltando ao menu principal.")
                break
            else:
                print("Opção inválida. Tente novamente.")



interface = Interface()
interface.iniciar()