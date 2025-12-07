#This program created by ketamaru v0.01
#Easy ASCII budger controller



from errors import MyTypeError, WrongInput

class Category:
#   vars: self.transactions(dist) - stores all transactions
#         self.category name - stores name of category
#         self.limit - stores limit of category

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
        
        #create new transaction-dict {'date': amount_of_transaction}
        self.transaction = {}

    def add_waste(self):  #the method is add new transaction to category
        summ = float(input('Enter the amount of transaction: '))
        date = input('Enter the date in format YEAR:MONTH:DAT (if empty, created currently date): ')
        if date == '':
            from datetime import datetime
            date = datetime.now().strftime("%Y-%m-%d")
        new_transaction = Transaction(summ, date)
        self.transaction[len(self.transaction) + 1] = new_transaction
        self.check_limit()
    
    def check_limit(self):  #this method is check if limit is out
        total_amount = self.count_total()
        if self.limit >= total_amount:
            print(f"It's ok you in limit\n Current limit is {total_amount}/{self.limit}")
            return True
        else:
            print(f"You limit is full, stop it \n Current limit is {total_amount}/{self.limit}")
            return False
    
    def count_total(self):  #this method is count all transactions
        total = 0
        for date_key in self.transaction:
            total += self.transaction[date_key]
        return total

    def get_all_transactions(self):
        category_transaction = []
        for date_key in self.transaction:
            category_transaction.append(self.transaction[date_key].get)
        self.show_all_transactions(category_transaction)
        
    def show_all_transactions(self, all_transaction):
        need = input('Show all transactions? (y/n): ')
        try:
            if need.lower() == 'y' or need.lower() =='n':
                print(all_transaction)          #-------------------------------THIS PLACE WILL BE CHANGED-------------------------------
            else:
                raise WrongInput(need)
        except WrongInput:
            self.show_all_transactions(all_transaction)

class Transaction:

    def __init__(self, amount_of_transaction: str, date_of_transaction: str):
        
        #check type of limit var (must be float)
        if not type(amount_of_transaction) == float:   
            raise MyTypeError(amount_of_transaction)
        else:
            self.amount_of_transaction = amount_of_transaction

        #check type of date var (must be str)
        if not type(date_of_transaction) == str:   
            raise MyTypeError(date_of_transaction)
        else:
            self.date_of_transaction = date_of_transaction
    
    def get_amount(self):
        return self.amount_of_transaction

    def get_transaction(self):
        return self.date_of_transaction, self.amount_of_transaction


if __name__ == '__main__':
    pass