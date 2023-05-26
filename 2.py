class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound():
        pass

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def make_sound(self):
        print("woof")
    
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def make_sound(self):
        print("meow")
    
    
cat = Cat('Kitty', 2)

print(cat.make_sound())