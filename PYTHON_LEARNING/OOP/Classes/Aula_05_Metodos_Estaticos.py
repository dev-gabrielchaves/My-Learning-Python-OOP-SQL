#Coleções de contextos que não são ligados entre si.
#Não é necessário a entrada do argumento 'self'.
#Não é necessária a criação de um objeto.

class Error:

    @staticmethod
    def error_500():
        print("Internal Server Error!")
    
    @staticmethod
    def error_404():
        print("Not Found!")

Error.error_404()
Error.error_500()