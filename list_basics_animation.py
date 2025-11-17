from manim import *

class ListBasicsAnimation(Scene):
    def __init__(self):
        super().__init__()
        # 设置背景颜色为白色
        self.camera.background_color = "#FFFFFF"

        # 优化颜色方案（与其他动画保持一致）
        self.TEXT_COLOR = "#000000"      # 黑色文字
        self.SQUARE_COLOR = "#95A5A6"     # 柔和的灰色方块边框
        self.HIGHLIGHT_COLOR = "#2ECC71"  # 清新的绿色
        self.INDEX_COLOR = "#3498DB"      # 明亮的蓝色
        self.CODE_COLOR = "#E67E22"       # 温暖的橙色
        self.ELEMENT_COLOR = "#9B59B6"    # 优雅的紫色

        # 创建水印
        watermark = Text(
            "作者：温程远",
            font="SimSun",
            color=self.TEXT_COLOR,
            font_size=24
        ).to_corner(DR, buff=0.3)
        watermark.set_opacity(0.3)
        self.add(watermark)

    def construct(self):
        # ====== 第一部分：什么是列表 ======
        title = Text("Python 列表基础", font="SimSun", color=self.TEXT_COLOR, font_size=48)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # 列表定义
        definition = Text(
            "列表(List)是Python中最常用的数据结构之一",
            font="SimSun",
            color=self.TEXT_COLOR,
            font_size=32
        ).next_to(title, DOWN, buff=0.8)

        self.play(Write(definition))
        self.wait(1)

        # 列表特性
        features = VGroup(
            Text("• 有序：元素按添加顺序排列", font="SimSun", color=self.TEXT_COLOR, font_size=28),
            Text("• 可变：可以修改、添加、删除元素", font="SimSun", color=self.TEXT_COLOR, font_size=28),
            Text("• 可重复：允许存储重复的元素", font="SimSun", color=self.TEXT_COLOR, font_size=28),
            Text("• 支持索引：通过索引快速访问元素", font="SimSun", color=self.TEXT_COLOR, font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(definition, DOWN, buff=0.6)

        for feature in features:
            self.play(Write(feature), run_time=0.8)
        self.wait(1.5)

        # 淡出第一部分
        self.play(
            FadeOut(definition),
            FadeOut(features)
        )

        # ====== 第二部分：创建列表 ======
        subtitle1 = Text("1. 创建列表", font="SimSun", color=self.CODE_COLOR, font_size=36)
        subtitle1.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle1))

        # 代码示例
        code_example = Text(
            "numbers = [2, 5, 8, 13, 17, 22, 26, 31]",
            font="Courier New",
            color=self.TEXT_COLOR,
            font_size=32
        ).next_to(subtitle1, DOWN, buff=0.5)

        self.play(Write(code_example))
        self.wait(1)

        # 可视化列表
        numbers = [2, 5, 8, 13, 17, 22, 26, 31]
        squares = VGroup()
        numbers_text = VGroup()

        square_size = 0.8
        stroke_width = 2

        for i, num in enumerate(numbers):
            square = Square(
                side_length=square_size,
                stroke_width=stroke_width,
                stroke_color=self.SQUARE_COLOR
            ).shift(RIGHT * i * (square_size + stroke_width/100))
            squares.add(square)

            number = Text(
                str(num),
                font="SimSun",
                font_size=28,
                color=self.TEXT_COLOR
            ).move_to(square.get_center())
            numbers_text.add(number)

        array_group = VGroup(squares, numbers_text)
        array_group.scale_to_fit_width(config.frame_width - 2)
        array_group.move_to(ORIGIN + DOWN * 0.8)  # 向下移动，避免与上方文本重叠

        self.play(
            Create(squares),
            Write(numbers_text),
            run_time=2
        )
        self.wait(1.5)

        self.play(
            FadeOut(subtitle1),
            FadeOut(code_example)
        )

        # ====== 第三部分：索引访问 ======
        subtitle2 = Text("2. 索引访问", font="SimSun", color=self.CODE_COLOR, font_size=36)
        subtitle2.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle2))

        # 添加索引标记
        index_text = VGroup()
        for i in range(len(numbers)):
            index = Text(
                str(i),
                font="SimSun",
                font_size=24,
                color=self.INDEX_COLOR
            ).next_to(squares[i], DOWN, buff=0.2)
            index_text.add(index)

        self.play(Write(index_text), run_time=1.5)
        self.wait(0.5)

        # 索引说明
        index_note = Text(
            "索引从 0 开始计数",
            font="SimSun",
            color=self.INDEX_COLOR,
            font_size=28
        ).next_to(subtitle2, DOWN, buff=0.3)

        self.play(Write(index_note))
        self.wait(1)

        # 演示访问特定索引
        access_examples = [
            ("numbers[0]", 0, "第一个元素"),
            ("numbers[3]", 3, "第四个元素"),
            ("numbers[7]", 7, "最后一个元素")
        ]

        for code, idx, desc in access_examples:
            # 代码
            access_code = VGroup(
                Text(code, font="Courier New", color=self.CODE_COLOR, font_size=32),
                Text(" → ", font="SimSun", color=self.TEXT_COLOR, font_size=32),
                Text(str(numbers[idx]), font="SimSun", color=self.ELEMENT_COLOR, font_size=32),
                Text(f"  ({desc})", font="SimSun", color=self.TEXT_COLOR, font_size=24)
            ).arrange(RIGHT, buff=0.2).next_to(index_note, DOWN, buff=0.8)

            # 高亮对应的方块
            self.play(
                Write(access_code),
                squares[idx].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
                numbers_text[idx].animate.set_color(self.HIGHLIGHT_COLOR),
                index_text[idx].animate.scale(1.3)
            )
            self.wait(1)

            # 恢复
            self.play(
                FadeOut(access_code),
                squares[idx].animate.set_stroke(color=self.SQUARE_COLOR, width=stroke_width),
                numbers_text[idx].animate.set_color(self.TEXT_COLOR),
                index_text[idx].animate.scale(1/1.3)
            )

        self.play(
            FadeOut(subtitle2),
            FadeOut(index_note)
        )

        # ====== 第四部分：列表操作 ======
        subtitle3 = Text("3. 列表操作", font="SimSun", color=self.CODE_COLOR, font_size=36)
        subtitle3.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle3))

        # 操作1：修改元素
        operation1 = Text(
            "修改元素: numbers[2] = 10",
            font="Courier New",
            color=self.TEXT_COLOR,
            font_size=28
        ).next_to(subtitle3, DOWN, buff=0.5)

        self.play(Write(operation1))

        # 高亮要修改的元素
        self.play(
            squares[2].animate.set_stroke(color=self.CODE_COLOR, width=4),
            numbers_text[2].animate.set_color(self.CODE_COLOR).scale(1.2)
        )
        self.wait(0.5)

        # 修改数值
        new_number = Text("10", font="SimSun", font_size=28, color=self.HIGHLIGHT_COLOR).move_to(numbers_text[2])
        self.play(
            Transform(numbers_text[2], new_number),
            squares[2].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4)
        )
        self.wait(1)

        # 恢复
        self.play(
            squares[2].animate.set_stroke(color=self.SQUARE_COLOR, width=stroke_width),
            FadeOut(operation1)
        )

        # 操作2：获取长度
        operation2 = VGroup(
            Text("获取长度: ", font="SimSun", color=self.TEXT_COLOR, font_size=28),
            Text("len(numbers)", font="Courier New", color=self.CODE_COLOR, font_size=28),
            Text(" = ", font="SimSun", color=self.TEXT_COLOR, font_size=28),
            Text("8", font="SimSun", color=self.ELEMENT_COLOR, font_size=28)
        ).arrange(RIGHT, buff=0.1).next_to(subtitle3, DOWN, buff=0.5)

        self.play(Write(operation2))

        # 依次高亮所有元素
        self.play(
            *[squares[i].animate.set_stroke(color=self.INDEX_COLOR, width=3) for i in range(len(numbers))],
            run_time=1.5
        )
        self.wait(1)

        # 恢复
        self.play(
            *[squares[i].animate.set_stroke(color=self.SQUARE_COLOR, width=stroke_width) for i in range(len(numbers))],
            FadeOut(operation2)
        )

        self.play(FadeOut(subtitle3))

        # ====== 第五部分：引出查找需求 ======
        subtitle4 = Text("4. 查找问题", font="SimSun", color=self.CODE_COLOR, font_size=36)
        subtitle4.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle4))

        # 问题描述
        question = Text(
            "如何在列表中查找特定的值？",
            font="SimSun",
            color=self.TEXT_COLOR,
            font_size=32
        ).next_to(subtitle4, DOWN, buff=0.5)

        self.play(Write(question))
        self.wait(1)

        # 示例：查找值 22
        target_example = VGroup(
            Text("例如：查找值 ", font="SimSun", color=self.TEXT_COLOR, font_size=30),
            Text("22", font="SimSun", color="#E74C3C", font_size=30),
            Text(" 在列表中的位置", font="SimSun", color=self.TEXT_COLOR, font_size=30)
        ).arrange(RIGHT, buff=0.1).next_to(question, DOWN, buff=0.5)

        self.play(Write(target_example))

        # 高亮目标值
        target_idx = 5  # 22在索引5的位置
        self.play(
            squares[target_idx].animate.set_stroke(color="#E74C3C", width=4),
            numbers_text[target_idx].animate.set_color("#E74C3C").scale(1.3)
        )
        self.wait(1.5)

        # 解决方案介绍
        self.play(
            FadeOut(question),
            FadeOut(target_example)
        )

        solutions = VGroup(
            Text("常用的查找算法：", font="SimSun", color=self.TEXT_COLOR, font_size=32),
            Text("", font="SimSun", font_size=10),  # 空行
            Text("1. 线性查找（Linear Search）", font="SimSun", color="#3498DB", font_size=28),
            Text("   - 逐个检查每个元素", font="SimSun", color=self.TEXT_COLOR, font_size=24),
            Text("   - 适用于无序列表", font="SimSun", color=self.TEXT_COLOR, font_size=24),
            Text("   - 时间复杂度：O(n)", font="SimSun", color=self.TEXT_COLOR, font_size=24),
            Text("", font="SimSun", font_size=10),  # 空行
            Text("2. 二分查找（Binary Search）", font="SimSun", color="#9B59B6", font_size=28),
            Text("   - 每次排除一半元素", font="SimSun", color=self.TEXT_COLOR, font_size=24),
            Text("   - 仅适用于有序列表", font="SimSun", color=self.TEXT_COLOR, font_size=24),
            Text("   - 时间复杂度：O(log n)", font="SimSun", color=self.TEXT_COLOR, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(subtitle4, DOWN, buff=0.5)

        for item in solutions:
            self.play(Write(item), run_time=0.6)

        self.wait(2)

        # 对比说明
        self.play(FadeOut(solutions))

        comparison = VGroup(
            Text("对于长度为 n 的列表：", font="SimSun", color=self.TEXT_COLOR, font_size=28),
            Text("", font="SimSun", font_size=10),
            Text("线性查找：最多需要检查 n 次", font="SimSun", color="#3498DB", font_size=26),
            Text("二分查找：最多需要检查 log₂(n) 次", font="SimSun", color="#9B59B6", font_size=26),
            Text("", font="SimSun", font_size=10),
            Text("当 n = 1000 时：", font="SimSun", color=self.TEXT_COLOR, font_size=26),
            Text("线性查找：最多 1000 次", font="SimSun", color="#3498DB", font_size=24),
            Text("二分查找：最多 10 次", font="SimSun", color="#9B59B6", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(subtitle4, DOWN, buff=0.5)

        for item in comparison:
            self.play(Write(item), run_time=0.5)

        self.wait(2)

        # 结束语
        self.play(
            FadeOut(subtitle4),
            FadeOut(comparison),
            FadeOut(squares),
            FadeOut(numbers_text),
            FadeOut(index_text)
        )

        conclusion = VGroup(
            Text("接下来，让我们详细了解", font="SimSun", color=self.TEXT_COLOR, font_size=36),
            Text("这两种查找算法的工作原理", font="SimSun", color=self.TEXT_COLOR, font_size=36)
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        self.play(Write(conclusion))
        self.wait(2)

        self.play(FadeOut(conclusion), FadeOut(title))
        self.wait(0.5)

if __name__ == "__main__":
    config.pixel_height = 2160
    config.pixel_width = 3840
    config.frame_rate = 30

    with tempconfig({"quality": "production_quality", "preview": False}):
        scene = ListBasicsAnimation()
        scene.render()
