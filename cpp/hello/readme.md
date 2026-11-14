# CMake 入门

`hello.h` 声明函数，`hello.cpp` 提供实现，`main.cpp` 调用它。CMake 将两个源文件编译并链接为 `HelloWorld`。

在本目录运行以下命令。也可以从仓库根目录按 [统一构建说明](../../README.md#c-示例) 构建。

```bash
cmake -S . -B build
cmake --build build --config Release
```

单配置生成器通常将程序放在 `build/HelloWorld`。Visual Studio 生成器将程序放在 `build/Release/HelloWorld.exe`。执行后输出 `Hello, World!`。
