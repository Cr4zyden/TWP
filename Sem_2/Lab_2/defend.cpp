#include <iostream>

struct Node {
    int data;       
    Node* next;     
};

void append(Node*& head, int value) {
    Node* newNode = new Node; 
    newNode->data = value;    
    newNode->next = nullptr;  

    if (head == nullptr) {
        head = newNode;
    } else {
        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }
}

void print_list(const Node* head) {
    const Node* current = head;
    while (current) {
        std::cout << current->data << " ";
        current = current->next;
    }
    std::cout << std::endl;
}

void remove_duplicates(Node* head) {
    Node* current = head; // 
    while (current !=nullptr) {
        Node* runner = current; 
        while (runner and runner->next) {
            if (runner->next->data == current->data) {
                Node* duplicate = runner->next;
                runner->next = runner->next->next;
                delete duplicate; 
            } else {
                runner = runner->next;
            }
        }
        current = current->next;
    }
}

int main() {
    Node* head = nullptr; // Инициализация пустого списка

    int n; // Количество элементов
    std::cout << "Введите количество элементов: ";
    std::cin >> n;

    std::cout << "Введите элементы списка: ";
    for (int i = 0; i < n; ++i) {
        int value;
        std::cin >> value;
        append(head, value); // Добавляем элементы в список
    }

    std::cout << "Исходный список: \n";
    print_list(head);

    remove_duplicates(head);

    std::cout << "Список без дубликатов: \n";
    print_list(head);

    // Освобождаем память

    return 0;
}