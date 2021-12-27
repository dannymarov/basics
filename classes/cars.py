class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # self.mileage = 0
        self.__mileage = 0 # encapsulation: hiding the data from being accessed by user

    def get_description(self):
        print(f'This is {self.make} {self.model} of {self.year}')

    def get_mileage(self):
        print(f'This car has a {self.__mileage} mile/s on it.')

    def set_mileage(self, new_mileage):
        if new_mileage > self.__mileage:
            self.__mileage = new_mileage
            print(f'odometer reader updated.')
        else:
            print('odometer reader was not updated.')

    def increment_odometer(self, miles):
        if miles > 0:
            # self.__mileage = self.__mileage + miles
            self.__mileage += miles
            print('Miles are added', miles)
        else:
            print('odometer cannot be updated with giving value!')

    def fill_gas_tank(self):
        print(f'Filling the tank for {self.model} ...Done!')

class ElectricCar(Car):#inheritance from class Car happening
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    def fill_gas_tank(self):
        """ Polymorphism: Method overriding serves to override the same method from parent class """
        print(f'This is {self.model} and it does not require gas...')
