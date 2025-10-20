class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def __str__(self):
        edu = "Да" if self.higher_education else "Нет"
        return f"Имя: {self.name}, Дата рождения: {self.birth_date}, Профессия: {self.occupation}, Высшее образование: {edu}"


person1 = Person("Алибек", "12.03.2005", "Программист", True)
person2 = Person("Айжан", "25.07.2002", "Дизайнер", False)
person3 = Person("Марат", "10.11.2003", "Учитель", True)

print(person1)
print(person2)
print(person3)
