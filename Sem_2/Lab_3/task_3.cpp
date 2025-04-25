#include <iostream>

// Определение структуры узла бинарного дерева
struct TreeNode {
    int value; // Значение узла
    TreeNode* left; // Указатель на левого потомка
    TreeNode* right; // Указатель на правого потомка

    TreeNode(int val) : value(val), left(nullptr), right(nullptr) {}
};

// Функция для добавления значения в бинарное дерево поиска
TreeNode* insertIntoBST(TreeNode* root, int value) {
    if (!root) {
        return new TreeNode(value); // Если дерево пустое, создаем новый узел
    }

    if (value < root->value) {
        root->left = insertIntoBST(root->left, value); // Добавляем в левое поддерево
    } else {
        root->right = insertIntoBST(root->right, value); // Добавляем в правое поддерево
    }

    return root;
}

// Рекурсивная функция для нахождения максимального элемента в бинарном дереве
int findMaximumValue(TreeNode* root) {
    if (!root) {
        throw std::runtime_error("Дерево пустое"); // Если дерево пустое, выбрасываем исключение
    }
    if (!root->right) {
        return root->value; // Если правый потомок отсутствует, текущий узел - максимальный
    }
    return findMaximumValue(root->right); // Иначе ищем в правом поддереве
}

int main() {
    std::cout << "Введите числа через пробел (для завершения введите 0): ";

    TreeNode* root = nullptr;
    int value;

    while (std::cin >> value && value != 0) {
        root = insertIntoBST(root, value);
    }

    try {
        int maxValue = findMaximumValue(root);
        std::cout << "Максимальное значение в дереве: " << maxValue << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}
