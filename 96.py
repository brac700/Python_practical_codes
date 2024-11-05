from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the speak method on each instance
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
    
print("This program is written and executed by Harshit Sidher (0221BCA054)")
