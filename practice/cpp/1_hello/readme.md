# CMake 入门
编译一个Hello World工程

## 文件结构
```bash
.
├── CMakeLists.txt  # 配置文件
├── hello.cpp       # 函数实现
├── hello.h         # 函数声明
├── main.cpp        # 程序入口
└── readme.md  
```

## 步骤
编写`CMakeLists.txt`
```bash
cmake_minimum_required(VERSION 3.0)
project(HelloWorldProject)

# 添加可执行文件
add_executable(HelloWorld main.cpp hello.cpp)
```

在项目根目录下运行以下代码
```bash
mkdir build
cd build
cmake ..    # 配置项目
make        # 编译
```

## 
```bash
./HelloWorld
```