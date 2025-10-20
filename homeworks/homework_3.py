from datetime import datetime

class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__occupation = occupation          # приватный
        self.__higher_education = higher_education  # приватный
        self.__birth_date = birth_date          # приватный

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return "есть" if self.__higher_education else "нет"

    @property
    def age(self):
        birth = datetime.strptime(self.__birth_date, "%d.%m.%Y")
        today = datetime.today()
        return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"У меня {self.higher_education} высшее образование.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Мое хобби {self.hobby}. У меня {self.higher_education} высшее образование.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group = group

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. "
              f"Я учился с друзьями в группе {self.group}. У меня {self.higher_education} высшее образование.")


# Проверка
friend1 = Friend("Максат", "11.09.2006", "программист", True, "футбол")
friend2 = Friend("Айбек", "14.08.2007", "экономист", True, "шахматы")

classmate1 = Classmate("Нурлан", "02.04.2005", "предприниматель", True, "11A")
classmate2 = Classmate("Ильяз", "25.06.2007", "стоматолог", True, "11B")

friend1.introduce()
print(friend1.age)
friend2.introduce()
print(friend2.age)
classmate1.introduce()
print(classmate1.age)
classmate2.introduce()
print(classmate2.age)
