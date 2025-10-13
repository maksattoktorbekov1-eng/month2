class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def __str__(self):
        edu = "Да" if self.higher_education else "Нет"
        return f"Имя: {self.name}, Дата рождения: {self.birth_date}, Профессия: {self.occupation}, Высшее образование: {edu}"


person1 = Person("Максат", "11.09.2006", "Программист", True)
person2 = Person("Айбек", "14.08.2007", "", False)
person3 = Person("Ильяз", "24.04.2007", "Учитель", True)
print(person1)
print(person2)
print(person3)
