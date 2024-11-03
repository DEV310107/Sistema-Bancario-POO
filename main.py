from funcoes import * #Importa as funções do menu
import os #Importa biblioteca

sair = None #Define a variavel sair para criação do loop 

while sair != 0:#Define a variável 'sair' para controlar o loop do menu
    try: #Permite que possa dá erro no código, porém não ira interromper o programa.
        escolha = menu() # Chama a função 'menu' para exibir o menu e retorna a escolha do usuário
        match escolha: # Usa a estrutura 'match' para tratar as diferentes opções do menu
            case "1": #Caso a escolha for igual a 1 irá entrar na case
                login() #chama a função login

            case "2":#Caso a escolha for igual a 2 irá entrar na case
                cadastro() #chama a função cadastro

            case "3":#Caso a escolha for igual a 3 irá entrar na case
                sair = 0 #Define sair como 0 para finalizar o loop
           
            case _: #case defalt[]
                        print("Opção inválida! Tente novamente.")

        
    except Exception as e: #O bloco except é executado se ocorrer uma exceção no bloco try
        print(f"Ocorreu um erro: {e}") #informa o usuario sobre o erro
        limpa_console()