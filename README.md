# Python列表与二分法课程动画

使用 Manim 制作的 Python 列表和查找算法教学动画视频。

## 作者
温程远

## 项目简介

本项目包含一系列使用 Manim 制作的教学动画，涵盖以下内容：

1. **Python 列表基础** (`list_basics_animation.py`) - 新增
   - 列表的定义和特性
   - 列表的创建方法
   - 索引访问机制
   - 基本列表操作
   - 引出查找问题

2. **线性查找** (`linear_search_animation.py`)
   - 线性查找算法的演示
   - 逐个元素检查的过程
   - 适用场景和时间复杂度

3. **二分查找** (`binary_search_animation.py`)
   - 二分查找算法的演示
   - low、high、mid 指针的移动
   - 有序列表的查找优化
   - 时间复杂度分析

4. **查找峰值** (`find_peak_animation.py`)
   - 峰值查找算法演示
   - 二分法的应用场景

## 环境配置

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

或手动安装：

```bash
pip install manim
pip install numpy
```

### 2. 系统要求

- Python 3.7+
- FFmpeg（用于视频渲染）
- LaTeX（可选，用于数学公式渲染）

## 使用方法

### 渲染单个动画

```bash
# 渲染 Python 列表基础动画（推荐从这个开始）
python list_basics_animation.py

# 渲染线性查找动画
python linear_search_animation.py

# 渲染二分查找动画
python binary_search_animation.py

# 渲染峰值查找动画
python find_peak_animation.py
```

### 使用 Manim 命令行

```bash
# 生成高质量 4K 视频
manim -pqh list_basics_animation.py ListBasicsAnimation

# 生成中等质量视频（更快）
manim -pqm list_basics_animation.py ListBasicsAnimation

# 生成低质量预览
manim -pql list_basics_animation.py ListBasicsAnimation
```

### 合并视频

如果需要将多个动画合并成一个完整的课程视频：

```bash
python merge_videos.py
```

## 视频输出

默认配置：
- 分辨率：3840x2160（4K）
- 帧率：30 FPS
- 背景：白色
- 字体：SimSun（宋体）

渲染后的视频文件会保存在 `media/videos/` 目录下。

## 课程结构

建议按以下顺序观看/渲染动画：

1. **list_basics_animation.py** - 了解 Python 列表基础知识
2. **linear_search_animation.py** - 学习线性查找算法
3. **binary_search_animation.py** - 学习二分查找算法
4. **find_peak_animation.py** - 了解二分法的其他应用

## 特色功能

- ✅ 统一的视觉风格和配色方案
- ✅ 清晰的中文注释和讲解
- ✅ 逐步演示算法执行过程
- ✅ 高亮显示关键步骤
- ✅ 代码和可视化同步展示
- ✅ 4K 高清画质
- ✅ 平滑的动画过渡

## 颜色方案

```python
TEXT_COLOR = "#000000"      # 黑色文字
SQUARE_COLOR = "#95A5A6"     # 灰色方块边框
HIGHLIGHT_COLOR = "#2ECC71"  # 绿色高亮
INDEX_COLOR = "#3498DB"      # 蓝色索引
CODE_COLOR = "#E67E22"       # 橙色代码
ELEMENT_COLOR = "#9B59B6"    # 紫色元素
```

## 文件说明

- `list_basics_animation.py` - Python列表基础动画（新增）
- `linear_search_animation.py` - 线性查找动画
- `binary_search_animation.py` - 二分查找动画
- `find_peak_animation.py` - 峰值查找动画
- `merge_videos.py` - 视频合并工具
- `extract_video.py` - 视频提取工具
- `requirements.txt` - Python依赖列表

## 常见问题

### Q: 渲染速度很慢怎么办？
A: 可以先使用 `-ql` 参数生成低质量预览，确认无误后再使用 `-qh` 生成高质量版本。

### Q: 中文字体显示异常？
A: 确保系统中安装了 SimSun（宋体）字体。Linux 用户可能需要安装中文字体包。

### Q: 如何修改视频分辨率？
A: 修改代码末尾的 `config.pixel_height` 和 `config.pixel_width` 参数。

## 许可证

本项目仅用于教学目的。

## 联系方式

作者：温程远
