import email


class User:
    # переменные класса
    total_users = 0

    def __init__(self, name, email):
        self.nema = name
        self.email = email
        User.total_users += 1

    @classmethod
    def get_total_users(cls):
        return User.total_users




print(f"{User.total_users=}")
user_1 = User("Maksat", "maks@gmail.com")
user_2 = User("John", "John@gmail.com")

