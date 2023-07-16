class User:
    def __init__(self, name, surname, email, phone, parol):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.parol = parol
        self.foydalanuvcilar_soni = 0

        def get_fullname(self):
            return f"ismi:{self.name} \nsurname:{self.surname}"

        def get_information(self):
            return f"ismi:{self.name} \nfamiliyasi:{self.surname} \nemail:{self.email} \nphone:{self.phone}"


user1 = User('azizbek', 'soliyev', 'azizbeksoliyev234@gmail.com', '99894166556', 'sdfgerwDFg2342@')
user1.get_information()
