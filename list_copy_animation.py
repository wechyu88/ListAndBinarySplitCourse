from manim import *

class ListCopyAnimation(Scene):
    """列表的深浅复制动画"""
    def __init__(self):
        super().__init__()
        self.camera.background_color = "#FFFFFF"

        # 颜色方案
        self.TEXT_COLOR = "#000000"
        self.SQUARE_COLOR = "#95A5A6"
        self.HIGHLIGHT_COLOR = "#2ECC71"
        self.INDEX_COLOR = "#3498DB"
        self.CODE_COLOR = "#E67E22"
        self.SHALLOW_COLOR = "#3498DB"
        self.DEEP_COLOR = "#9B59B6"
        self.REFERENCE_COLOR = "#E74C3C"

        # 创建水印
        watermark = Text(
            "作者：温程远",
            font="SimSun",
            color=self.TEXT_COLOR,
            font_size=24
        ).to_corner(DR, buff=0.3)
        watermark.set_opacity(0.3)
        self.add(watermark)

    def create_list_box(self, data, label, position, color):
        """创建列表框"""
        squares = VGroup()
        numbers = VGroup()

        square_size = 0.6
        for i, num in enumerate(data):
            square = Square(side_length=square_size, stroke_width=2, stroke_color=color)
            square.shift(RIGHT * i * 0.65)
            number = Text(str(num), font="SimSun", font_size=22, color=self.TEXT_COLOR).move_to(square)

            squares.add(square)
            numbers.add(number)

        list_group = VGroup(squares, numbers)

        # 添加标签
        label_text = Text(label, font="Courier New", color=color, font_size=24)
        label_text.next_to(list_group, LEFT, buff=0.3)

        final_group = VGroup(label_text, list_group)
        final_group.move_to(position)

        return final_group, squares, numbers

    def construct(self):
        # 标题
        title = Text("列表的复制：引用、浅复制、深复制", font="SimSun", color=self.TEXT_COLOR, font_size=40)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # ====== 第一部分：引用（赋值） ======
        subtitle1 = Text("1. 引用赋值（指向同一对象）", font="SimSun", color=self.CODE_COLOR, font_size=30)
        subtitle1.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle1))

        # 代码
        code1 = Text("list1 = [1, 2, 3]", font="Courier New", color=self.TEXT_COLOR, font_size=24)
        code1.next_to(subtitle1, DOWN, buff=0.3).to_edge(LEFT, buff=1)
        self.play(Write(code1))

        # 创建原始列表
        data1 = [1, 2, 3]
        list1_group, list1_squares, list1_numbers = self.create_list_box(
            data1, "list1:", ORIGIN + UP * 0.5, self.REFERENCE_COLOR
        )
        self.play(Create(list1_group))
        self.wait(0.5)

        # 引用赋值
        code2 = Text("list2 = list1", font="Courier New", color=self.REFERENCE_COLOR, font_size=24)
        code2.next_to(code1, DOWN, buff=0.2).align_to(code1, LEFT)
        self.play(Write(code2))

        # 创建引用箭头
        list2_label = Text("list2:", font="Courier New", color=self.REFERENCE_COLOR, font_size=24)
        list2_label.next_to(list1_group, DOWN, buff=0.8).shift(LEFT * 2)

        arrow = Arrow(
            list2_label.get_right() + RIGHT * 0.2,
            list1_group[1].get_bottom() + DOWN * 0.3,
            color=self.REFERENCE_COLOR,
            buff=0.1,
            stroke_width=3
        )

        self.play(Write(list2_label), Create(arrow))
        self.wait(1)

        # 说明
        explain1 = Text(
            "list1 和 list2 指向同一个列表对象！",
            font="SimSun",
            color=self.REFERENCE_COLOR,
            font_size=22
        )
        explain1.next_to(list2_label, DOWN, buff=0.5)
        self.play(Write(explain1))
        self.wait(1)

        # 修改演示
        modify_code = Text("list2[0] = 99", font="Courier New", color=self.REFERENCE_COLOR, font_size=24)
        modify_code.next_to(code2, DOWN, buff=0.2).align_to(code1, LEFT)
        self.play(Write(modify_code))

        # 修改第一个元素
        new_num = Text("99", font="SimSun", font_size=22, color=self.REFERENCE_COLOR).move_to(list1_numbers[0])
        self.play(
            list1_squares[0].animate.set_stroke(color=self.REFERENCE_COLOR, width=4),
            Transform(list1_numbers[0], new_num)
        )
        self.wait(0.5)

        # 显示两个都变了
        result1 = Text("list1 和 list2 都变成了 [99, 2, 3]", font="SimSun", color=self.REFERENCE_COLOR, font_size=22)
        result1.next_to(explain1, DOWN, buff=0.3)
        self.play(Write(result1))
        self.wait(2)

        # 清除
        self.play(
            FadeOut(code1), FadeOut(code2), FadeOut(modify_code),
            FadeOut(list1_group), FadeOut(list2_label), FadeOut(arrow),
            FadeOut(explain1), FadeOut(result1), FadeOut(subtitle1)
        )

        # ====== 第二部分：浅复制 ======
        subtitle2 = Text("2. 浅复制（copy 或 [:]）", font="SimSun", color=self.CODE_COLOR, font_size=30)
        subtitle2.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle2))

        # 代码
        code3 = Text("list1 = [1, 2, 3]", font="Courier New", color=self.TEXT_COLOR, font_size=24)
        code3.next_to(subtitle2, DOWN, buff=0.3).to_edge(LEFT, buff=1)
        self.play(Write(code3))

        # 创建原始列表
        data2 = [1, 2, 3]
        list3_group, list3_squares, list3_numbers = self.create_list_box(
            data2, "list1:", UP * 0.8 + LEFT * 2, self.SHALLOW_COLOR
        )
        self.play(Create(list3_group))
        self.wait(0.5)

        # 浅复制
        code4 = Text("list2 = list1.copy()", font="Courier New", color=self.SHALLOW_COLOR, font_size=24)
        code4.next_to(code3, DOWN, buff=0.2).align_to(code3, LEFT)
        self.play(Write(code4))

        # 创建复制的列表
        list4_group, list4_squares, list4_numbers = self.create_list_box(
            data2, "list2:", DOWN * 0.5 + LEFT * 2, self.SHALLOW_COLOR
        )
        self.play(Create(list4_group))
        self.wait(1)

        # 说明
        explain2 = Text(
            "创建了一个新的列表对象！",
            font="SimSun",
            color=self.SHALLOW_COLOR,
            font_size=22
        )
        explain2.next_to(list4_group, DOWN, buff=0.5)
        self.play(Write(explain2))
        self.wait(1)

        # 修改演示
        modify_code2 = Text("list2[0] = 99", font="Courier New", color=self.SHALLOW_COLOR, font_size=24)
        modify_code2.next_to(code4, DOWN, buff=0.2).align_to(code3, LEFT)
        self.play(Write(modify_code2))

        # 只修改list2
        new_num2 = Text("99", font="SimSun", font_size=22, color=self.SHALLOW_COLOR).move_to(list4_numbers[0])
        self.play(
            list4_squares[0].animate.set_stroke(color=self.SHALLOW_COLOR, width=4),
            Transform(list4_numbers[0], new_num2)
        )
        self.wait(0.5)

        # 显示结果
        result2 = VGroup(
            Text("list1 仍然是 [1, 2, 3]", font="SimSun", color=self.SHALLOW_COLOR, font_size=22),
            Text("list2 变成了 [99, 2, 3]", font="SimSun", color=self.SHALLOW_COLOR, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        result2.next_to(explain2, DOWN, buff=0.3)
        self.play(Write(result2))
        self.wait(2)

        # 清除
        self.play(
            FadeOut(code3), FadeOut(code4), FadeOut(modify_code2),
            FadeOut(list3_group), FadeOut(list4_group),
            FadeOut(explain2), FadeOut(result2), FadeOut(subtitle2)
        )

        # ====== 第三部分：深复制（嵌套列表） ======
        subtitle3 = Text("3. 深复制（嵌套列表的情况）", font="SimSun", color=self.CODE_COLOR, font_size=30)
        subtitle3.next_to(title, DOWN, buff=0.4)
        self.play(Write(subtitle3))

        # 说明浅复制的问题
        problem_text = Text(
            "当列表包含列表时，浅复制只复制外层",
            font="SimSun",
            color=self.TEXT_COLOR,
            font_size=24
        )
        problem_text.next_to(subtitle3, DOWN, buff=0.3)
        self.play(Write(problem_text))

        # 代码示例
        code5 = VGroup(
            Text("import copy", font="Courier New", color=self.TEXT_COLOR, font_size=22),
            Text("list1 = [[1, 2], [3, 4]]", font="Courier New", color=self.TEXT_COLOR, font_size=22),
            Text("list2 = copy.deepcopy(list1)", font="Courier New", color=self.DEEP_COLOR, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        code5.next_to(problem_text, DOWN, buff=0.3).to_edge(LEFT, buff=1)
        self.play(Write(code5))
        self.wait(1)

        # 显示深复制完全独立
        deep_explain = Text(
            "deepcopy() 会递归复制所有嵌套对象，\n确保完全独立！",
            font="SimSun",
            color=self.DEEP_COLOR,
            font_size=24,
            line_spacing=1.2
        )
        deep_explain.next_to(code5, DOWN, buff=0.5)
        self.play(Write(deep_explain))
        self.wait(2)

        # 清除并显示总结
        self.play(
            FadeOut(problem_text),
            FadeOut(code5),
            FadeOut(deep_explain),
            FadeOut(subtitle3)
        )

        # ====== 总结 ======
        summary_title = Text("总结", font="SimSun", color=self.CODE_COLOR, font_size=36)
        summary_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(summary_title))

        summary = VGroup(
            Text("• 引用赋值（=）", font="SimSun", color=self.REFERENCE_COLOR, font_size=26),
            Text("  指向同一对象，修改会互相影响", font="SimSun", color=self.TEXT_COLOR, font_size=22),
            Text("", font="SimSun", font_size=8),
            Text("• 浅复制（.copy() 或 [:]）", font="SimSun", color=self.SHALLOW_COLOR, font_size=26),
            Text("  创建新对象，但嵌套对象仍共享", font="SimSun", color=self.TEXT_COLOR, font_size=22),
            Text("", font="SimSun", font_size=8),
            Text("• 深复制（copy.deepcopy()）", font="SimSun", color=self.DEEP_COLOR, font_size=26),
            Text("  完全独立的副本，包括所有嵌套对象", font="SimSun", color=self.TEXT_COLOR, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        summary.next_to(summary_title, DOWN, buff=0.4)

        self.play(Write(summary), run_time=3)
        self.wait(3)

        # 结束
        self.play(
            FadeOut(summary),
            FadeOut(summary_title),
            FadeOut(title)
        )
        self.wait(0.5)

if __name__ == "__main__":
    config.pixel_height = 2160
    config.pixel_width = 3840
    config.frame_rate = 30

    with tempconfig({"quality": "production_quality", "preview": False}):
        scene = ListCopyAnimation()
        scene.render()
