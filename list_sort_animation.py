from manim import *

class ListSortAnimation(Scene):
    """列表排序动画 - sort() vs sorted() 对比"""
    def __init__(self):
        super().__init__()
        self.camera.background_color = "#FFFFFF"

        # 颜色方案
        self.TEXT_COLOR = "#000000"
        self.SQUARE_COLOR = "#95A5A6"
        self.SORT_COLOR = "#9B59B6"
        self.SORTED_COLOR = "#2ECC71"
        self.CODE_COLOR = "#E67E22"
        self.VAR_NAME_COLOR = "#E74C3C"
        self.HIGHLIGHT_COLOR = "#3498DB"

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

    def create_list_visualization(self, data, var_name="my_list", position=ORIGIN, color=None):
        """创建列表可视化"""
        squares = VGroup()
        numbers_text = VGroup()

        square_size = 0.65
        stroke_width = 2
        if color is None:
            color = self.SQUARE_COLOR

        for i, num in enumerate(data):
            square = Square(
                side_length=square_size,
                stroke_width=stroke_width,
                stroke_color=color
            ).shift(RIGHT * i * (square_size + 0.02))
            squares.add(square)

            number = Text(
                str(num),
                font=self.CHINESE_FONT,
                font_size=24,
                color=self.TEXT_COLOR
            ).move_to(square.get_center())
            numbers_text.add(number)

        # 添加变量名
        var_label = Text(
            f"{var_name} = ",
            font="Courier New",
            font_size=26,
            color=self.VAR_NAME_COLOR
        )

        list_group = VGroup(squares, numbers_text)
        var_label.next_to(list_group, LEFT, buff=0.3)

        # 整体定位
        full_group = VGroup(var_label, list_group)
        full_group.move_to(position)

        return var_label, squares, numbers_text

    def construct(self):
        # 标题
        title = Text(
            "Python 列表排序：sort() vs sorted()",
            font=self.CHINESE_FONT,
            color=self.TEXT_COLOR,
            font_size=44
        )
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # ====== 场景1：list.sort() - 原地排序 ======
        subtitle1 = Text(
            "方法1：list.sort() - 原地排序",
            font=self.CHINESE_FONT,
            color=self.SORT_COLOR,
            font_size=34
        )
        subtitle1.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle1))

        # 创建列表
        data1 = [3, 1, 4, 1, 5, 9, 2]
        var_label1, squares1, numbers_text1 = self.create_list_visualization(
            data1, "my_list", ORIGIN + UP * 0.3
        )

        self.play(
            Write(var_label1),
            Create(squares1),
            Write(numbers_text1),
            run_time=1.5
        )
        self.wait(1)

        # 代码示例
        code1 = Text(
            "my_list.sort()  # 原地修改，无返回值",
            font="Courier New",
            color=self.SORT_COLOR,
            font_size=26
        )
        code1.next_to(subtitle1, DOWN, buff=0.4)
        self.play(Write(code1))
        self.wait(0.8)

        # 标注
        note1 = Text(
            "⚠️ 直接修改原列表对象",
            font=self.CHINESE_FONT,
            color=self.SORT_COLOR,
            font_size=24
        )
        note1.next_to(var_label1, DOWN, buff=1.5).align_to(var_label1, LEFT)
        self.play(Write(note1))
        self.wait(0.5)

        # 高亮所有元素准备排序
        self.play(
            *[squares1[i].animate.set_stroke(color=self.SORT_COLOR, width=3) for i in range(len(data1))],
            run_time=0.8
        )
        self.wait(0.5)

        # 排序动画 - 使用冒泡排序可视化
        sorted_data1 = sorted(data1)

        # 创建排序后的位置
        new_squares1 = VGroup()
        new_numbers1 = VGroup()

        for i, num in enumerate(sorted_data1):
            square = Square(
                side_length=0.65,
                stroke_width=2,
                stroke_color=self.SORT_COLOR
            ).shift(RIGHT * i * (0.65 + 0.02))
            new_squares1.add(square)

            number = Text(
                str(num),
                font=self.CHINESE_FONT,
                font_size=24,
                color=self.TEXT_COLOR
            ).move_to(square.get_center())
            new_numbers1.add(number)

        new_list_group1 = VGroup(new_squares1, new_numbers1)
        new_list_group1.next_to(var_label1, RIGHT, buff=0.3)

        # 移动元素到新位置
        animations = []
        for i in range(len(data1)):
            original_value = data1[i]
            sorted_idx = None

            # 找到该值在排序后的位置
            for j, val in enumerate(sorted_data1):
                if val == original_value and j not in [animations[k][2] for k in range(len(animations))]:
                    sorted_idx = j
                    break

            if sorted_idx is None:
                sorted_idx = sorted_data1.index(original_value)

            animations.append((
                squares1[i].animate.move_to(new_squares1[sorted_idx]),
                numbers_text1[i].animate.move_to(new_numbers1[sorted_idx]),
                sorted_idx
            ))

        self.play(
            *[anim[0] for anim in animations],
            *[anim[1] for anim in animations],
            run_time=2
        )
        self.wait(1)

        # 结果说明
        result1 = Text(
            "排序后: [1, 1, 2, 3, 4, 5, 9]",
            font="Courier New",
            color=self.SORT_COLOR,
            font_size=26
        )
        result1.next_to(note1, DOWN, buff=0.4).align_to(note1, LEFT)
        self.play(Write(result1))
        self.wait(2)

        # 清除场景1
        self.play(
            FadeOut(subtitle1),
            FadeOut(code1),
            FadeOut(var_label1),
            FadeOut(squares1),
            FadeOut(numbers_text1),
            FadeOut(note1),
            FadeOut(result1)
        )

        # ====== 场景2：sorted() - 返回新列表 ======
        subtitle2 = Text(
            "方法2：sorted() - 返回新列表",
            font=self.CHINESE_FONT,
            color=self.SORTED_COLOR,
            font_size=34
        )
        subtitle2.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle2))

        # 创建原始列表
        data2 = [3, 1, 4, 1, 5, 9, 2]
        var_label2, squares2, numbers_text2 = self.create_list_visualization(
            data2, "original", ORIGIN + UP * 1.2
        )

        self.play(
            Write(var_label2),
            Create(squares2),
            Write(numbers_text2),
            run_time=1.5
        )
        self.wait(1)

        # 代码示例
        code2 = Text(
            "sorted_list = sorted(original)",
            font="Courier New",
            color=self.SORTED_COLOR,
            font_size=26
        )
        code2.next_to(subtitle2, DOWN, buff=0.4)
        self.play(Write(code2))
        self.wait(0.8)

        # 标注原列表
        note2_original = Text(
            "✅ 原列表保持不变",
            font=self.CHINESE_FONT,
            color=self.HIGHLIGHT_COLOR,
            font_size=24
        )
        note2_original.next_to(var_label2, LEFT, buff=0.3)
        self.play(Write(note2_original))
        self.wait(0.5)

        # 高亮原列表
        self.play(
            *[squares2[i].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=3) for i in range(len(data2))],
            run_time=0.8
        )
        self.wait(0.5)

        # 创建新列表（复制动画）
        sorted_data2 = sorted(data2)
        var_label3, squares3, numbers_text3 = self.create_list_visualization(
            sorted_data2, "sorted_list", ORIGIN + DOWN * 0.8, color=self.SORTED_COLOR
        )

        # 先创建未排序的副本
        temp_squares = VGroup()
        temp_numbers = VGroup()
        for i in range(len(data2)):
            sq_copy = squares2[i].copy()
            num_copy = numbers_text2[i].copy()
            temp_squares.add(sq_copy)
            temp_numbers.add(num_copy)

        temp_group = VGroup(temp_squares, temp_numbers)
        temp_group.next_to(var_label3, RIGHT, buff=0.3)

        # 显示变量名和复制列表
        self.play(
            Write(var_label3),
            TransformFromCopy(squares2, temp_squares),
            TransformFromCopy(numbers_text2, temp_numbers),
            run_time=1.5
        )
        self.wait(0.5)

        # 标注新列表
        note2_sorted = Text(
            "🔄 创建新的排序列表",
            font=self.CHINESE_FONT,
            color=self.SORTED_COLOR,
            font_size=24
        )
        note2_sorted.next_to(var_label3, LEFT, buff=0.3)
        self.play(Write(note2_sorted))
        self.wait(0.5)

        # 在新列表上排序
        self.play(
            *[temp_squares[i].animate.set_stroke(color=self.SORTED_COLOR, width=3) for i in range(len(data2))],
            run_time=0.8
        )

        # 移动到排序位置
        animations2 = []
        for i in range(len(data2)):
            original_value = data2[i]
            sorted_idx = sorted_data2.index(original_value)

            animations2.append((
                temp_squares[i].animate.move_to(squares3[sorted_idx]),
                temp_numbers[i].animate.move_to(numbers_text3[sorted_idx])
            ))

        self.play(
            *[anim[0] for anim in animations2],
            *[anim[1] for anim in animations2],
            run_time=2
        )
        self.wait(1)

        # 结果说明
        result2 = VGroup(
            Text("原列表: [3, 1, 4, 1, 5, 9, 2]", font="Courier New", color=self.HIGHLIGHT_COLOR, font_size=24),
            Text("新列表: [1, 1, 2, 3, 4, 5, 9]", font="Courier New", color=self.SORTED_COLOR, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        result2.next_to(note2_sorted, DOWN, buff=0.8).align_to(note2_sorted, LEFT)
        self.play(Write(result2))
        self.wait(2)

        # 清除场景2
        self.play(
            FadeOut(subtitle2),
            FadeOut(code2),
            FadeOut(var_label2),
            FadeOut(squares2),
            FadeOut(numbers_text2),
            FadeOut(note2_original),
            FadeOut(var_label3),
            FadeOut(temp_squares),
            FadeOut(temp_numbers),
            FadeOut(note2_sorted),
            FadeOut(result2)
        )

        # ====== 总结对比 ======
        summary_title = Text(
            "总结对比",
            font=self.CHINESE_FONT,
            color=self.CODE_COLOR,
            font_size=36
        )
        summary_title.next_to(title, DOWN, buff=0.6)
        self.play(Write(summary_title))

        comparison_table = VGroup(
            # 表头
            VGroup(
                Text("特性", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=28),
                Text("list.sort()", font="Courier New", color=self.SORT_COLOR, font_size=28),
                Text("sorted()", font="Courier New", color=self.SORTED_COLOR, font_size=28)
            ).arrange(RIGHT, buff=1.5),

            # 分隔线（用文字表示）
            Text("─" * 60, font="Courier New", color=self.TEXT_COLOR, font_size=20),

            # 第1行
            VGroup(
                Text("返回值", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24),
                Text("None", font="Courier New", color=self.SORT_COLOR, font_size=24),
                Text("新列表", font=self.CHINESE_FONT, color=self.SORTED_COLOR, font_size=24)
            ).arrange(RIGHT, buff=1.2),

            # 第2行
            VGroup(
                Text("原列表", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24),
                Text("被修改", font=self.CHINESE_FONT, color=self.SORT_COLOR, font_size=24),
                Text("不变", font=self.CHINESE_FONT, color=self.SORTED_COLOR, font_size=24)
            ).arrange(RIGHT, buff=1.2),

            # 第3行
            VGroup(
                Text("适用对象", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24),
                Text("仅列表", font=self.CHINESE_FONT, color=self.SORT_COLOR, font_size=24),
                Text("任何可迭代对象", font=self.CHINESE_FONT, color=self.SORTED_COLOR, font_size=24)
            ).arrange(RIGHT, buff=0.6),

            # 第4行
            VGroup(
                Text("内存", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=24),
                Text("节省空间", font=self.CHINESE_FONT, color=self.SORT_COLOR, font_size=24),
                Text("需要额外空间", font=self.CHINESE_FONT, color=self.SORTED_COLOR, font_size=24)
            ).arrange(RIGHT, buff=0.8)
        ).arrange(DOWN, buff=0.35)

        # 对齐表格列
        for i in range(2, len(comparison_table)):
            comparison_table[i].align_to(comparison_table[0], LEFT)

        comparison_table.next_to(summary_title, DOWN, buff=0.5)

        self.play(Write(comparison_table), run_time=4)
        self.wait(2)

        # 推荐建议
        recommendation = Text(
            "💡 推荐：需要保留原列表时使用 sorted()，否则使用 sort() 更高效",
            font=self.CHINESE_FONT,
            color=self.CODE_COLOR,
            font_size=24
        )
        recommendation.next_to(comparison_table, DOWN, buff=0.6)
        self.play(Write(recommendation))
        self.wait(3)

        # 结束
        self.play(
            FadeOut(summary_title),
            FadeOut(comparison_table),
            FadeOut(recommendation),
            FadeOut(title)
        )
        self.wait(0.5)

if __name__ == "__main__":
    config.pixel_height = 2160
    config.pixel_width = 3840
    config.frame_rate = 30

    with tempconfig({"quality": "production_quality", "preview": False}):
        scene = ListSortAnimation()
        scene.render()
