class Car: 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 
    def display_info(self): 
        print(f"{self.year} {self.make} {self.model}")
    
my_car = Car("Toyota", "Corolla", 2020) 
my_car.display_info()  # Output: 2020 Toyota Corolla

print("This program is written and executed by Harshit Sidher (0221BCA054)")