#include <iostream>
#include <cmath>
#include <unordered_map>
#include <string>

template <typename T>
std::string print_type() {
    std::unordered_map<std::string, std::string> m_types;
    m_types[typeid(float).name()] = "float";
    m_types[typeid(double).name()] = "double";
    m_types[typeid(long double).name()] = "long double";
    return m_types[typeid(T).name()];
}

template <typename T>
void print_zero() {
    int k = 0;
    T num = 1;
    while (num != static_cast<T>(0)) {
        num /= 2;
        k += 1;
    }
    std::cout << print_type<T>() << " машинный ноль = 2^-" << k << std::endl;
}

template <typename T>
void print_infinity() {
    int k = 0;
    T num = 1;
    while (num < std::numeric_limits<T>::max()) {
        num *= 2;
        k += 1;
    }
    std::cout << print_type<T>() << " машинная бесконечность = 2^" << k << std::endl;
}

template <typename T>
void print_epsilon() {
    int k = 0;
    T num = 1;
    while (static_cast<T>(1) + num > static_cast<T>(1)) {
        num /= 2;
        k += 1;
    }
    std::cout << print_type<T>() << " машинное эпсилон = 2^-" << k << std::endl;
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
