# Parent class (Base class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass  # Abstract method, to be defined in child classes

    def display_info(self):
        print(f"{self.name} is a {self.species}")

# Child class (Subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the parent class (Animal)
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        return "Woof!"

    def display_info(self):
        super().display_info()
        print(f"{self.name} is a {self.species} of breed {self.breed}")

# Child class (Subclass)
class Cat(Animal):
    def __init__(self, name, color):
        # Call the constructor of the parent class (Animal)
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self):
        return "Meow!"

    def display_info(self):
        super().display_info()
        print(f"{self.name} is a {self.species} with {self.color} fur")

# Creating objects of child classes
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "Tabby")

# Accessing attributes and methods of child classes
print(dog1.name)           
print(dog1.speak())        
dog1.display_info()


print(cat1.name)
print(cat1.speak())    
cat1.display_info()

