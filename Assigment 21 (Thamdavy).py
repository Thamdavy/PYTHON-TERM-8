class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old.")

# Corrected instantiation
myClassmate = Person("Alice", 25)

print(myClassmate.name)
print(myClassmate.age)

myClassmate.greet()
