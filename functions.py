def greet_user():
    print('Hello!')
    print('Hello!')


def greet_user_name(user_name):
    print(f'Hello! oh great {user_name}')


def greet_user_input():
    user_name = input('place your name here: ')
    print(f'Helo, your highness {user_name.title()}!')


def describe_city(city, country='united states of america'):
    print(f'{city.title()} is in {country.title()}.')


def get_largest_numbers(nums_list: list):
    # def get_largest_numbers(nums_list:list) -> int:
    print('the largest number is:', max(nums_list))
    return max(nums_list)

def make_album(artist_name, album_title, num_tracks = None):
    album = {'artist': artist_name.title(),
             'album': album_title.upper(),
             'tracks': num_tracks}
    return album

