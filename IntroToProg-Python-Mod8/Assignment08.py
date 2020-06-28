# ------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# TTaylor,6/1/20,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
import pickle

strFileName = 'products.pkl'

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    """

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def product_name(self):
        return self.__name

    @property
    def product_price(self):
        return self.__price

    @product_name.setter
    def product_name(self, value):
        self.__name = value

    @product_price.setter
    def product_price(self, value):
        self.__price = value


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
    """

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list
        :param file_name: (string) with name of file:
        :return: (list) of product objects
        """
        try:
            with open(file_name, "rb") as fileObject:
                return pickle.load(fileObject)
        except FileNotFoundError as e:
            print('\nHello, welcome to the Product List Document. \n'
                  'Because this is your first time here, I have no data to read to you --\n')
            return []


    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        with open(file_name, 'wb') as fileObject:
            pickle.dump(list_of_product_objects, fileObject)


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
            Menu of Options
            1) Show Current Data
            2) Add Data to the List
            3) Save Data to File & Exit Program
            ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Please select an option? [1 to 3] - ")).strip()
        print()
        return choice

    @staticmethod
    def print_current_product_list(list_of_products):
        """ Shows the current list
        :param list_of_products
        :return: nothing
        """
        print("**** The current List is: ****")
        for product in list_of_products:
            print(product.product_name + " | " + product.product_price)
        print("*************************")
        print()

    @staticmethod
    def input_new_product_data():
        name = input('Please enter Product Name: ')
        price = input('Please enter Product Price: ')
        if price == '':
            raise ValueError('There was no price entered')
        return Product(name, price)


# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while (True):
    # Show user a menu of options
    IO.print_menu_tasks()

    # Get user's menu option choice
    strChoice = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if strChoice == '1':
        IO.print_current_product_list(lstOfProductObjects)

    # Let user add data to the list of product objects
    elif strChoice.strip() == '2':
        try:
            product = IO.input_new_product_data()
            lstOfProductObjects.append(product)
        except ValueError as e:
            print(e)
        continue

    # let user save current data to file and exit program
    elif strChoice == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print("Your list has been saved! Goodbye!")
        break   # and Exit