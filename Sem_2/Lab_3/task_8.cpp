#include <iostream>
#include <string>

using namespace std;

// Состояния для левой головки (включая конечное)
enum LeftState {
    L_START,
    L_A,
    L_X,
    L_INVALID,
    L_ACCEPT  // Единое конечное состояние
};

// Состояния для правой головки
enum RightState {
    R_START,
    R_A,
    R_X,
    R_INVALID
};

bool is_balanced(const string &word) {
    LeftState l_state = L_START;
    RightState r_state = R_START;
    int head1 = 0;
    int head2 = word.size() - 1;
    int balance = 0;

    while (l_state != L_INVALID && r_state != R_INVALID && l_state != L_ACCEPT && head1 < head2) {
        // Обработка левой головки
        if (l_state != L_ACCEPT && head1 <= head2) {
            char c = word[head1];
            switch (l_state) {
                case L_START:
                case L_A:
                    if (c == 'a') {
                        balance++;
                        l_state = L_A;
                        head1++;
                    } else if (c == 'x') {
                        balance--;
                        l_state = L_X;
                        head1++;
                    } else {
                        l_state = L_INVALID;
                    }
                    break;
                case L_X:
                    if (c == 'a') {
                        balance++;
                        l_state = L_A;
                        head1++;
                    } else if (c == 'x') {
                        balance--;
                        head1++;
                    } else {
                        l_state = L_INVALID;
                    }
                    break;
                default:
                    break;
            }
        }

        // Обработка правой головки
        if (head1 <= head2 && r_state != R_INVALID) {
            char c = word[head2];
            switch (r_state) {
                case R_START:
                case R_A:
                    if (c == 'a') {
                        balance++;
                        r_state = R_A;
                        head2--;
                    } else if (c == 'x') {
                        balance--;
                        r_state = R_X;
                        head2--;
                    } else {
                        r_state = R_INVALID;
                    }
                    break;
                case R_X:
                    if (c == 'a') {
                        balance++;
                        r_state = R_A;
                        head2--;
                    } else if (c == 'x') {
                        balance--;
                        head2--;
                    } else {
                        r_state = R_INVALID;
                    }
                    break;
                default:
                    break;
            }
        }

        // Проверка условий для перехода в ACCEPT
        if (head1 > head2 && balance == 0) {
            l_state = L_ACCEPT;
        }
    }

    return l_state == L_ACCEPT;
}

int main() {
    string word;
    cout << "Введите слово из символов 'a' и 'x': ";
    cin >> word;

    if (is_balanced(word)) {
        cout << "Слово допущено: количество 'a' и 'x' одинаково." << endl;
    } else {
        cout << "Слово не допущено." << endl;
    }

    return 0;
}
