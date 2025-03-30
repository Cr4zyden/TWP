def task(input_val: str) -> bool: #Основная функция решения задачи
    stack = [] 
    staples = {')' : '(',  #словарь для правильных комбинаций скобок
               ']' : '[',
               '}': '{',
               '(': '',
               '[': '',
               '{': ''}
    
    stack.append(input_val[0])
    for i in range(1, len(input_val)):
        temp_val = input_val[i]
        if len(stack) >0 and staples[temp_val] == stack[-1]:
            stack.pop()
        else:
            stack.append(temp_val)   
    
    if len(stack) == 0:
        return True
    return False


#TOODO:
def check_input(input_val: str) -> bool: #Функция проверки ввода
    if set(list(input_val)).issubset('(){}[]'): return True
    return False

if __name__ == '__main__': 
    print("Введите посл-ть скобок: ")
    while True:
        input_val = input()
        if check_input(input_val):
            break
        print("Ошибка ввода, попробуйте еще раз:  ")
    
    print(task(input_val))