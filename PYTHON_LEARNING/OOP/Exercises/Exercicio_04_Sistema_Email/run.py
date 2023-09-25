from gerenciador_de_email import GerenciadorEmail

gerenciadorEmail = GerenciadorEmail('Minha Empresa', 'MinhaEmpresa@email.com')

while True:
   
    titulo = input("Defina o título do email: ")
    corpo = input("Defina o corpo do email: ")

    gerenciadorEmail.criar_email(titulo, corpo)

    nome_destinaratio = input("Defina o nome do destinatio: ")
    email_destinaratio = input("Defina o email do destinatio: ")

    gerenciadorEmail.definir_destinatarios(nome_destinaratio, email_destinaratio)

    while True:

        opcao = input("Deseja adicionar outro destinatario? ")

        if opcao == 's':
            nome_destinaratio = input("Defina o nome do destinatio: ")
            email_destinaratio = input("Defina o email do destinatio: ")

            gerenciadorEmail.definir_destinatarios(nome_destinaratio, email_destinaratio)
        
        else:
            break
    
    gerenciadorEmail.enviar_email()