#This file will be use for create doc which save .txt for first time
from budget import Category, Transaction

def check_file_exists(file_path='.'):
    try:
        with open(f'{file_path}\\budget_base.txt', 'r') as file:
            fill = file.read()
            if fill == '':
                return False
            else:
                return True
            
    except FileNotFoundError:
        with open(f'{file_path}\\budget_base.txt', 'w') as file:
            pass
        print('File created!')
        check_file_exists(file_path)
        

def read_file(file_path):
    if check_file_exists(file_path='.'):
        with open(f'{file_path}\\budget_base.txt', 'r') as file:
            fill = file.read()
            print(fill)
    else:
        fill_the_file()


def fill_the_budget_file(file_path='.'):
    with open(f'{file_path}\\budget_base.txt', 'w') as file:
        pass
