# 视觉感知

- [检测](detection/) 包括 [PyTorch IoU 与按类 NMS](detection/1.%20Non-Maximum%20Supression.ipynb)、[NumPy NMS 与匹配](detection/感知手撕.ipynb) 和 [CenterNet](detection/2.%20CenterNet.ipynb)。`nms.cc` 是使用 ATen Tensor 的参考片段。
- [跟踪](tracking/) 包括 [一维卡尔曼滤波](tracking/1.%20Kalman%20Filter.ipynb) 和 SORT。跟踪器使用 NumPy、SciPy 和 FilterPy，显示模式还需要 Matplotlib、scikit-image 和图像序列。
- [注意力与 ViT](attention/Transformer%20and%20ViT.ipynb) 包括缩放点积、掩码、多头注意力、归一化、图像分块和小型分类网络。PyTorch 示例可在 CPU 上运行。

```bash
python -m pip install -r vision/requirements.txt
python vision/detection/nms.py
python vision/tracking/sort.py --help
```

SORT 完整示例使用 MOT 格式的检测文件 `<seq_path>/<phase>/<sequence>/det/det.txt`。在 `vision/tracking/` 下运行可把生成的跟踪结果保存在该目录的 `output/`。

SORT 代码来自 [Alex Bewley 的 SORT 项目](https://github.com/abewley/sort)，保留原作者声明和 [GPL 许可文本](tracking/LICENSE)。
