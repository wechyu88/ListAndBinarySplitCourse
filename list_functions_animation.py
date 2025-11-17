from manim import *

class ListFunctionsAnimation(Scene):
    """列表函数和方法动画：遍历、排序等"""
    def __init__(self):
        super().__init__()
        self.camera.background_color = "#FFFFFF"

        # 颜色方案
        self.TEXT_COLOR = "#000000"
        self.SQUARE_COLOR = "#95A5A6"
        self.HIGHLIGHT_COLOR = "#2ECC71"
        self.INDEX_COLOR = "#3498DB"
        self.CODE_COLOR = "#E67E22"
        self.SORT_COLOR = "#9B59B6"

        # 创建水印
        watermark = Text(
            "作者：温程远",
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

        square_size = 0.7
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
                font_size=26,
                color=self.TEXT_COLOR
            ).move_to(square.get_center())
            numbers_text.add(number)

        array_group = VGroup(squares, numbers_text)
        array_group.move_to(position)

        return squares, numbers_text

    def construct(self):
        # 标题
        title = Text("Python 列表常用函数和方法", font="SimSun", color=self.TEXT_COLOR, font_size=44)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # ====== 第一部分：遍历列表 ======
        subtitle1 = Text("1. 遍历列表 (for循环)", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle1.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle1))

        # 创建列表
        data1 = [15, 23, 8, 42, 16]
        squares1, numbers_text1 = self.create_list_visualization(data1, ORIGIN + DOWN * 0.3)

        self.play(
            Create(squares1),
            Write(numbers_text1)
        )
        self.wait(0.5)

        # 代码示例
        code1 = Text("for num in numbers:", font="Courier New", color=self.CODE_COLOR, font_size=28)
        code1.next_to(subtitle1, DOWN, buff=0.25)
        self.play(Write(code1))

        # 依次遍历每个元素
        for i in range(len(data1)):
            self.play(
                squares1[i].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
                numbers_text1[i].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.3),
                run_time=0.5
            )
            self.wait(0.3)
            self.play(
                squares1[i].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
                numbers_text1[i].animate.set_color(self.TEXT_COLOR).scale(1/1.3),
                run_time=0.3
            )

        self.wait(1)

        self.play(
            FadeOut(code1),
            FadeOut(squares1),
            FadeOut(numbers_text1),
            FadeOut(subtitle1)
        )

        # ====== 第二部分：排序 ======
        subtitle2 = Text("2. 排序 (sort & sorted)", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle2.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle2))

        # 创建无序列表
        data2 = [42, 15, 8, 23, 16]
        squares2, numbers_text2 = self.create_list_visualization(data2, ORIGIN + DOWN * 0.3)

        self.play(
            Create(squares2),
            Write(numbers_text2)
        )
        self.wait(0.5)

        # 排序说明
        sort_desc = Text("numbers.sort() - 升序排序", font="Courier New", color=self.TEXT_COLOR, font_size=28)
        sort_desc.next_to(subtitle2, DOWN, buff=0.25)
        self.play(Write(sort_desc))
        self.wait(0.5)

        # 排序过程可视化（冒泡排序的简化版本）
        data_sorted = sorted(data2)

        # 创建排序后的新位置
        sorted_squares = VGroup()
        sorted_numbers = VGroup()

        square_size = 0.7
        stroke_width = 2

        for i, num in enumerate(data_sorted):
            square = Square(
                side_length=square_size,
                stroke_width=stroke_width,
                stroke_color=self.SORT_COLOR
            ).shift(RIGHT * i * (square_size + stroke_width/100))
            sorted_squares.add(square)

            number = Text(
                str(num),
                font="SimSun",
                font_size=26,
                color=self.SORT_COLOR
            ).move_to(square.get_center())
            sorted_numbers.add(number)

        sorted_group = VGroup(sorted_squares, sorted_numbers)
        sorted_group.move_to(ORIGIN + DOWN * 0.3)

        # 高亮显示排序过程
        self.play(
            *[squares2[i].animate.set_stroke(color=self.SORT_COLOR, width=3) for i in range(len(data2))],
            *[numbers_text2[i].animate.set_color(self.SORT_COLOR) for i in range(len(data2))],
            run_time=1
        )

        self.wait(0.5)

        # 变换到排序后的位置
        animations = []
        for i, num in enumerate(data2):
            sorted_idx = data_sorted.index(num)
            animations.append(squares2[i].animate.move_to(sorted_squares[sorted_idx]))
            animations.append(numbers_text2[i].animate.move_to(sorted_numbers[sorted_idx]))

        self.play(*animations, run_time=2)
        self.wait(1)

        # 恢复正常颜色
        self.play(
            *[squares2[i].animate.set_stroke(color=self.SQUARE_COLOR, width=2) for i in range(len(data2))],
            *[numbers_text2[i].animate.set_color(self.TEXT_COLOR) for i in range(len(data2))],
            run_time=0.5
        )

        self.wait(1)

        self.play(
            FadeOut(sort_desc),
            FadeOut(squares2),
            FadeOut(numbers_text2),
            FadeOut(subtitle2)
        )

        # ====== 第三部分：反转 ======
        subtitle3 = Text("3. 反转 (reverse)", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle3.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle3))

        # 创建列表
        data3 = [10, 20, 30, 40, 50]
        squares3, numbers_text3 = self.create_list_visualization(data3, ORIGIN + DOWN * 0.3)

        self.play(
            Create(squares3),
            Write(numbers_text3)
        )
        self.wait(0.5)

        # 反转说明
        reverse_desc = Text("numbers.reverse() - 反转列表", font="Courier New", color=self.TEXT_COLOR, font_size=28)
        reverse_desc.next_to(subtitle3, DOWN, buff=0.25)
        self.play(Write(reverse_desc))
        self.wait(0.5)

        # 反转动画
        n = len(data3)
        animations = []
        for i in range(n):
            animations.append(squares3[i].animate.move_to(squares3[n-1-i].get_center()))
            animations.append(numbers_text3[i].animate.move_to(numbers_text3[n-1-i].get_center()))

        self.play(*animations, run_time=1.5)
        self.wait(1.5)

        self.play(
            FadeOut(reverse_desc),
            FadeOut(squares3),
            FadeOut(numbers_text3),
            FadeOut(subtitle3)
        )

        # ====== 第四部分：其他常用方法 ======
        subtitle4 = Text("4. 其他常用方法", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle4.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle4))

        # 方法列表
        methods = VGroup(
            Text("len(numbers)", font="Courier New", color=self.CODE_COLOR, font_size=26),
            Text(" - 获取列表长度", font="SimSun", color=self.TEXT_COLOR, font_size=24),
            Text("", font="SimSun", font_size=8),
            Text("max(numbers)", font="Courier New", color=self.CODE_COLOR, font_size=26),
            Text(" - 获取最大值", font="SimSun", color=self.TEXT_COLOR, font_size=24),
            Text("", font="SimSun", font_size=8),
            Text("min(numbers)", font="Courier New", color=self.CODE_COLOR, font_size=26),
            Text(" - 获取最小值", font="SimSun", color=self.TEXT_COLOR, font_size=24),
            Text("", font="SimSun", font_size=8),
            Text("sum(numbers)", font="Courier New", color=self.CODE_COLOR, font_size=26),
            Text(" - 求和", font="SimSun", color=self.TEXT_COLOR, font_size=24),
            Text("", font="SimSun", font_size=8),
            Text("numbers.count(x)", font="Courier New", color=self.CODE_COLOR, font_size=26),
            Text(" - 统计x出现的次数", font="SimSun", color=self.TEXT_COLOR, font_size=24)
        )

        # 将方法分为两列显示
        left_methods = VGroup(methods[0], methods[1], methods[2], methods[3], methods[4], methods[5], methods[6], methods[7])
        right_methods = VGroup(methods[8], methods[9], methods[10], methods[11], methods[12], methods[13])

        left_methods.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        right_methods.arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        left_methods.next_to(subtitle4, DOWN, buff=0.4).shift(LEFT * 2.5)
        right_methods.next_to(subtitle4, DOWN, buff=0.4).shift(RIGHT * 1.5)

        self.play(
            Write(left_methods),
            Write(right_methods),
            run_time=3
        )
        self.wait(2)

        # 结束
        self.play(
            FadeOut(left_methods),
            FadeOut(right_methods),
            FadeOut(subtitle4),
            FadeOut(title)
        )
        self.wait(0.5)

if __name__ == "__main__":
    config.pixel_height = 2160
    config.pixel_width = 3840
    config.frame_rate = 30

    with tempconfig({"quality": "production_quality", "preview": False}):
        scene = ListFunctionsAnimation()
        scene.render()
