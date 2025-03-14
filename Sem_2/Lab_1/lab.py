class TuringMachine:
    def __init__(self, input_tape):
        # Инициализация ленты
        self.tape = list(input_tape)
        self.head_position = 0
        self.current_state = 'start'
        self.rules = {
            # Начальное состояние: ищем первое число (m)
            ('start', '|'): ('find_m_end', '|', 'R'),
            ('start', 'A'): ('start', 'A', 'R'),
            ('start', 'B'): ('start', 'B', 'R'),
            ('start', '='): ('start', '=', 'R'),

            # Ищем конец первого числа (m), помеченного 'A'
            ('find_m_end', '|'): ('find_m_end', '|', 'R'),
            ('find_m_end', 'A'): ('find_n_start', 'A', 'R'),

            # Ищем начало второго числа (n), помеченного 'B'
            ('find_n_start', '|'): ('find_n_end', '|', 'R'),
            ('find_n_start', 'B'): ('find_n_end', 'B', 'R'),

            # Ищем конец второго числа (n), помеченного 'B'
            ('find_n_end', '|'): ('find_n_end', '|', 'R'),
            ('find_n_end', '='): ('go_to_start', '=', 'L'),

            # Возвращаемся к началу первого числа (m)
            ('go_to_start', '|'): ('go_to_start', '|', 'L'),
            ('go_to_start', 'A'): ('go_to_start', 'A', 'L'),
            ('go_to_start', 'B'): ('go_to_start', 'B', 'L'),
            ('go_to_start', '='): ('go_to_start', '=', 'L'),
            ('go_to_start', ''): ('copy_m', '', 'R'),  # Достигли начала ленты

            # Копируем первое число (m) и перемещаемся ко второму числу (n)
            ('copy_m', '|'): ('copy_m', '|', 'R'),
            ('copy_m', 'A'): ('copy_n', 'A', 'R'),
            ('copy_m', 'B'): ('copy_n', 'B', 'R'),
            ('copy_m', '='): ('copy_m', '=', 'R'),

            # Копируем второе число (n) и начинаем умножение
            ('copy_n', '|'): ('copy_n', '|', 'R'),
            ('copy_n', 'B'): ('multiply', 'B', 'R'),

            # Умножение: добавляем результат после знака =
            ('multiply', '|'): ('multiply', '|', 'R'),
            ('multiply', '='): ('write_result', '=', 'R'),
            ('multiply', ''): ('write_result', '|', 'L'),  # Достигли конца ленты

            # Записываем результат умножения
            ('write_result', '|'): ('write_result', '|', 'L'),
            ('write_result', '='): ('halt', '=', 'S'),  # Завершаем программу
        }

    def run(self):
        # Выполнение программы
        while self.current_state != 'halt':
            current_symbol = self.tape[self.head_position] if self.head_position < len(self.tape) else ''
            if (self.current_state, current_symbol) in self.rules:
                new_state, new_symbol, move = self.rules[(self.current_state, current_symbol)]
                if self.head_position < len(self.tape):
                    self.tape[self.head_position] = new_symbol
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


if __name__ == "__main__":
    input_tape = input("Введите ленту (например, '|||A|||B='): ")
    tm = TuringMachine(input_tape)
    tm.run()