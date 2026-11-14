# Python 入门

- `list` 适合随机访问和尾部追加。做队列时用 `collections.deque`，从两端插入和移除都是常数时间。
- `dict` 记录键到值的映射，`set` 用于去重和成员查询，`collections.Counter` 用于计数。
- `bisect_left` 在有序序列中查找第一个大于等于目标值的位置，`bisect_right` 查找第一个严格大于目标值的位置。
- `heapq` 维护小根堆。堆顶是最小元素，整个列表没有全局排序。
- `functools.cache` 适用于参数可哈希、同一输入总得到同一结果的递归子问题。

```python
from bisect import bisect_left, bisect_right
from collections import Counter, deque
from heapq import nsmallest

values = [1, 2, 2, 4]
assert bisect_left(values, 2) == 1
assert bisect_right(values, 2) == 3
assert Counter(values)[2] == 2
assert deque(values).popleft() == 1
assert nsmallest(2, [4, 1, 2]) == [1, 2]
```

PyTorch 前向计算从 [注意力与 ViT](../vision/attention/Transformer%20and%20ViT.ipynb) 的小张量示例入手。
