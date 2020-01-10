class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def get_full_name(self):
        print(f"{self.first} {self.last} is {self.age} years old")


user1 = User("Bill", "Smith", 24)

user1.get_full_name()

# Define Bank Account Below:


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def balance(self):
        return self.balance


class Chicken:
    total_eggs = 0

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs
