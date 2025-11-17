from manim import *

class ListIterationAnimation(Scene):
    """列表遍历动画 - 两种遍历方式对比"""
    def __init__(self):
        super().__init__()
        self.camera.background_color = "#FFFFFF"

        # 颜色方案
        self.TEXT_COLOR = "#000000"
        self.SQUARE_COLOR = "#95A5A6"
        self.HIGHLIGHT_COLOR = "#2ECC71"
        self.INDEX_COLOR = "#3498DB"
        self.CODE_COLOR = "#E67E22"
        self.ITEM_COLOR = "#9B59B6"
        self.VAR_NAME_COLOR = "#E74C3C"

        # 使用更好的中文字体
        self.CHINESE_FONT = "Microsoft YaHei"

        # 创建水印
        watermark = Text(
            "作者：温程远",
            font=self.CHINESE_FONT,
            color=self.TEXT_COLOR,
            font_size=24
        ).to_corner(DR, buff=0.3)
        watermark.set_opacity(0.3)
        self.add(watermark)

    def create_list_visualization(self, data, var_name="my_list", position=ORIGIN):
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
            ).shift(RIGHT * i * (square_size + 0.02))
            squares.add(square)

            number = Text(
                str(num),
                font=self.CHINESE_FONT,
                font_size=26,
                color=self.TEXT_COLOR
            ).move_to(square.get_center())
            numbers_text.add(number)

        # 添加索引（在方框上方）
        index_text = VGroup()
        for i in range(len(data)):
            index = Text(
                str(i),
                font=self.CHINESE_FONT,
                font_size=20,
                color=self.INDEX_COLOR
            ).next_to(squares[i], UP, buff=0.2)
            index_text.add(index)

        # 添加变量名
        var_label = Text(
            f"{var_name} = ",
            font="Courier New",
            font_size=28,
            color=self.VAR_NAME_COLOR
        )

        list_group = VGroup(squares, numbers_text)
        var_label.next_to(list_group, LEFT, buff=0.3)

        # 整体居中
        full_group = VGroup(var_label, list_group, index_text)
        full_group.move_to(position)

        return var_label, squares, numbers_text, index_text

    def construct(self):
        # 标题
        title = Text(
            "Python 列表遍历",
            font=self.CHINESE_FONT,
            color=self.TEXT_COLOR,
            font_size=48
        )
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # ====== 场景1：传统索引遍历 ======
        subtitle1 = Text(
            "方法1：传统索引遍历",
            font=self.CHINESE_FONT,
            color=self.CODE_COLOR,
            font_size=36
        )
        subtitle1.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle1))

        # 创建列表
        data = [15, 23, 8, 42, 16]
        var_label, squares, numbers_text, index_text = self.create_list_visualization(
            data, "my_list", ORIGIN + UP * 0.5
        )

        self.play(
            Write(var_label),
            Create(squares),
            Write(numbers_text),
            Write(index_text),
            run_time=1.5
        )
        self.wait(1)

        # 代码示例
        code1 = VGroup(
            Text("for i in range(len(my_list)):", font="Courier New", color=self.CODE_COLOR, font_size=26),
            Text("    print(f'索引{i}: {my_list[i]}')", font="Courier New", color=self.TEXT_COLOR, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        code1.next_to(subtitle1, DOWN, buff=0.4)
        self.play(Write(code1))
        self.wait(1)

        # 创建迭代变量i的显示框
        i_label = Text("i = ", font="Courier New", color=self.INDEX_COLOR, font_size=28)
        i_value_box = Rectangle(
            width=0.8,
            height=0.6,
            stroke_color=self.INDEX_COLOR,
            stroke_width=3
        )
        i_value = Text("0", font=self.CHINESE_FONT, color=self.INDEX_COLOR, font_size=28).move_to(i_value_box)

        i_group = VGroup(i_label, i_value_box, i_value).arrange(RIGHT, buff=0.2)
        i_group.next_to(squares, DOWN, buff=1.2)

        self.play(
            Write(i_label),
            Create(i_value_box),
            Write(i_value)
        )
        self.wait(0.5)

        # 输出显示区域
        output_label = Text("输出:", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24)
        output_label.next_to(i_group, DOWN, buff=0.5).align_to(i_group, LEFT)
        self.play(Write(output_label))

        # 遍历每个元素
        outputs = VGroup()
        for i in range(len(data)):
            # 更新i的值
            new_i_value = Text(str(i), font=self.CHINESE_FONT, color=self.INDEX_COLOR, font_size=28).move_to(i_value_box)
            self.play(Transform(i_value, new_i_value), run_time=0.3)

            # 高亮当前索引
            self.play(
                index_text[i].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.5),
                run_time=0.3
            )
            self.wait(0.2)

            # 高亮对应元素
            self.play(
                squares[i].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
                numbers_text[i].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.3),
                run_time=0.3
            )
            self.wait(0.3)

            # 显示输出
            output_text = Text(
                f"索引{i}: {data[i]}",
                font=self.CHINESE_FONT,
                color=self.TEXT_COLOR,
                font_size=22
            )
            output_text.next_to(output_label, DOWN, buff=0.2 + i * 0.4).align_to(output_label, LEFT)
            outputs.add(output_text)
            self.play(Write(output_text), run_time=0.4)
            self.wait(0.3)

            # 恢复高亮
            self.play(
                index_text[i].animate.set_color(self.INDEX_COLOR).scale(1/1.5),
                squares[i].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
                numbers_text[i].animate.set_color(self.TEXT_COLOR).scale(1/1.3),
                run_time=0.3
            )

        self.wait(2)

        # 清除场景1
        self.play(
            FadeOut(subtitle1),
            FadeOut(code1),
            FadeOut(var_label),
            FadeOut(squares),
            FadeOut(numbers_text),
            FadeOut(index_text),
            FadeOut(i_group),
            FadeOut(output_label),
            FadeOut(outputs)
        )

        # ====== 场景2：直接遍历元素 ======
        subtitle2 = Text(
            "方法2：直接遍历元素",
            font=self.CHINESE_FONT,
            color=self.CODE_COLOR,
            font_size=36
        )
        subtitle2.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle2))

        # 重新创建列表
        var_label2, squares2, numbers_text2, index_text2 = self.create_list_visualization(
            data, "my_list", ORIGIN + UP * 0.5
        )

        self.play(
            Write(var_label2),
            Create(squares2),
            Write(numbers_text2),
            Write(index_text2),
            run_time=1.5
        )
        self.wait(1)

        # 代码示例
        code2 = VGroup(
            Text("for item in my_list:", font="Courier New", color=self.CODE_COLOR, font_size=26),
            Text("    print(item)", font="Courier New", color=self.TEXT_COLOR, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        code2.next_to(subtitle2, DOWN, buff=0.4)
        self.play(Write(code2))
        self.wait(1)

        # 创建item变量的显示框
        item_label = Text("item = ", font="Courier New", color=self.ITEM_COLOR, font_size=28)
        item_value_box = Rectangle(
            width=1.2,
            height=0.6,
            stroke_color=self.ITEM_COLOR,
            stroke_width=3
        )
        item_value = Text("", font=self.CHINESE_FONT, color=self.ITEM_COLOR, font_size=28).move_to(item_value_box)

        item_group = VGroup(item_label, item_value_box, item_value).arrange(RIGHT, buff=0.2)
        item_group.next_to(squares2, DOWN, buff=1.2)

        self.play(
            Write(item_label),
            Create(item_value_box)
        )
        self.wait(0.5)

        # 输出显示区域
        output_label2 = Text("输出:", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24)
        output_label2.next_to(item_group, DOWN, buff=0.5).align_to(item_group, LEFT)
        self.play(Write(output_label2))

        # 遍历每个元素
        outputs2 = VGroup()
        for i in range(len(data)):
            # 高亮当前元素
            self.play(
                squares2[i].animate.set_stroke(color=self.ITEM_COLOR, width=4),
                numbers_text2[i].animate.set_color(self.ITEM_COLOR).scale(1.4),
                run_time=0.4
            )
            self.wait(0.2)

            # 更新item的值
            new_item_value = Text(
                str(data[i]),
                font=self.CHINESE_FONT,
                color=self.ITEM_COLOR,
                font_size=28
            ).move_to(item_value_box)

            if i == 0:
                self.play(Write(new_item_value), run_time=0.4)
                item_value = new_item_value
            else:
                self.play(Transform(item_value, new_item_value), run_time=0.4)

            self.wait(0.3)

            # 显示输出
            output_text2 = Text(
                str(data[i]),
                font=self.CHINESE_FONT,
                color=self.TEXT_COLOR,
                font_size=24
            )
            output_text2.next_to(output_label2, DOWN, buff=0.2 + i * 0.45).align_to(output_label2, LEFT)
            outputs2.add(output_text2)
            self.play(Write(output_text2), run_time=0.4)
            self.wait(0.3)

            # 恢复高亮
            self.play(
                squares2[i].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
                numbers_text2[i].animate.set_color(self.TEXT_COLOR).scale(1/1.4),
                run_time=0.3
            )

        self.wait(2)

        # 清除场景2
        self.play(
            FadeOut(subtitle2),
            FadeOut(code2),
            FadeOut(var_label2),
            FadeOut(squares2),
            FadeOut(numbers_text2),
            FadeOut(index_text2),
            FadeOut(item_group),
            FadeOut(output_label2),
            FadeOut(outputs2)
        )

        # ====== 总结对比 ======
        summary_title = Text(
            "两种方法对比",
            font=self.CHINESE_FONT,
            color=self.CODE_COLOR,
            font_size=36
        )
        summary_title.next_to(title, DOWN, buff=0.6)
        self.play(Write(summary_title))

        comparison = VGroup(
            Text("方法1：for i in range(len(list))", font="Courier New", color=self.INDEX_COLOR, font_size=28),
            Text("  • 适用场景：需要索引位置", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24),
            Text("  • 优点：可以修改列表元素", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24),
            Text("  • 缺点：代码稍显冗长", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24),
            Text("", font=self.CHINESE_FONT, font_size=10),
            Text("方法2：for item in list", font="Courier New", color=self.ITEM_COLOR, font_size=28),
            Text("  • 适用场景：只需要元素值", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24),
            Text("  • 优点：代码简洁清晰", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24),
            Text("  • 缺点：不能直接修改元素", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24),
            Text("", font=self.CHINESE_FONT, font_size=10),
            Text("推荐：优先使用方法2（更Pythonic）", font=self.CHINESE_FONT, color=self.CODE_COLOR, font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        comparison.next_to(summary_title, DOWN, buff=0.5)

        self.play(Write(comparison), run_time=4)
        self.wait(3)

        # 结束
        self.play(
            FadeOut(summary_title),
            FadeOut(comparison),
            FadeOut(title)
        )
        self.wait(0.5)

if __name__ == "__main__":
    config.pixel_height = 2160
    config.pixel_width = 3840
    config.frame_rate = 30

    with tempconfig({"quality": "production_quality", "preview": False}):
        scene = ListIterationAnimation()
        scene.render()
