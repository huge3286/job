## Template
实现一个自适应参数类型的打印函数（这对Python来说根本不是事），如下所示
```cpp
template <typename T>
void print(const T& x) {
    for (const auto& i : x) {
        std::cout << i << ' ';
    }
    std::cout << std::endl;
}
```