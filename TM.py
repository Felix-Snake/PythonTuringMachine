
class TM(): # Turing Machine
    # По PEP8 здесь должно быть пояснение
    inp = ""
    outp = ""
    steps = 0
    current_status = ""
    head_current_position = 0

    def __init__(self, operations:dict)->None:
        self.operarions = operations

    def __call__(self, inp):
        self.transformation()#Стандартная функция. Будет работать если простотобратиться к объекту через TM(input)
    def __len__(self):
        return len(self.operations)

    def __add__(self, TM2):#plus
        pass

    def __sub__(self, TM2): # minus
        pass

    def transformation(self, inp:str):
        self.steps = len(inp)
        step_out = operations[self.inp[self.steps - self.head_current_position - 1] + current_status]
        self.inp = inp.replace(inp[steps - head_current_position - 1], stepout[0])

        self.head_current_position += 1
        self.current_status = stepout[1:]

    def _execute_operation(self, operation:str)->None:
        move_code = {
                "R":1,
                "C":0,
                "L":-1
                }
        self.outp = self.inp[:self.head_current_position] + operation[0] + self.inp[(self.head_current_position+1):]
        
        self.head_current_position += move_code[operation[1].upper()]

        self.current_status = operation[2:]

        
    def _move_head_position():
        pass

    def _del_null_elements(inp:str)->str:
        return str(int(inp))





