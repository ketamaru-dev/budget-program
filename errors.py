#Here discribe exception can will be used in program

class MyTypeError(TypeError):
    def __init__(self, name_of_arg):
        super().__init__(self)
        self.problem_arg = name_of_arg

    def __str__(self):
        super().__str__()
        print(f'Error in variable {self.problem_arg}')
