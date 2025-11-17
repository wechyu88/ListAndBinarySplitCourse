from manim import *

class ListComprehensionAnimation(Scene):
    """列表推导式和数值列表动画"""
    def __init__(self):
        super().__init__()
        self.camera.background_color = "#FFFFFF"

        # 颜色方案
        self.TEXT_COLOR = "#000000"
        self.SQUARE_COLOR = "#95A5A6"
        self.HIGHLIGHT_COLOR = "#2ECC71"
        self.INDEX_COLOR = "#3498DB"
        self.CODE_COLOR = "#E67E22"
        self.COMPREHENSION_COLOR = "#9B59B6"

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
        # 标题
        title = Text("数值列表与列表推导式", font="SimSun", color=self.TEXT_COLOR, font_size=44)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # ====== 第一部分：range()生成数值列表 ======
        subtitle1 = Text("1. 使用 range() 生成数值列表", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle1.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle1))

        # range() 示例
        code1 = Text("numbers = list(range(1, 6))", font="Courier New", color=self.CODE_COLOR, font_size=28)
        code1.next_to(subtitle1, DOWN, buff=0.3)
        self.play(Write(code1))
        self.wait(0.5)

        # 生成效果
        result1 = Text("结果: [1, 2, 3, 4, 5]", font="Courier New", color=self.HIGHLIGHT_COLOR, font_size=28)
        result1.next_to(code1, DOWN, buff=0.3)

        # 逐个显示数字
        squares1 = VGroup()
        numbers1 = VGroup()
        for i in range(1, 6):
            square = Square(side_length=0.6, stroke_width=2, stroke_color=self.SQUARE_COLOR)
            square.shift(RIGHT * (i-1) * 0.65)
            number = Text(str(i), font="SimSun", font_size=24, color=self.TEXT_COLOR).move_to(square)

            squares1.add(square)
            numbers1.add(number)

        list_group1 = VGroup(squares1, numbers1)
        list_group1.next_to(result1, DOWN, buff=0.4)

        for i in range(5):
            self.play(
                Create(squares1[i]),
                Write(numbers1[i]),
                run_time=0.4
            )

        self.play(Write(result1))
        self.wait(1.5)

        self.play(
            FadeOut(code1),
            FadeOut(result1),
            FadeOut(squares1),
            FadeOut(numbers1),
            FadeOut(subtitle1)
        )

        # ====== 第二部分：列表推导式基础 ======
        subtitle2 = Text("2. 列表推导式 - 基础语法", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle2.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle2))

        # 传统方法
        traditional_title = Text("传统方法：", font="SimSun", color=self.TEXT_COLOR, font_size=26)
        traditional_title.next_to(subtitle2, DOWN, buff=0.3).to_edge(LEFT, buff=1)
        self.play(Write(traditional_title))

        traditional_code = VGroup(
            Text("squares = []", font="Courier New", color=self.TEXT_COLOR, font_size=22),
            Text("for i in range(1, 6):", font="Courier New", color=self.TEXT_COLOR, font_size=22),
            Text("    squares.append(i**2)", font="Courier New", color=self.TEXT_COLOR, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        traditional_code.next_to(traditional_title, DOWN, buff=0.2).align_to(traditional_title, LEFT)

        self.play(Write(traditional_code), run_time=2)
        self.wait(1)

        # 列表推导式方法
        comprehension_title = Text("列表推导式：", font="SimSun", color=self.COMPREHENSION_COLOR, font_size=26)
        comprehension_title.next_to(traditional_code, DOWN, buff=0.4).align_to(traditional_title, LEFT)
        self.play(Write(comprehension_title))

        comprehension_code = Text(
            "squares = [i**2 for i in range(1, 6)]",
            font="Courier New",
            color=self.COMPREHENSION_COLOR,
            font_size=22
        )
        comprehension_code.next_to(comprehension_title, DOWN, buff=0.2).align_to(traditional_title, LEFT)

        self.play(Write(comprehension_code))
        self.wait(1)

        # 显示结果
        result_text = Text("结果: [1, 4, 9, 16, 25]", font="Courier New", color=self.HIGHLIGHT_COLOR, font_size=26)
        result_text.next_to(comprehension_code, DOWN, buff=0.4).align_to(traditional_title, LEFT)

        squares2 = VGroup()
        numbers2 = VGroup()
        for i, val in enumerate([1, 4, 9, 16, 25]):
            square = Square(side_length=0.6, stroke_width=2, stroke_color=self.COMPREHENSION_COLOR)
            square.shift(RIGHT * i * 0.65)
            number = Text(str(val), font="SimSun", font_size=22, color=self.COMPREHENSION_COLOR).move_to(square)

            squares2.add(square)
            numbers2.add(number)

        list_group2 = VGroup(squares2, numbers2)
        list_group2.next_to(result_text, DOWN, buff=0.3).align_to(traditional_title, LEFT)

        for i in range(5):
            self.play(
                Create(squares2[i]),
                Write(numbers2[i]),
                run_time=0.3
            )

        self.play(Write(result_text))
        self.wait(2)

        self.play(
            FadeOut(traditional_title),
            FadeOut(traditional_code),
            FadeOut(comprehension_title),
            FadeOut(comprehension_code),
            FadeOut(result_text),
            FadeOut(squares2),
            FadeOut(numbers2),
            FadeOut(subtitle2)
        )

        # ====== 第三部分：带条件的列表推导式 ======
        subtitle3 = Text("3. 带条件的列表推导式", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle3.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle3))

        # 示例：筛选偶数
        example_desc = Text("示例：筛选1-10中的偶数", font="SimSun", color=self.TEXT_COLOR, font_size=26)
        example_desc.next_to(subtitle3, DOWN, buff=0.3)
        self.play(Write(example_desc))

        example_code = Text(
            "evens = [i for i in range(1, 11) if i % 2 == 0]",
            font="Courier New",
            color=self.COMPREHENSION_COLOR,
            font_size=24
        )
        example_code.next_to(example_desc, DOWN, buff=0.3)
        self.play(Write(example_code))
        self.wait(1)

        # 显示过滤过程
        process_text = Text("处理过程：", font="SimSun", color=self.TEXT_COLOR, font_size=24)
        process_text.next_to(example_code, DOWN, buff=0.4)
        self.play(Write(process_text))

        # 显示1-10的数字，高亮偶数
        all_nums = VGroup()
        for i in range(1, 11):
            num = Text(str(i), font="SimSun", font_size=24, color=self.TEXT_COLOR)
            num.shift(RIGHT * (i-1) * 0.5)
            all_nums.add(num)

        all_nums.next_to(process_text, DOWN, buff=0.3)
        self.play(Write(all_nums))
        self.wait(0.5)

        # 高亮偶数
        for i in range(1, 11):
            if i % 2 == 0:
                self.play(
                    all_nums[i-1].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.3),
                    run_time=0.3
                )

        self.wait(1)

        # 显示最终结果
        final_result = Text("结果: [2, 4, 6, 8, 10]", font="Courier New", color=self.HIGHLIGHT_COLOR, font_size=26)
        final_result.next_to(all_nums, DOWN, buff=0.4)
        self.play(Write(final_result))
        self.wait(2)

        self.play(
            FadeOut(example_desc),
            FadeOut(example_code),
            FadeOut(process_text),
            FadeOut(all_nums),
            FadeOut(final_result),
            FadeOut(subtitle3)
        )

        # ====== 第四部分：嵌套列表推导式 ======
        subtitle4 = Text("4. 嵌套列表推导式", font="SimSun", color=self.CODE_COLOR, font_size=32)
        subtitle4.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle4))

        # 示例：生成3x3矩阵
        matrix_desc = Text("示例：生成3x3矩阵", font="SimSun", color=self.TEXT_COLOR, font_size=26)
        matrix_desc.next_to(subtitle4, DOWN, buff=0.3)
        self.play(Write(matrix_desc))

        matrix_code = Text(
            "matrix = [[i*3+j for j in range(1,4)] for i in range(3)]",
            font="Courier New",
            color=self.COMPREHENSION_COLOR,
            font_size=22
        )
        matrix_code.next_to(matrix_desc, DOWN, buff=0.3)
        self.play(Write(matrix_code))
        self.wait(1)

        # 显示矩阵
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix_group = VGroup()

        for i in range(3):
            row_group = VGroup()
            for j in range(3):
                square = Square(side_length=0.5, stroke_width=2, stroke_color=self.SQUARE_COLOR)
                square.shift(RIGHT * j * 0.55 + DOWN * i * 0.55)
                number = Text(str(matrix[i][j]), font="SimSun", font_size=20, color=self.TEXT_COLOR).move_to(square)
                row_group.add(VGroup(square, number))
            matrix_group.add(row_group)

        matrix_group.next_to(matrix_code, DOWN, buff=0.5)

        # 逐行显示矩阵
        for row in matrix_group:
            self.play(*[Create(cell[0]) for cell in row], run_time=0.5)
            self.play(*[Write(cell[1]) for cell in row], run_time=0.5)

        self.wait(2)

        # 结束
        self.play(
            FadeOut(matrix_desc),
            FadeOut(matrix_code),
            FadeOut(matrix_group),
            FadeOut(subtitle4),
            FadeOut(title)
        )
        self.wait(0.5)

if __name__ == "__main__":
    config.pixel_height = 2160
    config.pixel_width = 3840
    config.frame_rate = 30

    with tempconfig({"quality": "production_quality", "preview": False}):
        scene = ListComprehensionAnimation()
        scene.render()
