# Закрепление пройденного материала - Использование ООП в пf
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self, sound):
        pass

class Dog(Animal):
    def make_sound(self,sound):
        print("гав гав")
class Cat(Animal):
    def make_sound(self,sound):
        print("")
puppy = Dog()
puppy.make_sound("")