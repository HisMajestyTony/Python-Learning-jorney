class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def bark(self):
        print(f'Woof! My name is {self.name}')

    def human_years(self):
        return self.age * 7

    def is_older_than(self, other_dog):
        return self.age > other_dog.age

    def description(self):
        return f"My dog is {self.name}, age {self.age}, species {Dog.species}."




dog1 = Dog("Rex", 3)
dog2 = Dog("Bob", 4)
dog3 = Dog("Django", 5)

if dog1.is_older_than(dog2):
    print(f"{dog1.name} is older than {dog2.name}")
else:
    print(f"{dog2.name} is older than {dog1.name}")

print(dog1.description())
print(dog2.description())
print(dog3.description())