#This program created by ketamaru v0.01
from errors import MyTypeError 

class Category:

#initializing category
    def __init__(self, name_of_category: str, limit: float):
        
        #check type of name_of_category var (must be str)
        if not type(name_of_category) == str:
            raise MyTypeError(name_of_category)
        else:
            self.category_name = name_of_category
            
        #check type of limit var (must be float)

        if not type(limit) == float:        
            raise MyTypeError(limit)
        else:
            self.limit = limit
        self.curent_spending = 0
    
    def add_waste(self, spend: Transaction):
        pass

class Transaction:

    def __init__(self, amount_of_transaction: float, name_of_transaction: str, date_of_transaction: str):
        
        #check type of name_of_transaction var (must be str)
        if not type(name_of_transaction) == str:
            raise MyTypeError(name_of_transaction)
        else:
            self.name_of_transaction = name_of_transaction

        #check type of limit var (must be float)
        if not type(amount_of_transaction) == float:   
            raise MyTypeError(amount_of_transactiont)
        else:
            self.amount_of_transaction = amount_of_transaction

        #check type of date var (must be str)
        if not type(date_of_transaction) == str:   
            raise MyTypeError(date_of_transaction)
        else:
            self.date_of_transaction = date_of_transaction



if __name__ == '__main__':
    pass