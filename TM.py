
class TM():
    """Turing Machine 
        operations : The dict of strings with instructions for Turing Machine
    """

    inp = ""
    outp = ""
    steps = 0
    current_status = "q1"
    head_current_position = 0
    break_count = 0
    break_count_max = 2

    def __init__(self, operations:dict)->None:
        self.operations = operations

    def __call__(self, inp:str)->None:
        """Standart_Function 
            inp : string of 0's and 1's for processing by a Turing Machine
        """
        self.transformation(inp)#The standard function. It will work if you just access the object via TM(input)

    def __len__(self):
        return len(self.operations)

    def transformation(self, inp:str):
        self.inp = inp
        print(self.inp)
        while self.current_status != "q0":
            self.steps = len(self.inp)
            step_out = self.operations[self.inp[self.head_current_position] + self.current_status]
        
            self._execute_operation(step_out)
            if self.break_count > self.break_count_max:
                print("Stop process...")
                print("The Turing Machine never stop")
                print(f"↓ - {self.current_status}")
                print(self.outp)
                self.inp = self.outp

                break

            print(f"↓ - {self.current_status}")
            print(self.outp)
            self.inp = self.outp
        

    def _execute_operation(self, operation:str)->None:
        move_code = {
                "R":1,
                "C":0,
                "L":-1
                }
        self.outp = self.inp[:self.head_current_position] + operation[0] + self.inp[(self.head_current_position+1):]
        
        self.head_current_position += move_code[operation[1].upper()]

        if self.head_current_position > (len(self.outp) - 1): 
            self.outp += "0"
            self.break_count += 1
        

        self.current_status = operation[2:]


        
    def _del_null_elements(inp:str)->str:
        return str(int(inp))



if __name__ == '__main__':
    operations = {
        "0q1":"1Rq1",
        "1q1":"0Rq2",
        "0q2":"0Rq2",
        "1q2":"1Rq1",
        "1q2":"1Rq0"
        }

    t = TM(operations)
    t(input())

