class Vehicle: 
    def __init__(self, brand, model): 
        self.brand = brand 
        self.model = model 
 
    def start(self): 
        print(f"{self.brand} {self.model} is starting.") 
 
# Child class inherits from Vehicle 
class Car(Vehicle): 
    def play_music(self): 
        print(f"{self.brand} {self.model} is playing music.") 
 
class ElectricCar(Car): 
    def charge(self): 
        print(f"{self.brand} {self.model} is charging.") 
class SmartDevice: 
    def connect_wifi(self): 
        print("Connecting to WiFi...") 
 
class SmartCar(Car, SmartDevice): 
    def auto_drive(self): 
        print(f"{self.brand} {self.model} is driving automatically.") 
class Bike(Vehicle): 
    def kick_start(self): 
        print(f"{self.brand} {self.model} is kick-started.") 
class ElectricSmartCar(SmartCar, ElectricCar): 
    def autopilot_mode(self): 
        print(f"{self.brand} {self.model} is in autopilot mode.") 

