#Here discribe exception can will be used in program

class MyTypeError(TypeError):
    def __init__(self, name_of_arg):
        super().__init__(self)
        self.problem_arg = name_of_arg

    def __str__(self):
        super().__str__()
        print(f'Error in variable {self.problem_arg}')


class WrongInput(Exception):
    def __init__(self, var=None):
        super().__init__(self)
        self.exc_var = var
    
    def __str__(self):
        if not self.exc_var == None:
            print(f'Error is occured, enter {self.exc_var} is wrong! Try again!')
        else:
            print(f'Error is occured. Try again!')

class CreateError(Exception):
    def __init__(self):
        super().__init__(self)
    
    def __str__(self):
        print('---Error of file create---')