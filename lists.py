cars = ['car', 'der', 'fre', 'opt']
# print(* cars, sep=', ')

for car in cars:
    print(f'I love the {car}')

nums = list(range(50, 70, 2))
print(nums)

nums_by3 = list(range(21, 71, 3))
print(*nums_by3)

squares = []
for num in range(10, 21):
    print(num * num)
    print(num ** num)
    squares.append(num ** 2)
print(squares)

print(f'minimum of saquares: {min(squares)}')
print(f'summation of saquares: {sum(squares)}')
print(f'maximum of saquares: {max(squares)}')

squares2 = [num ** 2 for num in range(5, 11)]
print(squares2)

odds = list(range(1, 20, 2))
print(odds)
even = list(range(0, 20, 2))
print(even)

# for num in range(1, 1000001):
# print(num)

nums = list(range(1, 1000001))
print(f'the minimum value: {min(nums)}')
print(f'the maximum value: {max(nums)}')
print(f'the summation value: {sum(nums)}')

nums_times3 = [x * 3 for x in range(1, 11)]
print(nums_times3)

mult_of3 = []
for number in range(3, 31, 3):
    mult_of3.append(number)
print(mult_of3)

cubes = []
for number in range(1, 11):
    cubes.append(number**3)
print(cubes)

cubes2 = [num**3 for num in range(1, 11)]
print(cubes2)

pizzas = ['chicken', 'mozzarella', 'pineapple']
friends_pizzas = pizzas[:]
print(pizzas)
print(friends_pizzas)
pizzas.append('beef')
friends_pizzas.append('pork')

print(pizzas)
print(friends_pizzas)
for pizza in pizzas:
    print(f'My favorite pizza is: {pizza}')

for pizza in friends_pizzas:
    print(f"My friends' favorite pizza is: {pizza}")