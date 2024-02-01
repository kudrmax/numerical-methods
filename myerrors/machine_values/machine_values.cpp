#include <iostream>
#include <cmath>

template <typename T>
void print_zero() {
    int k = 0;
    T num = static_cast<T>(1);
    while (num != static_cast<T>(0)) {
        num = static_cast<T>(num / 2);
        k += 1;
    }
    std::cout << typeid(T).name() << " машинный ноль = 2^-" << k << std::endl;
}

template <typename T>
void print_infinity() {
    int k = 0;
    T num = static_cast<T>(1);
    while (num < std::numeric_limits<T>::max()) {
        num = static_cast<T>(num * 2);
        k += 1;
    }
    std::cout << typeid(T).name() << " машинная бесконечность = 2^" << k << std::endl;
}

template <typename T>
void print_epsilon() {
    int k = 0;
    T num = static_cast<T>(1);
    while (static_cast<T>(1.) + num > static_cast<T>(1.)) {
        num = static_cast<T>(num / 2);
        k += 1;
    }
    std::cout << typeid(T).name() << " машинное эпсилон = 2^-" << k << std::endl;
}

int main() {
    print_zero<float>();
    print_infinity<float>();
    print_epsilon<float>();
    std::cout << std::endl;

    print_zero<double>();
    print_infinity<double>();
    print_epsilon<double>();
    std::cout << std::endl;

    print_zero<long double>();
    print_infinity<long double>();
    print_epsilon<long double>();
    std::cout << std::endl;

    return 0;
}
