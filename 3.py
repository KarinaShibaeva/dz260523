class Venicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
    def start(self):
        pass

class Car(Venicle):
    def __init__(self,  brand, speed):
        super().__init__( brand, speed)
    
    def start(self):
        print(f"Двигатель {self.brand} запущен")
    
    
class Motocycle(Venicle):
    def __init__(self,  brand, speed):
        super().__init__( brand, speed)
    
    def start(self):
        print(f"Двигатель {self.brand} запущен")
        
car = Car('bmv', 300)

print(car.start())