from functions import *
from functions import greet_user

greet_user_name('John')
greet_user()
greet_user_input()
describe_city('new york')
describe_city('paris', 'france')


# nums = (range(1, 2000))
nums = [12, 23, 121, 334, 45, 23, 545, 65, 445, 777]
chars = ['aa', 'd', 'x', 'u', 'g']

get_largest_numbers(nums)
get_largest_numbers(chars)
result = get_largest_numbers(nums) + 100
print('the result of the function plus number is: ', result)
# get_largest_numbers(range(1, 1090))

print('############################ Album')

album1 = make_album('funeral', 'arcade fire')
album2 = make_album('shakira', 'donde estan los ladrones')
album3 = make_album('beatles','white album', 30)
print(f"{album1['artist']} had a great album named {album1['album']}")
print(f"{album2['artist']} had a great album named {album2['album']} with a total of {album2['tracks']} tracks on it.")
print(f"{album3['artist']} had a great album named {album3['album']} with a total of {album3['tracks']} tracks on it.")

