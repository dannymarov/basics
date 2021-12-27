from classes.cars import *

car1 = Car('wolksvagon', 'SS', 2014)
car2 = Car('wercedez', 'ES350', 2018)
car3 = Car('toyota', 'Camry', 1939)

print(f'Model of this car:', car1.make.upper())
print(f'Model of this car:', car2.make.title())
print(f'Model of this car:', car3.make.lower())


car1.get_description()
car1.get_mileage()
car1.mileage = 25
car1.get_mileage()
car1.mileage = -100
car1.get_mileage()
# car1.get_mileage()
car1.set_mileage(25)
car1.get_mileage()
car1.set_mileage(0)
car1.get_mileage()
car1.set_mileage(-100)
car1.get_mileage()
print('#########################')
# car1.set_mileage(0)
# car1.get_mileage()
car1.mileage = -1100
car1.set_mileage(50)
car1.get_mileage()

car1.increment_odometer(50)
car1.get_mileage()
car1.increment_odometer(-500)
car1.get_mileage()

car1.increment_odometer(23)
car1.get_mileage()
car1.increment_odometer(-500)
car1.get_mileage()

print('##########################')
car4 = ElectricCar('Tesla', 'Model Y', 2020)
car4.get_description()
car4.fill_gas_tank()
car1.fill_gas_tank()
