class Contact:
    def __init__(self, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Номер телефона должен содержать из 10 цифр")

        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        """Проверяет, что номер содержит ровно из 10 цифр"""
        return phone_number.isdigit() and len(phone_number) == 10

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


contact1 = Contact("Максат", "0500016019")


# 2
class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Некорекктный номер телефона - должен быть 10 цифр")

        new_contact = Contact(name, phone_number)

        cls.all_contacts.append(new_contact)

    @classmethod
    def show_all_contacts(cls):
        if not cls.all_contacts:
            print("Список котактов пуст.")
        else:
            for contact in cls.all_contacts:
                print(contact)


ContactList.add_contact("Maksat", "0500016019")
ContactList.add_contact("Sultan", "0700210220")

ContactList.show_all_contacts()
