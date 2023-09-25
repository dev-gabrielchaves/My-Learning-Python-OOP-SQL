class GerenciadorEmail:

    def __init__(self, nome_remetente: str, email_remetente: str) -> None:
        self.__nome_remetente = nome_remetente
        self.__email_remetente = email_remetente
        self.__titulo = None
        self.__corpo = None
        self.__lista_de_destinatarios = []

    def criar_email(self, titulo: str, corpo: str) -> None:
        self.__titulo = titulo
        self.__corpo = corpo
    
    def definir_destinatarios(self, nome: str, email: str) -> None:
        novo_destinatario = {
            'Nome' : nome,
            'Email' : email
        }
        self.__lista_de_destinatarios.append(novo_destinatario)
    
    def enviar_email(self) -> None:

        print("Enviando mensagem:\n" \
              f"Nome do remetente: {self.__nome_remetente}\n" \
                f"Email do remetente: {self.__email_remetente}\n" \
                    f"Título do email: {self.__titulo}\n" \
                        f"Corpo do email: {self.__corpo}")
        print("\nDestinatário(s):\n")
        for destinatario in self.__lista_de_destinatarios:
            for key in destinatario:
                print(f'{key}: {destinatario[key]}')