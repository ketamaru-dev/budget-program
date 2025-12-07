#This file will be use for create doc which save .txt for first time
from budget import Category
from errors import WrongInput, CreateError
import json

#transaction file (type - json):
#date = {categories:{
#   "category1": {
#               "name_of_transaction": "name",
#               "limit_transaction": value,
#               "transactions": {
#                                   "date1": value
#                                   "date2": value
#                                       ...
#                                }
#                }
#   "category2": {...}
#                   },
#   COUNT_OF_CATEGORIES = value
#}


def touch_file(file_path='.'):
    try:
        with open(f'{file_path}\\budget_base.json', 'r') as file:
            return None
            
    except FileNotFoundError:
        isCreate = input('File not found, do you want to create it? (y/n)')
        if isCreate.lower() == 'y':
            with open(f'{file_path}\\budget_base.json', 'w') as file:
                fill_the_budget_file()
                print('File created!')
                return None
        else:
            raise CreateError
        
        

def fill_the_budget_file(file_path='.'):
    all_categories = []
    print("Welcome to create module of budget app,\n Fisrst step: create new category")
    all_categories.append(init_category())
    while isContinue_of_create():
         all_categories.append(init_category())

    save_budget_file({'categories':all_categories, 'count_categories': len(all_categories)})


def save_budget_file(budget_file, save_path='.'):
    with open(f'{save_path}\\budget_base.json', 'w') as file:
        json.dump(file, budget_file, ensure_ascii=False, indent=4)


def load_fudget_file(load_path='.'):
    with open(f'{load_path}\\budget_base.json', 'r') as file:
        budget_dict = json.load(file)
        return budget_dict

def isContinue_of_create():
    while True:
        try:
            isContinue = input('Do you want to continue category create? (y/n)')
            if isContinue.lower() == 'y':
                return True
            elif isContinue.lower() == 'n':
                return False
            else:
                raise WrongInput(isContinue)
        except WrongInput(isContinue):
            continue

def init_category() -> Category:
    name_of_cat = input("Enter the name of category: ")
    category_limit = float("Enter the limit of category: ")
    new_category = Category(name_of_cat, category_limit)
    print('Category created!')
    return new_category


if __name__ == '__main__':
    pass