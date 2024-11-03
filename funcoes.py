from classes import *  # Importa todas as classes que você criou no classes.py, permitindo usar elas neste arquivo
import os  # Importa a biblioteca os para utilizar comandos do sistema, como limpar a tela

# Definições fixas para o gerente do banco
gerente_nome = "grupo3"  # Nome predefinido do gerente, usado para autenticação
gerente_cpf = "110211310107"  # CPF predefinido do gerente, usado para autenticação

banco = Banco()  # Cria uma instância da classe Banco, que gerencia clientes e suas contas
clientes = []  # Inicializa uma lista vazia para armazenar os clientes cadastrados

def menu():  # Função que exibe o menu principal do banco
    while True:  
        print("=" * 30)
        print(" " * 8 + "SENAI BANK")
        print("=" * 30)
        print("1 - LOGIN")  # Opção para fazer login
        print("2 - CADASTRO")  # Opção para cadastro de novo cliente
        print("3 - SAIR")  # Opção para sair do sistema
        print("=" * 30)
        escolha = input("---> ")  # Solicita ao usuário que escolha uma opção

        if escolha == '1':
            return '1'  # Retorna '1' para indicar que o usuário escolheu fazer login
        elif escolha == '2':
            return '2'  # Retorna '2' para indicar que o usuário quer se cadastrar
        elif escolha == '3':
            return '3'  # Retorna '3' para indicar que o usuário quer sair
        else:
            print("Opção inválida! Tente novamente.")  

def limpa_console():
    os.system("pause")  # Pausa a execução até o usuário pressionar uma tecla
    os.system("cls")  # Limpa a tela

def cadastro():
    global banco  # Indica que a variável banco aqui é a global 
    limpa_console()  
    print("=" * 60)
    print(" " * 10 + "BEM-VINDO À TELA DE CADASTRO")
    print("=" * 60)
    nome = input("INSIRA O SEU NOME COMPLETO:\n---> ")  # Solicita o nome completo do usuário
    cpf = input("INSIRA O SEU CPF:\n---> ")  # Solicita o CPF do usuário
    novo_cliente = Cliente(nome, cpf)  # Cria uma nova instância de Cliente com os dados fornecidos
    banco.adicionar_cliente(novo_cliente)  # Adiciona o novo cliente à lista de clientes no banco
    clientes.append(novo_cliente)  # Adiciona o novo cliente à lista local de clientes
    print("CADASTRO REALIZADO COM SUCESSO!") 
    limpa_console()  

def login():
    global banco, gerente_nome, gerente_cpf  # Indica que estas variáveis são globais
    limpa_console()  
    sair = None  # Variável de controle para sair do loop de login
    while sair is None:  
        print("=" * 60)
        print(" " * 10 + "BEM VINDO À TELA DE LOGIN")
        print("")
        print("1 - FAZER LOGIN")  # Opção para fazer login
        print("")
        print("2 - VOLTAR AO MENU PRINCIPAL")  # Opção para voltar ao menu principal
        print("")
        escolha = input("ESCOLHA UMA OPÇÃO:\n---> ")  # Solicita a escolha do usuário

        if escolha == '2':
            print("VOLTANDO AO MENU PRINCIPAL...")  # Mensagem indicando retorno ao menu principal
            return  # Sai da função login e retorna ao menu principal

        elif escolha == '1':
            limpa_console()  
            nome = input("INSIRA O SEU NOME COMPLETO:\n---> ")  # Solicita o nome do usuário para login
            cpf = input("INSIRA O SEU CPF:\n---> ")  # Solicita o CPF do usuário para login
            if nome == gerente_nome and cpf == gerente_cpf:
                print(f"BEM VINDO, GERENTE {nome}!")  
                gerente()  # Chama a função de gerenciamento do gerente
                return  
            for cliente in banco._clientes:  # Itera sobre todos os clientes cadastrados no banco
                if cliente.get_cpf() == cpf and cliente.get_nome() == nome:
                    print(f"BEM VINDO, {cliente.get_nome()}!") 
                    conta_principal(cliente)  # Chama a função principal da conta do cliente
                    return  
            print("Nome ou CPF incorretos. Tente novamente.")  
            limpa_console()  
        else:
            print("Opção inválida! Tente novamente.")  # Mensagem de erro para opções inválidas no login
            limpa_console() 

def conta_principal(cliente):
    sair = None  # Variável de controle para sair do menu principal da conta do cliente
    while sair != 0:  
        limpa_console() 
        print("=" * 30)
        print(" " * 8 + "SENAI BANK")
        print("=" * 30)
        print("BEM VINDO À SUA CONTA!!") 
        print("")
        print("")
        print(" ______________________________________")
        print("|                MENU                  |")
        print(" --------------------------------------")
        print("| 1 - ENTRAR NA CONTA POUPANÇA         |")  # Opção para acessar a conta poupança
        print("| 2 - ENTRAR NA CONTA CORRENTE         |")  # Opção para acessar a conta corrente
        print("| 3 - CRIAR PERFIL                     |")  # Opção para criar um novo perfil (não definido no trecho)
        print("| 4 - EXCLUIR PERFIL                   |")  # Opção para excluir o perfil (não definido no trecho)
        print("| 5 - SAIR DO PERFIL                   |")  # Opção para sair do perfil atual
        print("| 6 - VER TRANSAÇÕES                   |")  # Opção para visualizar as transações
        print("|______________________________________|")
        print("")
        print("")
        print("")
        try: 
            escolha = int(input("ESCOLHA UMA OPÇÃO: \n --->")) 
            match escolha: 

                case 1:
                    limpa_console()  
                    conta_poupanca = None  # Inicializa a variável da conta poupança
                    for conta in cliente.get_contas():  # Itera sobre todas as contas do cliente
                        if isinstance(conta, ContaPoupanca):
                            conta_poupanca = conta  # Identifica se já existe uma conta poupança
                            break
                    if not conta_poupanca:
                        conta_poupanca = ContaPoupanca()  # Cria uma nova conta poupança caso não exista
                        cliente.adicionar_conta(conta_poupanca)  # Adiciona a nova conta poupança ao cliente
                        print("Bem-vindo à sua Conta Poupança!") 
                        limpa_console()
                    poupanca(conta_poupanca)  # Chama a função que gerencia a conta poupança

                case 2:
                    limpa_console()  # Limpa a tela antes de acessar a corrente
                    conta_corrente = None  # Inicializa a variável da conta corrente
                    for conta in cliente.get_contas():  # Itera sobre todas as contas do cliente
                        if isinstance(conta, ContaCorrente):
                            conta_corrente = conta  # Identifica se já existe uma conta corrente
                            break
                    if not conta_corrente:
                        conta_corrente = ContaCorrente()  # Cria uma nova conta corrente caso não exista
                        cliente.adicionar_conta(conta_corrente)  # Adiciona a nova conta corrente ao cliente
                        print("Bem-vindo à sua Conta Corrente!")  #
                        limpa_console()
                    corrente(conta_corrente)  # Chama a função que gerencia a conta corrente
                
                case 3:
                    limpa_console()  # Limpa a tela antes de criar um perfil
                    adicionar_cliente()  # Chama a função para adicionar um novo cliente (perfil)
    
                case 4:
                    excluirperfil()  # Chama a função para excluir o perfil do cliente
    
                case 5:
                    sair = 0  # Define a variável sair como 0 para encerrar o loop e retornar ao menu principal
    
                case 6:
                    limpa_console()  # Limpa a tela antes de exibir as transações
                    if cliente:
                        print(f"Transações do cliente {cliente.get_nome()}:")  # Exibe o nome do cliente
                        for conta in cliente.get_contas():
                            tipo_conta = 'Corrente' if isinstance(conta, ContaCorrente) else 'Poupança'  # Determina o tipo da conta
                            print(f"Conta {tipo_conta}:")  # Exibe o tipo da conta
                            for transacao in conta._extrato.consultar_extrato():
                                print(transacao)  # Lista todas as transações dessa conta
                    os.system("pause")  # Pausa a execução para que o cliente possa visualizar as transações
                case _: 
                    print("Opção inválida! Tente novamente.")  # Mensagem de erro para opções inválidas
        except ValueError:
            print("Por favor, insira uma opção numérica válida.")  # Mensagem de erro se a entrada não for um número
            os.system("pause")  

def poupanca(conta_poupanca):
    limpa_console()  
    print("BEM-VINDO À POUPANÇA")  # Mensagem de boas-vindas à seção de poupança
    print("")
    while True: 
        print("\nEscolha uma opção:")
        print("1: Consultar saldo")  # Opção para verificar o saldo
        print("2: Sacar")  # Opção para sacar dinheiro
        print("3: Depositar")  # Opção para depositar dinheiro
        print("4: Sair")  # Opção para sair da poupança
        opcao = input("Digite o número da opção: ")  # Solicita a escolha do usuário
        match opcao:  
            case '1':
                print(f"Seu saldo é de: R$ {conta_poupanca.consultar_saldo():.2f}")  # Exibe o saldo atual
                limpa_console()
            case '2':
                try:
                    valor_saque = float(input("Insira o valor que deseja sacar: "))  # Solicita o valor a ser sacado
                    if conta_poupanca.sacar(valor_saque):
                        print(f"Saldo atual: R$ {conta_poupanca.consultar_saldo():.2f}")  # Atualiza e exibe o saldo após o saque
                    limpa_console()
                except ValueError:
                    print("Por favor, insira um número válido.") 
                    limpa_console()
            case '3':
                try:
                    deposito_valor = float(input("Insira o valor que deseja depositar: "))  # Solicita o valor a ser depositado
                    conta_poupanca.depositar(deposito_valor)  # Executa o depósito na conta poupança
                    print(f"Saldo atual: R$ {conta_poupanca.consultar_saldo():.2f}")  # Atualiza e exibe o saldo após o depósito
                    limpa_console()
                except ValueError:
                    print("Por favor, insira um número válido.")  
                    limpa_console()
            case '4':
                print("Saindo...")  # Mensagem de saída da poupança
                limpa_console()
                break  
            case _:
                print("Opção inválida. Tente novamente.")  
                limpa_console()

def corrente(conta_corrente):
    limpa_console()  
    print("BEM-VINDO À CORRENTE")  
    while True:  
        print("\nEscolha uma opção:")
        print("1: Consultar saldo")  # Opção para verificar o saldo
        print("2: Sacar")  # Opção para sacar dinheiro
        print("3: Depositar")  # Opção para depositar dinheiro
        print("4: Transferir")  # Opção para transferir dinheiro para outra conta
        print("5: Sair")  # Opção para sair da conta corrente
        opcao = input("Digite o número da opção: ")  # Solicita a escolha do usuário
        match opcao: 
            case '1':
                print(f"Seu saldo é de: R$ {conta_corrente.consultar_saldo():.2f}")  # Exibe o saldo atual
                limpa_console()
            case '2':
                try:
                    valor_saque = float(input("Insira o valor que deseja sacar: "))  # Solicita o valor a ser sacado
                    if conta_corrente.sacar(valor_saque):
                        print(f"Saldo atual: R$ {conta_corrente.consultar_saldo():.2f}")  # Atualiza e exibe o saldo após o saque
                    limpa_console()
                except ValueError:
                    print("Por favor, insira um número válido.")  
                    limpa_console()
            case '3':
                try:
                    deposito_valor = float(input("Insira o valor que deseja depositar: "))  # Solicita o valor a ser depositado
                    conta_corrente.depositar(deposito_valor)  # Executa o depósito na conta corrente
                    print(f"Saldo atual: R$ {conta_corrente.consultar_saldo():.2f}")  # Atualiza e exibe o saldo após o depósito
                    limpa_console()
                except ValueError:
                    print("Por favor, insira um número válido.")  # Mensagem de erro se o valor não for numérico
                    limpa_console()
            case '4':
                cpf_destino = input("Digite o CPF do cliente que você deseja enviar: ")  # Solicita o CPF do destinatário da transferência
                cliente_destino = banco.obter_cliente(cpf_destino)  # Busca o cliente destinatário no banco
                if not cliente_destino:
                    print("Cliente não encontrado")  
                else:
                    conta_destino = None  # Inicializa a variável da conta destino
                    for conta in cliente_destino.get_contas():  # Itera sobre as contas do cliente destinatário
                        if isinstance(conta, ContaCorrente):
                            conta_destino = conta  # Identifica se há uma conta corrente do destinatário
                            break
                    if not conta_destino:
                        print("Cliente não possui conta corrente")  # Mensagem de erro se o destinatário não tiver conta corrente
                    else:
                        try:
                            valor = float(input("Digite o valor para transferir:"))  # Solicita o valor da transferência
                            if conta_corrente.transferir(conta_destino, valor):
                                print("Transferência realizada")  
                        except ValueError:
                            print("Por favor, insira um valor válido.")  
                limpa_console()
            case '5':
                print("Saindo...")  
                limpa_console()
                break  # Encerra o loop 
            case _:
                print("Opção inválida. Tente novamente.")  
                limpa_console()

def gerente():
    limpa_console()  # Limpa a tela antes de acessar as funções do gerente
    while True: 
        print("=" * 30)
        print(" " * 8 + "GERENTE - SENAI BANK")
        print("=" * 30)
        print("1 - LISTAR TODOS OS CLIENTES")  # Opção para listar todos os clientes cadastrados
        print("2 - ADICIONAR NOVO CLIENTE")  # Opção para adicionar um novo cliente ao banco
        print("3 - EXCLUIR CLIENTE")  # Opção para excluir um cliente existente
        print("4 - CONSULTAR TRANSAÇÕES DE UM CLIENTE")  # Opção para consultar as transações de um cliente específico
        print("5 - VOLTAR AO MENU PRINCIPAL")  # Opção para voltar ao menu principal

        try:
            escolha = int(input("---> "))  # Solicita a escolha do gerente e converte para inteiro
            match escolha: 
                case 1:
                    listar_clientes()  # Chama a função para listar todos os clientes
                case 2:
                    adicionar_cliente()  # Chama a função para adicionar um novo cliente
                case 3:
                    excluir_cliente()  # Chama a função para excluir um cliente existente
                case 4:
                    extrato()  # Chama a função para consultar o extrato de transações de um cliente
                case 5:
                    break  # Encerra o loop e sai da função gerente, retornando ao menu principal
                case _:
                    print("Opção inválida! Tente novamente.")  # Mensagem de erro para opções inválidas
        except ValueError:
            print("Por favor, insira uma opção numérica válida.")  # Mensagem de erro se a entrada não for um número
            limpa_console()

def listar_clientes():
    limpa_console() 
    print("LISTA DE TODOS OS CLIENTES:")
    if not banco._clientes:
        print("Nenhum cliente cadastrado.")  # Informa que não há clientes registrados
    else:
        for cliente in banco._clientes:  # Itera sobre todos os clientes cadastrados no banco
            print(f"Nome: {cliente.get_nome()} - CPF: {cliente.get_cpf()}")  # Exibe o nome e CPF de cada cliente
    limpa_console() 

def adicionar_cliente():
    limpa_console()  
    print("ADICIONAR NOVO USUÁRIO")
    nome = input("INSIRA O NOME DO NOVO USUÁRIO \n -->")  # Solicita o nome do novo cliente
    cpf = input("INSIRA O CPF DO NOVO USUÁRIO \n -->")  # Solicita o CPF do novo cliente
    if banco.obter_cliente(cpf):
        print("ERRO: Já existe um cliente com este CPF cadastrado.")  # Informa que o CPF já está cadastrado
    else:
        novo_cliente = Cliente(nome, cpf)  # Cria uma nova instância de Cliente
        banco.adicionar_cliente(novo_cliente)  # Adiciona o novo cliente ao banco
        print("CADASTRO REALIZADO COM SUCESSO!")  
    limpa_console()

def excluir_cliente():
    limpa_console()  
    print("EXCLUIR CLIENTE")  
    cpf = input("INSIRA O CPF QUE VOCÊ DESEJA EXCLUIR:\n---> ")  # Solicita o CPF do cliente a ser excluído
    cliente = banco.obter_cliente(cpf)  # Busca o cliente no banco pelo CPF
    if cliente:
        for conta in cliente.get_contas():  # Itera sobre todas as contas do cliente
            cliente.remover_conta(conta)  # Remove cada conta associada ao cliente
        banco.remover_cliente(cpf)  # Remove o cliente do banco
    else:
        print("CLIENTE NÃO ENCONTRADO.")  
    os.system("pause")  # Pausa a execução para que o usuário veja a mensagem

def extrato():
    limpa_console()
    cpf = input("INSIRA O CPF DO CLIENTE PARA VERIFICAR O EXTRATO \n -->")  # Solicita o CPF do cliente para consultar o extrato
    cliente = banco.obter_cliente(cpf)  # Busca o cliente no banco pelo CPF
    if cliente:
        print(f"Transações do cliente {cliente.get_nome()}:")  # Exibe o nome do cliente
        for conta in cliente.get_contas():  # Itera sobre todas as contas do cliente
            tipo_conta = 'Corrente' if isinstance(conta, ContaCorrente) else 'Poupança'  # Determina o tipo da conta
            print(f"Conta {tipo_conta}:")  # Exibe o tipo da conta
            for transacao in conta._extrato.consultar_extrato():  # Itera sobre todas as transações da conta
                print(transacao)  # Exibe cada transação
    else:
        print("Cliente não encontrado.")  # Informa que o cliente não foi encontrado
    limpa_console()  # Limpa a tela após a consulta

def excluirperfil():
    limpa_console()
    cpf_cliente = input("DIGITE O CPF DA CONTA QUE VOCê DESEJA EXCLUIR?:\n---> ")  # Solicita o CPF do cliente a ser excluído
    banco.remover_cliente(cpf_cliente)  # Remove o cliente do banco utilizando o CPF fornecido
    return  