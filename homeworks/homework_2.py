class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(f"Привет,меня зовут {self.name}, я родился в {self.birth_date},работаю{self.occupation}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, friend_name):
        super().__init__(name, birth_date, occupation)
        self.friend_name = friend_name

    def introduce(self):
        print(f"Привет, меня зовут{self.name},я друг {self.friend_name},"
              f"я родился {self.birth_date},я работаю {self.occupation}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, classmate_name):
        super().__init__(name, birth_date, occupation)
        self.classmate_name = classmate_name

    def introduce(self):
        print(f"Привет, меня зовут{self.name},я одноклассник {self.classmate_name},"
              f"я родился {self.birth_date},работаю {self.occupation}.")


friend1 = Friend("Максат", "11.09.2006", "программистом", "Руслана")
friend2 = Friend("Айбек", "14.08.2007", "экономистом", "Алихана")

classmate1 = Classmate("Нурлан", "02.04.2005", "предпринемателем", "Алибека")
classmate2 = Classmate("Ильяз", "25.06.2007", "стомотологом", "Саламата")
friend1.introduce()
friend2.introduce()
classmate1.introduce()
classmate2.introduce()
