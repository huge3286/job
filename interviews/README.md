# 笔试练习

[按公司整理的题解](company-exams/) 保留了原来的日期和题号。脚本使用标准输入，部分历史题解只有代码或注释。

[小米手机通信校准](company-exams/xiaomi/09023.py) 通过二分定位目标频道的相邻记录。题面和样例参见 [2023 年 9 月 2 日小米笔试记录](https://cloud.tencent.com/developer/article/2327241)。

[原根目录的两道题](undated/) 缺少完整原题。回文题按不同回文字符串计数并对 `10^9 + 7` 取模。树上题以 1 为根，按输入顺序覆盖子树，最终输出节点权值和。

```bash
python interviews/company-exams/xiaomi/09023.py
```

示例输入为两行。

```text
2800
1950:10 2000:15 3000:9
```

输出为 `9.0`。
