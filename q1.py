# Define a class Bird with a method fly() and a class Fish with a method swim(). 
# Create a class Penguin that inherits both Bird and Fish, and use super() to call the fly()
# method in the Penguin class.

class Bird:
    def fly(self):
        print("Bird can fly")

class Fish:
    def swim(self):
        print("Fish can swim")

class Penguin(Bird, Fish):
    def fly(self):
        super().fly()
        print("Penguins cannot fly")

Penguin().fly()