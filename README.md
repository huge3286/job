# job · 秋招算法与工程练习

算法原理、手撕代码、C++ 工程示例和视觉感知笔记。算法 Notebook 按主题组织，公司的笔试题按原题号保存。

| 目录 | 内容 |
| --- | --- |
| [algorithms/](algorithms/) | 二分、排序、前缀和、图、动态规划、字符串匹配和 LeetCode 专题 |
| [cpp/](cpp/) | C++ 基础笔记、Hello World、快速排序测试和分组题 |
| [vision/](vision/) | IoU、NMS、CenterNet、Kalman Filter、SORT、Transformer 和 ViT |
| [interviews/](interviews/) | 按公司整理的笔试题与来源未注明的练习 |

## 算法笔记

建议从 [二分](algorithms/Array/二分.ipynb)、[前缀和](algorithms/Array/前缀和.ipynb) 和 [图的遍历](algorithms/Graph/图的遍历.ipynb) 开始。算法示例使用 Python 3.10 或更新版本的标准库。Notebook 可以在 GitHub 上阅读，也可在本地用 JupyterLab 运行。

```bash
python -m pip install jupyterlab
python -m jupyterlab
```

## C++ 示例

从根目录运行，需安装 CMake 3.16 或更新版本、支持 C++17 的编译器和 GoogleTest。Linux 上可安装发行版的 `libgtest-dev`。使用 Visual Studio 时，可在配置阶段通过 `CMAKE_PREFIX_PATH` 指向与编译器架构匹配的 GoogleTest 安装目录。

```bash
cmake -S . -B build
cmake --build build --config Release
ctest --test-dir build -C Release --output-on-failure
```

只构建 Hello World 和分组题时，可在配置阶段加 `-DBUILD_TESTING=OFF`，此时无需 GoogleTest。

## 视觉感知

```bash
python -m pip install -r vision/requirements.txt
python vision/detection/nms.py
```

[视觉笔记索引](vision/) 列出了每个示例的依赖和运行方式。
