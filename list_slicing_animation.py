from manim import *

class ListSlicingAnimation(Scene):
    """列表切片操作动画"""
    def __init__(self):
        super().__init__()
        self.camera.background_color = "#FFFFFF"

        # 颜色方案
        self.TEXT_COLOR = "#000000"
        self.SQUARE_COLOR = "#95A5A6"
        self.HIGHLIGHT_COLOR = "#2ECC71"
        self.INDEX_COLOR = "#3498DB"
        self.CODE_COLOR = "#E67E22"
        self.SLICE_COLOR = "#9B59B6"

        # 创建水印
        watermark = Text(
            "作者:温程远",
            font="SimSun",
            color=self.TEXT_COLOR,
            font_size=24
        ).to_corner(DR, buff=0.3)
        watermark.set_opacity(0.3)
        self.add(watermark)

    def create_list_visualization(self, data, position=ORIGIN):
        """创建列表可视化"""
        squares = VGroup()
        numbers_text = VGroup()

        square_size = 0.65
        stroke_width = 2

        for i, num in enumerate(data):
            square = Square(
                side_length=square_size,
                stroke_width=stroke_width,
                stroke_color=self.SQUARE_COLOR
            ).shift(RIGHT * i * (square_size + stroke_width/100))
            squares.add(square)

            number = Text(
                str(num),
                font="SimSun",
                font_size=24,
                color=self.TEXT_COLOR
            ).move_to(square.get_center())
            numbers_text.add(number)

        array_group = VGroup(squares, numbers_text)
        array_group.move_to(position)

        # 添加正向索引
        index_text = VGroup()
        for i in range(len(data)):
            index = Text(
                str(i),
                font="SimSun",
                font_size=18,
                color=self.INDEX_COLOR
            ).next_to(squares[i], UP, buff=0.12)
            index_text.add(index)

        # 添加负向索引
        neg_index_text = VGroup()
        for i in range(len(data)):
            neg_index = Text(
                str(i - len(data)),
                font="SimSun",
                font_size=18,
                color="#E74C3C"
            ).next_to(squares[i], DOWN, buff=0.12)
            neg_index_text.add(neg_index)

        return squares, numbers_text, index_text, neg_index_text

    def construct(self):
        # 标题
        title = Text("Python 列表切片", font="SimSun", color=self.TEXT_COLOR, font_size=44)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # ====== 第一部分：基本切片 ======
        subtitle1 = Text("1. 基本切片语法 [start:stop:step]", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle1.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle1))

        # 创建列表
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        squares, numbers_text, index_text, neg_index_text = self.create_list_visualization(
            data, ORIGIN + DOWN * 0.3
        )

        self.play(
            Create(squares),
            Write(numbers_text),
            Write(index_text),
            Write(neg_index_text),
            run_time=2
        )
        self.wait(1)

        # 示例1: numbers[2:7]
        example1 = Text("numbers[2:7] - 从索引2到6", font="Courier New", color=self.TEXT_COLOR, font_size=26)
        example1.next_to(subtitle1, DOWN, buff=0.25)
        self.play(Write(example1))

        # 高亮切片范围
        for i in range(2, 7):
            self.play(
                squares[i].animate.set_stroke(color=self.SLICE_COLOR, width=4),
                numbers_text[i].animate.set_color(self.SLICE_COLOR),
                run_time=0.3
            )

        self.wait(1.5)

        # 恢复
        for i in range(2, 7):
            self.play(
                squares[i].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
                numbers_text[i].animate.set_color(self.TEXT_COLOR),
                run_time=0.2
            )

        self.play(FadeOut(example1))

        # 示例2: numbers[:5]
        example2 = Text("numbers[:5] - 从开始到索引4", font="Courier New", color=self.TEXT_COLOR, font_size=26)
        example2.next_to(subtitle1, DOWN, buff=0.25)
        self.play(Write(example2))

        for i in range(0, 5):
            self.play(
                squares[i].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
                numbers_text[i].animate.set_color(self.HIGHLIGHT_COLOR),
                run_time=0.3
            )

        self.wait(1.5)

        for i in range(0, 5):
            self.play(
                squares[i].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
                numbers_text[i].animate.set_color(self.TEXT_COLOR),
                run_time=0.2
            )

        self.play(FadeOut(example2))

        # 示例3: numbers[6:]
        example3 = Text("numbers[6:] - 从索引6到结尾", font="Courier New", color=self.TEXT_COLOR, font_size=26)
        example3.next_to(subtitle1, DOWN, buff=0.25)
        self.play(Write(example3))

        for i in range(6, 10):
            self.play(
                squares[i].animate.set_stroke(color=self.CODE_COLOR, width=4),
                numbers_text[i].animate.set_color(self.CODE_COLOR),
                run_time=0.3
            )

        self.wait(1.5)

        for i in range(6, 10):
            self.play(
                squares[i].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
                numbers_text[i].animate.set_color(self.TEXT_COLOR),
                run_time=0.2
            )

        self.play(FadeOut(example3), FadeOut(subtitle1))

        # ====== 第二部分：步长切片 ======
        subtitle2 = Text("2. 使用步长 (Step)", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle2.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle2))

        # 示例4: numbers[::2] - 每隔一个取一个
        example4 = Text("numbers[::2] - 每隔一个元素取一个", font="Courier New", color=self.TEXT_COLOR, font_size=26)
        example4.next_to(subtitle2, DOWN, buff=0.25)
        self.play(Write(example4))

        for i in range(0, 10, 2):
            self.play(
                squares[i].animate.set_stroke(color=self.SLICE_COLOR, width=4),
                numbers_text[i].animate.set_color(self.SLICE_COLOR).scale(1.2),
                run_time=0.4
            )

        self.wait(1.5)

        for i in range(0, 10, 2):
            self.play(
                squares[i].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
                numbers_text[i].animate.set_color(self.TEXT_COLOR).scale(1/1.2),
                run_time=0.2
            )

        self.play(FadeOut(example4))

        # 示例5: numbers[1::3] - 从索引1开始，每隔2个取一个
        example5 = Text("numbers[1::3] - 从索引1开始，步长为3", font="Courier New", color=self.TEXT_COLOR, font_size=26)
        example5.next_to(subtitle2, DOWN, buff=0.25)
        self.play(Write(example5))

        for i in range(1, 10, 3):
            self.play(
                squares[i].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
                numbers_text[i].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.2),
                run_time=0.4
            )

        self.wait(1.5)

        for i in range(1, 10, 3):
            self.play(
                squares[i].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
                numbers_text[i].animate.set_color(self.TEXT_COLOR).scale(1/1.2),
                run_time=0.2
            )

        self.play(FadeOut(example5), FadeOut(subtitle2))

        # ====== 第三部分：反向切片 ======
        subtitle3 = Text("3. 反向切片", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle3.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle3))

        # 示例6: numbers[::-1] - 反转列表
        example6 = Text("numbers[::-1] - 反转整个列表", font="Courier New", color=self.TEXT_COLOR, font_size=26)
        example6.next_to(subtitle3, DOWN, buff=0.25)
        self.play(Write(example6))

        # 从右到左依次高亮
        for i in range(9, -1, -1):
            self.play(
                squares[i].animate.set_stroke(color="#E74C3C", width=4),
                numbers_text[i].animate.set_color("#E74C3C").scale(1.2),
                run_time=0.3
            )

        self.wait(1.5)

        for i in range(10):
            self.play(
                squares[i].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
                numbers_text[i].animate.set_color(self.TEXT_COLOR).scale(1/1.2),
                run_time=0.15
            )

        self.play(FadeOut(example6))

        # 示例7: numbers[-3:] - 最后3个元素
        example7 = Text("numbers[-3:] - 最后3个元素", font="Courier New", color=self.TEXT_COLOR, font_size=26)
        example7.next_to(subtitle3, DOWN, buff=0.25)
        self.play(Write(example7))

        for i in range(7, 10):
            self.play(
                squares[i].animate.set_stroke(color=self.SLICE_COLOR, width=4),
                numbers_text[i].animate.set_color(self.SLICE_COLOR),
                neg_index_text[i].animate.set_color(self.SLICE_COLOR).scale(1.3),
                run_time=0.4
            )

        self.wait(1.5)

        # 结束
        self.play(
            FadeOut(example7),
            FadeOut(subtitle3),
            FadeOut(squares),
            FadeOut(numbers_text),
            FadeOut(index_text),
            FadeOut(neg_index_text),
            FadeOut(title)
        )
        self.wait(0.5)

if __name__ == "__main__":
    config.pixel_height = 2160
    config.pixel_width = 3840
    config.frame_rate = 30

    with tempconfig({"quality": "production_quality", "preview": False}):
        scene = ListSlicingAnimation()
        scene.render()
