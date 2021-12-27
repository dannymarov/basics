from classes.dogs import Dog, Cat

dog1 = Dog('Rupert', 'brown', 'Amerikan Eskimo', 2)
print('name of the dog: ', dog1.name)
print('color of the dog: ', dog1.color)
print('age of the dog: ', dog1.age)
print('breed of the dog: ', dog1.breed)
print('#############################')
dog2 = Dog('Krill', 'black', 'shepherd', 5)
dog3 = Dog('Frenchi', 'smoky white', 'scottish shorthair', 8)

dog1.run()
dog1.sit()
dog1.bark()
dog1.description()

print('##################################')

dog2.run()
dog2.sit()
dog2.bark()
dog2.description()

print('##################################')

dog3.run()
dog3.sit()
dog3.bark()
dog3.description()

print('##################################')

cat1 = Cat()
cat1.sits()

print('##################################')

