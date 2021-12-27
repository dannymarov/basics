print('Hello dictionaries')
student1 = {"name": "John",
            "age": 23,
            "country": "USA"}
print(student1)
student1['city'] = 'Brooklyn'

print(student1)
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
print('Union: ', set1.union(set2))
print('Intersection: ', set1.intersection(set2))
print('Difference set1 from set2: ', set1.difference(set2))
print('Difference set2 from set1: ', set2.difference(set1))

for key in student1:
    print('Key: ', key)
    print('Values using the keys: ', student1[key])
print('######################### by keys')
for bro in student1.keys():
    print('key: ', bro)
    print('values using the key: ', student1[bro])
print('######################### by values')
for value in student1.values():
    print('value of the dictionary: ', value)
print('######################### by items')
for key, value in sorted(student1.items()):
    print('this is the keys: ', key)
    print('this is the values: ', value)

friend1 = {'first_name': 'John',
           'last_name': 'Vick',
           'age': 34,
           'city': 'Lost Vegas'}
print(friend1['first_name'], friend1['last_name'], friend1['age'], friend1['city'])
friend2 = {'first_name': 'Nina',
           'last_name': 'Small',
           'age': 29,
           'city': 'Cave'}
friends = [friend1, friend2]
print(friends)
print(friends[0]['first_name'])
print(friend1['first_name'])
print(friends[1]['first_name'])
print('#########################')
fav_numbers = {'John': 2,
               'Smith': 4,
               'jack': 5,
               'trool': 6}
for a, b in fav_numbers.items():
    print(f"{a.title()}'s favorite number is {b}.")

glossary = {'variable': 'reference that can store a data',
            'string': 'sequence of characters',
            'list': 'a collection of elements in a particular order',
            'loop': 'An iteration over an object until that object is complete',
            'dictionary': 'a collection of key-value pairs'}
for word, definition in glossary.items():
    print(f'{word.upper()}\n\t {definition.title()}')
print('#########################')
rivers = {'egypt': 'nile',
          'brazil': 'amazonia',
          'usa': 'Mississippi',
          'ganga': 'India'}
for country, river in rivers.items():
    if country == 'usa':
        print(f'{country.upper()} has a large river naming {river.title()}')
    else:
        print(f'{country.title()} has a large river naming {river.title()}')

river_list = []
for river in rivers.values():
    print(river.title())
    river_list.append(river.title())
print(river_list)

river_list2 = [river.title() for river in rivers.values()]
print(river_list2)

country_list = [country.title() for country in rivers.keys()]
print(country_list)
print('###############################')
fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}
names = ['jen', 'hobbit', 'edward', 'mark']
for name in names:
    if name in fav_lang:
        print(f'{name.title()} thank you for taking the poll')
    else:
        print(f'{name.title()} please take a poll.')

number = int(input('Please provide with any number: '))

while number < 500:
    print(number)
    number = number * 3
