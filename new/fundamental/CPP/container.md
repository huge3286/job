# STL Container

## array
```cpp
template<
    class T,
    std::size_t N
> struct array;
```

用法和C语言数组类似，简单来说就是分配一个连续的内存空间保存数组
```cpp
int a[10];  // c-tpye
std::array<int, 10> a;  // array
std::iota(a.begin(), a.end(), 0);
std::sort(a.begin(), a.end(), [](int x, int y){ return x > y; });
std::swap(a.at(0), a.at(4));
```

数组是定长的，只能修改内容没法修改大小


## vector
```cpp
template<
    class T,
    class Allocator = std::allocator<T>
> class vector;
```

向量，也叫做可变长数组，用法和Python的list类似。  
std::allocator 是 std::vector 模板的默认模板参数，不需要设置，用于分配和释放 vector 内部元素的内存。这允许您在创建 std::vector 实例时指定自定义的内存分配器，但通常情况下，您可以直接使用 std::vector 的默认内存分配器，而不必担心内存管理的细节。
```cpp
vector<T> v; // 采用模版类实现，默认构造函数
vector<T> v(T* v1.begin(), T* v1.end()); // 将v1[begin(), end())区间中的元素拷贝给本身
vector<T> v(int n, T elem); // 将n个elem拷贝给本身
vector<T> v(const vector<T> v1); // 拷贝构造函数
```
常见用法
```cpp
vector<int> a(9, 0);
std::iota(a.begin(), a.end(), 0);

// append & pop
a.push_back(9)
a.pop_back()

// 构造切片数组
vector<int> b(a.begin() + 3, a.begin() + 8);
// 删除指定范围内的元素
a.erase(a.begin()+5, a.begin()+7);
```
提供常数时间的数组访问，末尾元素添加和删除

## string
本质上是一个动态的$char$数组
```cpp
string(const string& str);  // 从另一个字符串构造
string(const char* s);      // 从char风格字符串构建
string(int n, char c);      // 长为n 元素为c的字符串
```

下面演示string的常见操作
```cpp
string a = "helloworld";
string b = a.substr(0, 5);  // 两个参数分别是 start & len

a.append('z');  // 等价于 += 
a.pop_back();
a.erase(a.begin()+5, a.begin()+7);
```

## deque
双端队列，可以在头部实现O(1)的插入，没有容量的概念，因为它是由动态的分段连续空间组合而成，随时可以增加一块新的空间并链接起来。

图示为双端队列原理，可以看做是 **双向链表+动态数组**
![双端队列原理](https://3445412966-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F4jcp9JrFSUV0Enu5fcXK%2Fuploads%2FRZ95iPL2Vl8mSTALXMwD%2FIMG_1584.jpeg?alt=media&token=9fefe149-9396-4414-9867-3244c5e1bd7f)

```cpp
deque<T> deqT; // 默认构造函数
deque(beg, end); // 构造函数将[beg, end)区间中的元素拷贝给本身
deque(int n, T elem); // 构造函数将n个elem拷贝给本身
deque(const deque& deq); // 拷贝构造函数
```
双端队列常见用法

```cpp
push_back(T elem); // 在容器尾部添加一个元素
push_front(T elem); // 在容器头部插入一个元素

pop_back(); // 删除容器最后一个数据
pop_front(); // 删除容器第一个数据

T& at(int idx); // 返回索引idx所指的数据
T& operator[](int idx); // 返回索引idx所指的数据

T& front(); // 返回首元素的引用
T& back(); // 返回尾元素的引用
```

## stack
栈是一种先进后出的数据结构，只有一个出口
> 栈不允许遍历，没有迭代器
```cpp
stack<T> stkT; // 默认构造函数，stack采用模版类实现
stack(const stack& stk); // 拷贝构造函数
```

常见用法
```cpp
stack& operator=(const stack& stk); // 重载赋值操作符

void push(T elem); // 向栈顶添加元素
void pop(); // 从栈顶移除第一个元素
T& top(); // 返回栈顶元素
```

## queue
队列是一种后进后出的数据结构，只有一个出口一个入口
> 栈不允许遍历，没有迭代器
```cpp
queue<T> queT; // queue对象的默认构造函数形式，采用模版类实现
queue(const queue& que); // 拷贝构造函数
```
常见用法
```cpp
void push(T elem); // 往队尾添加元素
void pop(); // 从队头移除第一个元素
T& back(); // 返回最后一个元素
T& front(); // 返回第一个元素
```

## list
是双向链表
