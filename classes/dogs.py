class Dog():
    def __init__(self, name, color, breed, age):
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age

    def run(self):
        print(f'{self.name.title()} is running...')

    def sit(self):
        print(f'{self.name.title()} is now sitting...')

    def bark(self):
        print(f'{self.name.title()} says <Wroof-Wroof> madafaka')

    def description(self):
        if self.name.lower() == 'frenchi':
            print(
                f'Hello this is {self.name} and she is {self.breed} of {self.age} months of age and as you can see her color is {self.color}.')
        else:
            print(
                f'Hello this is {self.name} and he is {self.breed} of {self.age} and as you can see his color is {self.color}.')


class Cat():
    def __init__(self):
        pass

    def sits(self):
        print('Cats like to sit on laptops...')


class Restaurant():
    def __init__(self, restaurant_name:str, cusine_type:str):
        self.name = restaurant_name
        self.type = cusine_type

    def describe_restaurant(self):
        print(f'We are {self.name.upper()} and we are {self.type.title()} restaurant.')

    def open_restaurant(self):
        print(f'{self.name.upper()} is now open.')


restaurant1 = Restaurant('taco bells', 'mexican')

print(restaurant1.name.title())
print(restaurant1.type.title())
restaurant1.type = 'american'
print(f'Updated new menu with',restaurant1.type.title())
restaurant1.open_restaurant()
restaurant1.describe_restaurant()
