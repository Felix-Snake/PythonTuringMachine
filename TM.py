
class TM(): # Turing Machine
    # По PEP8 здесь должно быть пояснение
    inp = ""
    outp = ""
    steps = 0
    current_status = "q1"
    head_current_position = 0
    break_count = 0
    break_count_max = 3

    def __init__(self, operations:dict)->None:
        self.operations = operations

    def __call__(self, inp):
        self.transformation(inp)#Стандартная функция. Будет работать если простотобратиться к объекту через TM(input)
    def __len__(self):
        return len(self.operations)

    def __add__(self, TM2):#plus
        pass

    def __sub__(self, TM2): # minus
        pass

    def transformation(self, inp:str):
        self.inp = inp
        print(self.inp)
        while self.current_status != "q0":
            self.steps = len(inp)
            step_out = self.operations[self.inp[self.steps - self.head_current_position - 1] + self.current_status]
        

            self._execute_operation(step_out)
            if self.break_count >= self.break_count_max:
                print("Stop process...")
                break
            print(f"↓ - {self.current_status}")
            print(self.outp)
            self.inp = self.outp
        
        #self.head_current_position += 1
        #self.current_status = stepout[1:]

    def _execute_operation(self, operation:str)->None:
        move_code = {
                "R":1,
                "C":0,
                "L":-1
                }
        self.outp = self.inp[:self.head_current_position] + operation[0] + self.inp[(self.head_current_position+1):]
        
        self.head_current_position += move_code[operation[1].upper()]

        if self.head_current_position >= len(self.inp): 
                                             self.inp += "0"
                                             self.break_count += 1
        

        self.current_status = operation[2:]


        
    def _del_null_elements(inp:str)->str:
        return str(int(inp))



if __name__ == '__main__':
    operations = {
        "0q1":"1Rq1",
        "1q1":"0Rq0"

        }
    t = TM(operations)
    t("00010")

