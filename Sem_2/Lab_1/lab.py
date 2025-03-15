class TuringMachine:
    def __init__(self, input_tape):
        # Инициализация ленты
        self.tape = list(input_tape)
        self.head_position = 0
        self.current_state = 'start'
        self.m_count = 0
        self.n_count = 0
        self.count = 0
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
            # Ищем начало второго числа'
            
            ('second_num', '|'): ('second_num', '|', 'R'),
            ('second_num', 'B'): ('end_find', 'B', 'R'),
            ('second_num', 'A'): ('end_find', 'A', 'R'),

            ('end_find', '='): ('halt', '=', 'S'),

        }

    def run(self):
        # Выполнение программы
        while self.current_state != 'halt':
            current_symbol = self.tape[self.head_position] if self.head_position < len(self.tape) else ''
            if (self.current_state, current_symbol) in self.rules:
                new_state, new_symbol, move = self.rules[(self.current_state, current_symbol)]
                print(new_symbol, self.current_state)
                if new_symbol == '|':
                    self.count += 1

                if self.head_position < len(self.tape):
                    self.tape[self.head_position] = new_symbol
                    if self.current_state in ('first_num', 'second_num'):
                        if new_symbol == 'A':
                            self.m_count = self.count
                            self.count = 0
                        elif new_symbol == 'B':
                            self.n_count = self.count
                            self.count = 0 
                else:
                    self.tape.append(new_symbol)  # Расширяем ленту, если нужно
                
                self.current_state = new_state
                if move == 'R':
                    self.head_position += 1
                elif move == 'L':
                    self.head_position -= 1
            else:
                break

        # Вывод результата
        print(''.join(self.tape))
        print(self.m_count, self.n_count)

if __name__ == "__main__":
    input_tape = input("Введите ленту (например, '|||A|||B='): ")
    tm = TuringMachine(input_tape)
    tm.run()