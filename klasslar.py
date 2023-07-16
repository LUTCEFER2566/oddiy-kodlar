class User:
    def __init__(self, name, surname, email, phone, age):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.age = age
        self.soni = 0

    def getname(self):
        return f"name:{self.name}"


use1 = User('jahon', 'sobirov', 'jasdfbijkqw213345!@Gmail,com', '+985978465', '23')
print(use1.getname())
