from abc import ABC , abstractclassmethod,abstractproperty
from datetime import datetime


class Usuario(ABC):
  def __init__(self , nome, data_nascimento, cpf, endereco):
    self.nome = nome
    self.data_nascimento = data_nascimento
    self.cpf =  cpf
    self.endereco = endereco
      

  @abstractclassmethod
  def exibir_informacoes(self):
    pass

class ContaBancaria:
  def __init__(self, cliente):
    self.saldo = 0
    self. transacoes = []
    self.saques_realizados = 0
    self.cliente = cliente

  def depositar(self, amount):
    if amount > 0:
      self.saldo += amount
      self.transacoes.append(f"Depósito: + {amount}")
      return True
    return False
  
  def sacar(self, amount):
    if amount > 0 and self.saldo >= amount and self.saques_realizados < 3:
      self.saldo -= amount
      self.transacoes.append(f"Saque: - {amount:.2f}")
      self.saques_realizados += 1
      return True
    elif amount == 500:
      print("Limite máximo de R$500 por saques...")
    elif self.saques_realizados >=3:
      print("Limite máximo de  sasques diários atingido...")
    else:
      print("Saldo insuficiente...")
    return False
  
  def extrato(self):
    return self.transacoes
  
class Cliente(Usuario):
   def exibir_informcoes(self):
      print(f"Nome: {self.nome}")
      print(f"Data de nascimento: {self.data_nascimento}")
      print(f"CPF: {self.cpf}")
      print(f"Endereço: {self.endereco}")

   @classmethod
   def criar_cliente(cls): 
      nome = input("Digite o nome do cliente:  ")
      data_nascimento = input("Digite a data de nascimento( dd/mm/aaaa")
      cpf = input("Digite o CPF: ")
      endereco = input("Digite o endereço (logradouro, no - bairro - cidade/sigla estado")
      return cls(nome, data_nascimento, cpf, endereco)
   

#Lista d eclientes
clientes =[]
      
def cadastrar_usuario():
  cliente = Cliente.criar_cliente()
  #Verificar se cpf Já Existe
  cpf_existente = any(c.cpf== cliente.cpf for c in clientes)
  if cpf_existente:
    print("CPf já cadastrado. Não é possivel cadastrar o mesmo Cpf")
    return  

  clientes.append(cliente)
  print("Usuário cadastro com suceso!")

cliente_index = (clientes[0])# Assumindo o primeiro cliente da lista
conta_usuario = ContaBancaria(cliente_index)


def criar_conta_corrente():
  cpf = input("Digite o CPF do cliente: ")

  for cliente in clientes:
    if cliente.cpf == cpf:
      conta = ContaBancaria(cliente)
      print("Conta corrente criada com sucesso!")
      return
  
  print("CPF não encontrado.Certifique-se de cadastrar o cliente...")



# Função para exibir o menu e lidar com as operações

def menu_usuario():
  print("1 - Depositar")
  print("2 - Sacar")
  print("3 - Exibir Extrato")
  print("4 - Exibir Saldo")
  print("0 - Sair")

  opcao = input("Ecolher um a opção: ")
  return opcao


# Interação com o usuário

while True:
    opcao = menu_usuario()

    if opcao == '1':
        valor = float(input("Digite o valor para depositar: "))
        conta_usuario.depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor para saque: "))
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
  
