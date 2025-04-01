#include <iostream>
#include <string>

using namespace std;

struct Stack {
    char val;
    Stack* next;
};

void push(Stack*& s, char val) {
    Stack* temp = new Stack;
    temp->val = val;
    temp->next = s;
    s = temp;
}

void pop(Stack*& s) {
    if (s == nullptr) return;
    Stack* temp = s;
    s = s->next;
    delete temp;
}

bool check_string(const string& input) {
    const string allowedChars = "(){}[]";
    return input.find_first_not_of(allowedChars) == string::npos;
}

bool task(const string& input) {
    Stack* s = nullptr;
    
    // Проверка на пустую строку
    if (input.empty()) return false;
    
    for (char c : input) {
        if (s == nullptr) {
            push(s, c);
            continue;
        }
        
        switch (c) {
            case '}':
                if (s->val == '{') pop(s);
                else push(s, c);
                break;
            case ')':
                if (s->val == '(') pop(s);
                else push(s, c);
                break;
            case ']':
                if (s->val == '[') pop(s);
                else push(s, c);
                break;
            default:
                push(s, c);
        }
    }
    bool result = (s == nullptr);
    // Очистка памяти
    while (s != nullptr) pop(s);
    
    return result;
}


int main() {
    string input;
    while (true) {
        cout << "Введите последовательность скобок: ";
        getline(cin, input);
        if (check_string(input)) break;
        cout << "Ошибка ввода! Используйте только скобки: (){}[]\n";
    }
    
    if (task(input))cout << "Последовательность правильная\n";
    else cout << "Последовательность неправильная\n";

    return 0;
}