# ------------------------------------ #
# Title: <name of script here>
# Description: <description of script>
# ChangeLog: (Who, When, What)
# <Example TTaylor, 1/1/2020, Created Script>
# ------------------------------------ #

# -- Data -- #
import pickle
import sys

vegList = ['cucumber', 'lettuce', 'real pickle']


# -- Processing -- #
def write_to_file(listToWrite):
    with open('vegList.pkl', 'wb') as vegpickle:
        print(listToWrite)
        pickle.dump(listToWrite, vegpickle)


def read_file():
    with open('vegList.pkl', 'rb') as vegpickle:
        readOut = pickle.load(vegpickle)
        print(readOut)
        return readOut


# -- Presentation -- #
def get_user_input():
    vegItem = input('Enter a vegetable: ')
    if len(vegItem) == 0:
        raise ValueError('Error: You didn\'t type anything')
    return vegItem


# -- Main Script -- #
try:
    fileData = read_file()
except FileNotFoundError as e:
    print('\nHello, welcome to the veg editor. \n'
          'Because this is your first time here, I have no data to read to you --\n')
    fileData = vegList
except pickle.UnpicklingError as e:
    print('Oops! Someone has tampered with the vegList.pkl file. \n  !! Please remove the file.')
    sys.exit(1)

try:
    fileData.append(get_user_input())
    write_to_file(fileData)
except ValueError as e:
    print(e)

