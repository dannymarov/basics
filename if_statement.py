# print('hello')
# user = input('Enter you name here: ')
# if user.lower() == 'john':
#    print(f'Hello, {user.title()}!!')
#    print('What do you want to study today?')
# else:
#    print('I do not know you.')

cars = ['ferrari', 'bmw', 'lexus', 'tesla']
for car in cars:
    if car.lower() == 'ferrari':
        print(f'Congrats you must love your {car.upper()}!')
    else:
        print(f'{car.title()} is a good car, but not good enough')

nums = (2, 3, 4, 5, 6)
print(10 in nums)

# Example of the inner loop
names = ['john', 'mark', 'ollie']
pizzas = ['pepperoni', 'cheese', 'bacon']
for name in names:
    print(name.title())
    for pizza in pizzas:
        print(f'{name.title()} likes {pizza.upper()}')
    print('#######')

# age = int(input('Please provide your age: '))

age = 10
if age <= 4:
    print('Your admission fee if free.')
elif 4 < age <= 18:
    # We can also use this line:
    # elif age > 4 and age <= 18:
    print('Your admission fee is 5$.')
else:
    print('Your admission fee is 10$.')

alien_color = 'Green'
if alien_color.lower() == 'green':
    print('you have just earned 5 points, yehooo!!')

# alien_color = input('Provide what color of alien did you shoot: 23')
alien_color = 'green'
# while alien_color.lower() != 'exit' and alien_color.lower() != 'x':
if alien_color.lower() == 'green':
    print('you have just earned 5 points, yehooo!!')
elif alien_color.lower() == 'yellow':
    print('you have just earned 10 points, nice job!!')
elif alien_color.lower() == 'red':
    print('you have just earned 15 points, great job!!')
else:
    print('you have not earned points, goo luck next time!!')
# alien_color = input('provide with proper color: ')

listby3 = []
listby5 = []
listby35 = []
for number in range(1, 101):
    print(number)
    if number % 3 == 0 and number % 5 == 0:
        listby35.append(number)
    elif number % 3 == 0:
        listby3.append(number)
    elif number % 5 == 0:
        listby5.append(number)
print(listby3)
print(listby5)
print(listby35)

players = [['john', 22, 320],
           ['mark', 26, 440],
           ['jose', 34, 350]]
print(f'the salary for the whole year is: {players[0][2]}')
print(f'and here the name of the player who is: {players[1][0]}')
print(players[2][2])

for player in players:
    print(f'Name of the player is: {player[0]}')
    print(f'Age of the player is: {player[1]}')
    print(f'Score of the player is: {player[2]}')

##########################
current_users = ['mark', 'ollie', 'hulk', 'mermaid', 'spongebob']
new_users = ['grey', 'ollie', 'nick', 'hulk', 'squidward']

for new_user in new_users:
    if new_user in current_users:
        print(f'The username {new_user} is not available. Please provide with another one.')
    else:
        print(f'username {new_user} is actually available.')

