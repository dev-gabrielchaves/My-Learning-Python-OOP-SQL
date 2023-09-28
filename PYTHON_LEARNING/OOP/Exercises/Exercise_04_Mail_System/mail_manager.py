class MailManager:

    def __init__(self, sender_name: str, sender_mail: str) -> None:
        self.__sender_name = sender_name
        self.__sender_mail = sender_mail
        self.__title = None
        self.__body = None
        self.adressee_list = []
        self.__mail_box = []

    def create_mail(self, title: str, body: str) -> None:
        self.__title = title
        self.__body = body
    
    def set_adressee(self, name: str, mail: str) -> None:
        new_adressee = {
            'Name' : name,
            'Mail' : mail
        }
        self.adressee_list.append(new_adressee)
    
    def send_mail(self) -> None:

        new_mail = {
            'Sender Name' : self.__sender_name,
            'Sender Mail' : self.__sender_mail,
            'Mail Title' : self.__title,
            'Mail Body' : self.__body,
            'Adressee' : self.adressee_list
        }
        self.__mail_box.append(new_mail)

        print("\nMail sent!\n")
    
    def show_mail_box(self) -> None:
        
        for mail in self.__mail_box:
            for key in mail:
                if key == 'Adressee':
                    print("\nAdressee(s):\n")
                    for i in mail[key]:
                        for j in i:
                            print(f"{j}: {i[j]}")
                    print("\n-----------------------")
                else:
                    print(f"{key}: {mail[key]}")
            print()