class TuringMachine:
    def __init__(self, input_tape):
        # Инициализация ленты
        self.tape = list(input_tape)
        self.head_position = 0
        self.current_state = 'start'
        self.m_count = 0
        self.n_count = 0
        self.count = 0
        self.result_count = 0
        self.rules = {
            # Начальное состояние: ищем первое число
            ('start', '|'): ('first_num', '|', 'R'),
            ('start', 'A'): ('start', 'A', 'R'),
            ('start', 'B'): ('start', 'B', 'R'),
            ('start', '='): ('start', '=', 'R'),

            # Ищем конец первого числа '
            ('first_num', '|'): ('first_num', '|', 'R'),
            ('first_num', 'A'): ('second_num', 'A', 'R'),
            ('first_num', 'B'): ('second_num', 'B', 'R'),
            
            # Ищем конец второго числа'
            ('second_num', '|'): ('second_num', '|', 'R'),
            ('second_num', 'B'): ('end_find', 'B', 'R'),
            ('second_num', 'A'): ('end_find', 'A', 'R'),

            ('end_find', '='): ('append_result', '=', 'R'),
            ('append_result', '_'): ('append_result', '|', 'R')
        }

    def gui(self):
        print(f"{' ' * (self.head_position)}▼")


    def run(self):
        # Выполнение программы
        while self.current_state != 'halt':
            if self.head_position >= len(self.tape):
                self.tape.append('_')
            self.gui()
            current_symbol = self.tape[self.head_position] 
            if (self.current_state, current_symbol) in self.rules:
                new_state, new_symbol, move = self.rules[(self.current_state, current_symbol)]
                print(''.join(self.tape))
                if new_symbol == '|':
                    self.count += 1
                elif new_symbol == '=':
                    self.result_count = self.m_count * self.n_count
                
                self.tape[self.head_position] = new_symbol
                if self.current_state in ('first_num', 'second_num'):
                    if new_symbol == 'A':
                        self.m_count = self.count
                        self.count = 0
                    elif new_symbol == 'B':
                        self.n_count = self.count
                        self.count = 0 
                if self.current_state == 'append_result':
                    self.result_count -= 1
                
                self.current_state = new_state
                if move == 'R':
                    self.head_position += 1
                elif move == 'L':
                    self.head_position -= 1
                if new_state == 'append_result' and self.result_count == 0:
                    self.current_state = 'halt'
                    continue
            else:
                break

        # Вывод результата
        print(''.join(self.tape))

def input_check(inp_str):
    st = list(set(list(inp_str)))
    if len(st) in (4, 3):
        if sorted(st) == sorted(('|', 'A', 'B', '=')):
            return True
        if sorted(st) == sorted(('A', 'B', '=')):
            return True
    return False

if __name__ == "__main__":
    while True:
        input_tape = input("Введите ленту (например, '|||A|||B='): ")
        if input_check(input_tape):
            break
        else:
            print("Введите ленту правильно")
    tm = TuringMachine(input_tape)
    tm.run()