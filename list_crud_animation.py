from manim import *

class ListCRUDAnimation(Scene):
    """列表的增删查改操作动画 - 修复版"""
    def __init__(self):
        super().__init__()
        self.camera.background_color = "#FFFFFF"

        # 颜色方案
        self.TEXT_COLOR = "#000000"
        self.SQUARE_COLOR = "#95A5A6"
        self.HIGHLIGHT_COLOR = "#2ECC71"
        self.INDEX_COLOR = "#3498DB"
        self.CODE_COLOR = "#E67E22"
        self.DELETE_COLOR = "#E74C3C"
        self.ADD_COLOR = "#27AE60"
        self.VAR_NAME_COLOR = "#9B59B6"

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

    def create_list_visualization(self, data, var_name="numbers", position=ORIGIN):
        """创建列表可视化，包含变量名"""
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

        # 添加索引（在方框下方）
        index_text = VGroup()
        for i in range(len(data)):
            index = Text(
                str(i),
                font=self.CHINESE_FONT,
                font_size=20,
                color=self.INDEX_COLOR
            ).next_to(squares[i], DOWN, buff=0.2)
            index_text.add(index)

        # 添加变量名（在方框左侧）
        var_label = Text(
            f"{var_name} = ",
            font="Courier New",
            font_size=28,
            color=self.VAR_NAME_COLOR
        )

        # 组合所有元素
        list_group = VGroup(squares, numbers_text)
        var_label.next_to(list_group, LEFT, buff=0.3)

        # 整体居中
        full_group = VGroup(var_label, list_group, index_text)
        full_group.move_to(position)

        return var_label, squares, numbers_text, index_text

    def update_indices(self, squares, old_indices):
        """创建更新后的索引标签"""
        new_indices = VGroup()
        for i in range(len(squares)):
            index = Text(
                str(i),
                font=self.CHINESE_FONT,
                font_size=20,
                color=self.INDEX_COLOR
            ).next_to(squares[i], DOWN, buff=0.2)
            new_indices.add(index)
        return new_indices

    def construct(self):
        # 标题
        title = Text(
            "Python 列表操作：增删查改",
            font=self.CHINESE_FONT,
            color=self.TEXT_COLOR,
            font_size=44
        )
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # ====== 第一部分：添加元素 ======
        subtitle1 = Text(
            "1. 添加元素 (Create/Add)",
            font=self.CHINESE_FONT,
            color=self.CODE_COLOR,
            font_size=36
        )
        subtitle1.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle1))

        # 初始列表
        data = [10, 20, 30, 40]
        var_label, squares, numbers_text, index_text = self.create_list_visualization(
            data, "numbers", ORIGIN + DOWN * 0.8
        )

        self.play(
            Write(var_label),
            Create(squares),
            Write(numbers_text),
            Write(index_text),
            run_time=1.5
        )
        self.wait(1)

        # 方法1: append() - 末尾添加
        method1 = Text(
            "numbers.append(50)",
            font="Courier New",
            color=self.CODE_COLOR,
            font_size=28
        )
        method1.next_to(subtitle1, DOWN, buff=0.4)
        self.play(Write(method1))
        self.wait(0.5)

        # 创建新元素
        new_square = Square(
            side_length=0.7,
            stroke_width=2,
            stroke_color=self.ADD_COLOR
        ).next_to(squares[-1], RIGHT, buff=0.02)
        new_number = Text(
            "50",
            font=self.CHINESE_FONT,
            font_size=26,
            color=self.ADD_COLOR
        ).move_to(new_square.get_center())
        new_index = Text(
            "4",
            font=self.CHINESE_FONT,
            font_size=20,
            color=self.INDEX_COLOR
        ).next_to(new_square, DOWN, buff=0.2)

        self.play(
            Create(new_square),
            Write(new_number),
            Write(new_index),
            run_time=1
        )
        self.wait(1)

        # 将新元素变为正常颜色
        self.play(
            new_square.animate.set_stroke(color=self.SQUARE_COLOR),
            new_number.animate.set_color(self.TEXT_COLOR)
        )

        # 更新组
        squares.add(new_square)
        numbers_text.add(new_number)
        index_text.add(new_index)
        data.append(50)

        self.wait(1)
        self.play(FadeOut(method1))

        # 方法2: insert() - 指定位置插入（重点：索引更新）
        method2 = Text(
            "numbers.insert(2, 25)",
            font="Courier New",
            color=self.CODE_COLOR,
            font_size=28
        )
        method2.next_to(subtitle1, DOWN, buff=0.4)
        self.play(Write(method2))

        explain = Text(
            "在索引2处插入，后续元素索引+1",
            font=self.CHINESE_FONT,
            color=self.TEXT_COLOR,
            font_size=22
        )
        explain.next_to(method2, DOWN, buff=0.25)
        self.play(Write(explain))
        self.wait(0.5)

        # 高亮插入位置
        self.play(
            squares[2].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
            index_text[2].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.3)
        )
        self.wait(0.5)

        # 将后面的元素和索引一起右移
        shift_elements = VGroup()
        shift_indices = VGroup()
        for i in range(2, len(squares)):
            shift_elements.add(squares[i], numbers_text[i])
            shift_indices.add(index_text[i])

        self.play(
            shift_elements.animate.shift(RIGHT * 0.72),
            shift_indices.animate.shift(RIGHT * 0.72),
            run_time=1
        )
        self.wait(0.3)

        # 插入新元素
        insert_square = Square(
            side_length=0.7,
            stroke_width=2,
            stroke_color=self.ADD_COLOR
        ).move_to(squares[1].get_center() + RIGHT * 0.72)
        insert_number = Text(
            "25",
            font=self.CHINESE_FONT,
            font_size=26,
            color=self.ADD_COLOR
        ).move_to(insert_square.get_center())
        insert_index = Text(
            "2",
            font=self.CHINESE_FONT,
            font_size=20,
            color=self.ADD_COLOR
        ).next_to(insert_square, DOWN, buff=0.2)

        self.play(
            Create(insert_square),
            Write(insert_number),
            Write(insert_index),
            run_time=0.8
        )
        self.wait(0.5)

        # 更新后续索引值：3→4, 4→5, 5→6
        # 淡出旧索引
        old_indices_to_update = VGroup()
        for i in range(2, len(index_text)):
            old_indices_to_update.add(index_text[i])

        self.play(FadeOut(old_indices_to_update), run_time=0.5)

        # 创建新索引
        new_indices = VGroup()
        current_squares = [sq for sq in squares]
        current_squares.insert(2, insert_square)

        for i in range(2, len(current_squares)):
            new_idx = Text(
                str(i),
                font=self.CHINESE_FONT,
                font_size=20,
                color=self.INDEX_COLOR
            ).next_to(current_squares[i], DOWN, buff=0.2)
            new_indices.add(new_idx)

        self.play(Write(new_indices), run_time=0.8)

        # 重建index_text组
        new_index_text = VGroup()
        for i in range(2):
            new_index_text.add(index_text[i])
        new_index_text.add(insert_index)
        for idx in new_indices:
            new_index_text.add(idx)

        index_text = new_index_text
        squares.add(insert_square)
        numbers_text.add(insert_number)

        self.wait(0.5)

        # 恢复正常颜色
        self.play(
            squares[2].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
            insert_square.animate.set_stroke(color=self.SQUARE_COLOR),
            insert_number.animate.set_color(self.TEXT_COLOR),
            insert_index.animate.set_color(self.INDEX_COLOR),
            FadeOut(explain)
        )

        self.wait(1.5)

        # 清除场景
        self.play(
            FadeOut(method2),
            FadeOut(var_label),
            FadeOut(squares),
            FadeOut(numbers_text),
            FadeOut(index_text),
            FadeOut(subtitle1)
        )

        # ====== 第二部分：删除元素（重点：索引更新） ======
        subtitle2 = Text(
            "2. 删除元素 (Delete)",
            font=self.CHINESE_FONT,
            color=self.CODE_COLOR,
            font_size=36
        )
        subtitle2.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle2))

        # 重新创建列表
        data2 = [10, 20, 30, 40, 50]
        var_label2, squares2, numbers_text2, index_text2 = self.create_list_visualization(
            data2, "numbers", ORIGIN + DOWN * 0.8
        )

        self.play(
            Write(var_label2),
            Create(squares2),
            Write(numbers_text2),
            Write(index_text2),
            run_time=1.5
        )
        self.wait(1)

        # 方法1: remove() - 按值删除
        method3 = Text(
            "numbers.remove(30)",
            font="Courier New",
            color=self.CODE_COLOR,
            font_size=28
        )
        method3.next_to(subtitle2, DOWN, buff=0.4)
        self.play(Write(method3))

        explain2 = Text(
            "删除索引2的元素，后续元素索引-1",
            font=self.CHINESE_FONT,
            color=self.TEXT_COLOR,
            font_size=22
        )
        explain2.next_to(method3, DOWN, buff=0.25)
        self.play(Write(explain2))
        self.wait(0.5)

        # 高亮要删除的元素
        self.play(
            squares2[2].animate.set_stroke(color=self.DELETE_COLOR, width=4),
            numbers_text2[2].animate.set_color(self.DELETE_COLOR).scale(1.2),
            index_text2[2].animate.set_color(self.DELETE_COLOR).scale(1.3)
        )
        self.wait(0.8)

        # 删除元素
        delete_group = VGroup(squares2[2], numbers_text2[2], index_text2[2])
        self.play(FadeOut(delete_group), run_time=0.8)
        self.wait(0.3)

        # 后面元素左移
        shift_left_elements = VGroup()
        shift_left_indices = VGroup()
        for i in range(3, 5):
            shift_left_elements.add(squares2[i], numbers_text2[i])
            shift_left_indices.add(index_text2[i])

        self.play(
            shift_left_elements.animate.shift(LEFT * 0.72),
            shift_left_indices.animate.shift(LEFT * 0.72),
            run_time=1
        )
        self.wait(0.3)

        # 更新索引：3→2, 4→3
        old_delete_indices = VGroup(index_text2[3], index_text2[4])
        self.play(FadeOut(old_delete_indices), run_time=0.5)

        # 创建新索引
        remaining_squares = [squares2[0], squares2[1], squares2[3], squares2[4]]
        new_delete_indices = VGroup()
        for i in range(2, 4):
            new_idx = Text(
                str(i),
                font=self.CHINESE_FONT,
                font_size=20,
                color=self.INDEX_COLOR
            ).next_to(remaining_squares[i], DOWN, buff=0.2)
            new_delete_indices.add(new_idx)

        self.play(Write(new_delete_indices), run_time=0.8)
        self.wait(1.5)

        self.play(
            FadeOut(method3),
            FadeOut(explain2),
            FadeOut(var_label2),
            FadeOut(squares2),
            FadeOut(numbers_text2),
            FadeOut(index_text2),
            FadeOut(new_delete_indices),
            FadeOut(subtitle2)
        )

        # ====== 第三部分：修改元素 ======
        subtitle3 = Text(
            "3. 修改元素 (Update)",
            font=self.CHINESE_FONT,
            color=self.CODE_COLOR,
            font_size=36
        )
        subtitle3.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle3))

        # 重新创建列表
        data3 = [10, 20, 30, 40, 50]
        var_label3, squares3, numbers_text3, index_text3 = self.create_list_visualization(
            data3, "numbers", ORIGIN + DOWN * 0.8
        )

        self.play(
            Write(var_label3),
            Create(squares3),
            Write(numbers_text3),
            Write(index_text3),
            run_time=1.5
        )
        self.wait(1)

        # 修改元素
        method4 = Text(
            "numbers[2] = 99",
            font="Courier New",
            color=self.CODE_COLOR,
            font_size=28
        )
        method4.next_to(subtitle3, DOWN, buff=0.4)
        self.play(Write(method4))
        self.wait(0.5)

        # 高亮要修改的元素
        self.play(
            squares3[2].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
            numbers_text3[2].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.3),
            index_text3[2].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.3)
        )
        self.wait(0.5)

        # 修改值
        new_value = Text(
            "99",
            font=self.CHINESE_FONT,
            font_size=26,
            color=self.HIGHLIGHT_COLOR
        ).move_to(numbers_text3[2])
        self.play(Transform(numbers_text3[2], new_value), run_time=0.8)
        self.wait(0.5)

        # 恢复正常颜色
        self.play(
            squares3[2].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
            numbers_text3[2].animate.set_color(self.TEXT_COLOR).scale(1/1.3),
            index_text3[2].animate.set_color(self.INDEX_COLOR).scale(1/1.3)
        )
        self.wait(1)

        self.play(
            FadeOut(method4),
            FadeOut(var_label3),
            FadeOut(squares3),
            FadeOut(numbers_text3),
            FadeOut(index_text3),
            FadeOut(subtitle3)
        )

        # ====== 第四部分：查找元素 ======
        subtitle4 = Text(
            "4. 查找元素 (Read)",
            font=self.CHINESE_FONT,
            color=self.CODE_COLOR,
            font_size=36
        )
        subtitle4.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle4))

        # 重新创建列表
        data4 = [10, 20, 30, 40, 50]
        var_label4, squares4, numbers_text4, index_text4 = self.create_list_visualization(
            data4, "numbers", ORIGIN + DOWN * 0.8
        )

        self.play(
            Write(var_label4),
            Create(squares4),
            Write(numbers_text4),
            Write(index_text4),
            run_time=1.5
        )
        self.wait(1)

        # 方法1: 通过索引访问
        method5 = Text(
            "numbers[3] → 40",
            font="Courier New",
            color=self.TEXT_COLOR,
            font_size=28
        )
        method5.next_to(subtitle4, DOWN, buff=0.4)
        self.play(Write(method5))

        self.play(
            squares4[3].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
            numbers_text4[3].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.3),
            index_text4[3].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.3)
        )
        self.wait(1.2)

        self.play(
            squares4[3].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
            numbers_text4[3].animate.set_color(self.TEXT_COLOR).scale(1/1.3),
            index_text4[3].animate.set_color(self.INDEX_COLOR).scale(1/1.3),
            FadeOut(method5)
        )

        # 方法2: index() - 查找值的索引
        method6 = Text(
            "numbers.index(30) → 2",
            font="Courier New",
            color=self.TEXT_COLOR,
            font_size=28
        )
        method6.next_to(subtitle4, DOWN, buff=0.4)
        self.play(Write(method6))

        # 先高亮值30
        self.play(
            squares4[2].animate.set_stroke(color=self.CODE_COLOR, width=4),
            numbers_text4[2].animate.set_color(self.CODE_COLOR).scale(1.3)
        )
        self.wait(0.5)

        # 然后高亮返回的索引
        self.play(
            index_text4[2].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.5)
        )
        self.wait(1.5)

        # 结束
        self.play(
            FadeOut(method6),
            FadeOut(var_label4),
            FadeOut(squares4),
            FadeOut(numbers_text4),
            FadeOut(index_text4),
            FadeOut(subtitle4),
            FadeOut(title)
        )
        self.wait(0.5)

if __name__ == "__main__":
    config.pixel_height = 2160
    config.pixel_width = 3840
    config.frame_rate = 30

    with tempconfig({"quality": "production_quality", "preview": False}):
        scene = ListCRUDAnimation()
        scene.render()
