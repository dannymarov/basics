from yaml import *


def read_file(filepath):
    with open(filepath) as names:
        print(names.read())
        print(names.readline())
        print(names.readline())
        print(names.readlines())
        print(names.name)


def read_file_lines(filepath):
    try:
        print('Reading the file')
        with open(filepath, mode='r') as data:
            for line in data.readlines():
                print(f'line value:', line, end='')
            print('\n \nnow i have read the file.')
            print(f'Divivsion for fun {5 / 0}')
    except FileNotFoundError as err:
        print(f'please check your file path. \n{err}')
    except ZeroDivisionError as err:
        print(f'who divides number by 0', {err})

    finally:
        print(f'\n read_file_lines function completed!')


def load_yml(filepath):
    with open(filepath) as data:
        doc = safe_load(data)
    return doc

myfile = './../data/names.txt'
# myfile = './../data/name.txt' this will give error due to the file nonexistence <names> proper filename, while <name> is not.
students_path = './../data/students.yml'

# read_file(myfile)
# read_file_lines(myfile)

doc = load_yml(students_path)

bird1 = doc['student1']['calling-birds'][0]
all_birds = doc['student1']['calling-birds']

web_url = doc['credentials']['url']
uname = doc['credentials']['username']
pword = doc['credentials']['password']

print('trying to get url: ', web_url)
print('trying to get username: ', uname)
print('trying to get password: ', pword)
print('first bird in the list: ', bird1)
print('list of calling birds: ', all_birds)

