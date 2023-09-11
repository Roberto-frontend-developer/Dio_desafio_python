class Usuario:
    def __init__(self, nome, data_nascimneto, cpf , endereco):
        self.nome = nome
        self.data_nascimneto = data_nascimneto
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    def __init__(self,cliente):
        self.saldo = 0
        self.transacoes = []
        self.saques_realizados = 0
        self.cliente = cliente

    
    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Despósito: +{valor}")
            return True
        return False
    
    def sacar(self,valor):
        if valor > 0 and self.saldo >= valor and self.saques_realizados < 3:
            self.saldo -= valor
            self.transacoes.append(f"Saque: -{valor:.2f}")
            self.saques_realizados += 1
            return True
        elif valor > 500:
            print("Limite de  máximo de  R$500 por saque.")
        elif self.saques_realizados >=3 :
            print("Limite de máximo saques diários atingido. ")
        else:
            print("Saldo insuficiente...")
        return False

    
    def extrato (self):
        return self.transacoes
    
# Lista de clientes
clientes = []

def cadastrar_usuario():
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Digite o CPF: ")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Verificar se o CPF já está cadastrado
    cpf_existente = any(cliente.cpf == cpf for cliente in clientes)
    if cpf_existente:
        print("CPF já cadastrado. Não é possível cadastrar o mesmo CPF novamente.")
        return

    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    clientes.append(usuario)
    print("Usuário cadastrado com sucesso!")

def criar_conta_corrente():
    cpf = input("Digite o CPF do cliente: ")
    
    # Verificar se o CPF existe na lista de clientes
    for cliente in clientes:
        if cliente.cpf == cpf:
            conta = ContaBancaria(cliente)
            print("Conta corrente criada com sucesso!")
            return
    
    print("CPF não encontrado. Certifique-se de cadastrar o cliente primeiro.")


conta_usuario = ContaBancaria(clientes)

#Função para exibir o menu e lidar comm as operações

def menu_usuario():
    
    print("1 - Despositar")
    print("2 - Sacar")
    print("3 - Exibir Extrato")
    print("4 - Exibir Saldo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")
    return opcao

#interação com usuário

while True:
    opcao = menu_usuario()


    if opcao == '1':
        valor = float(input("digite o valor para depósitar: "))
        conta_usuario.depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor para Saque: "))
        conta_usuario.sacar(valor)
    elif opcao == '3':
        extrato = conta_usuario.extrato()
        for transacao in extrato:
          print(transacao)
    elif opcao == '4':
        print(f"Saldo atual: {conta_usuario.saldo:.2f}")
    elif opcao == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")