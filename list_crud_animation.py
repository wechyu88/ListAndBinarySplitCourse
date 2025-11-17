from manim import *

class ListCRUDAnimation(Scene):
    """列表的增删查改操作动画"""
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

        # 添加索引
        index_text = VGroup()
        for i in range(len(data)):
            index = Text(
                str(i),
                font="SimSun",
                font_size=20,
                color=self.INDEX_COLOR
            ).next_to(squares[i], DOWN, buff=0.15)
            index_text.add(index)

        return squares, numbers_text, index_text

    def construct(self):
        # 标题
        title = Text("Python 列表操作：增删查改", font="SimSun", color=self.TEXT_COLOR, font_size=44)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # ====== 第一部分：添加元素 ======
        subtitle1 = Text("1. 添加元素 (Create/Add)", font="SimSun", color=self.CODE_COLOR, font_size=36)
        subtitle1.next_to(title, DOWN, buff=0.5)
        self.play(Write(subtitle1))

        # 初始列表
        data = [10, 20, 30, 40]
        squares, numbers_text, index_text = self.create_list_visualization(data, ORIGIN + DOWN * 0.5)

        self.play(
            Create(squares),
            Write(numbers_text),
            Write(index_text)
        )
        self.wait(1)

        # 方法1: append() - 末尾添加
        method1 = Text("append(50) - 在末尾添加元素", font="SimSun", color=self.TEXT_COLOR, font_size=28)
        method1.next_to(subtitle1, DOWN, buff=0.3)
        self.play(Write(method1))
        self.wait(0.5)

        # 创建新元素
        new_square = Square(
            side_length=0.7,
            stroke_width=2,
            stroke_color=self.ADD_COLOR
        ).next_to(squares[-1], RIGHT, buff=0.02)
        new_number = Text("50", font="SimSun", font_size=26, color=self.ADD_COLOR).move_to(new_square.get_center())
        new_index = Text("4", font="SimSun", font_size=20, color=self.INDEX_COLOR).next_to(new_square, DOWN, buff=0.15)

        self.play(
            Create(new_square),
            Write(new_number),
            Write(new_index)
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

        self.wait(0.5)
        self.play(FadeOut(method1))

        # 方法2: insert() - 指定位置插入
        method2 = Text("insert(2, 25) - 在索引2处插入元素", font="SimSun", color=self.TEXT_COLOR, font_size=28)
        method2.next_to(subtitle1, DOWN, buff=0.3)
        self.play(Write(method2))
        self.wait(0.5)

        # 高亮插入位置
        self.play(
            squares[2].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
            index_text[2].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.3)
        )
        self.wait(0.5)

        # 将后面的元素右移
        shift_group = VGroup()
        for i in range(2, len(squares)):
            shift_group.add(squares[i], numbers_text[i], index_text[i])

        self.play(shift_group.animate.shift(RIGHT * 0.72))

        # 插入新元素
        insert_square = Square(
            side_length=0.7,
            stroke_width=2,
            stroke_color=self.ADD_COLOR
        ).move_to(squares[1].get_center() + RIGHT * 0.72)
        insert_number = Text("25", font="SimSun", font_size=26, color=self.ADD_COLOR).move_to(insert_square.get_center())

        self.play(
            Create(insert_square),
            Write(insert_number)
        )

        # 恢复高亮
        self.play(
            squares[2].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
            index_text[2].animate.set_color(self.INDEX_COLOR).scale(1/1.3),
            insert_square.animate.set_stroke(color=self.SQUARE_COLOR),
            insert_number.animate.set_color(self.TEXT_COLOR)
        )

        self.wait(1)

        # 清除场景准备下一部分
        self.play(
            FadeOut(method2),
            FadeOut(squares),
            FadeOut(numbers_text),
            FadeOut(index_text),
            FadeOut(insert_square),
            FadeOut(insert_number),
            FadeOut(subtitle1)
        )

        # ====== 第二部分：删除元素 ======
        subtitle2 = Text("2. 删除元素 (Delete)", font="SimSun", color=self.CODE_COLOR, font_size=36)
        subtitle2.next_to(title, DOWN, buff=0.5)
        self.play(Write(subtitle2))

        # 重新创建列表
        data2 = [10, 20, 30, 40, 50]
        squares2, numbers_text2, index_text2 = self.create_list_visualization(data2, ORIGIN + DOWN * 0.5)

        self.play(
            Create(squares2),
            Write(numbers_text2),
            Write(index_text2)
        )
        self.wait(1)

        # 方法1: remove() - 按值删除
        method3 = Text("remove(30) - 删除值为30的元素", font="SimSun", color=self.TEXT_COLOR, font_size=28)
        method3.next_to(subtitle2, DOWN, buff=0.3)
        self.play(Write(method3))
        self.wait(0.5)

        # 高亮要删除的元素
        self.play(
            squares2[2].animate.set_stroke(color=self.DELETE_COLOR, width=4),
            numbers_text2[2].animate.set_color(self.DELETE_COLOR).scale(1.2)
        )
        self.wait(0.5)

        # 删除元素
        delete_group = VGroup(squares2[2], numbers_text2[2], index_text2[2])
        self.play(FadeOut(delete_group))

        # 后面元素左移
        shift_left = VGroup()
        for i in range(3, len(squares2)):
            shift_left.add(squares2[i], numbers_text2[i], index_text2[i])

        self.play(shift_left.animate.shift(LEFT * 0.72))
        self.wait(1)

        self.play(
            FadeOut(method3),
            FadeOut(squares2),
            FadeOut(numbers_text2),
            FadeOut(index_text2),
            FadeOut(subtitle2)
        )

        # ====== 第三部分：修改元素 ======
        subtitle3 = Text("3. 修改元素 (Update)", font="SimSun", color=self.CODE_COLOR, font_size=36)
        subtitle3.next_to(title, DOWN, buff=0.5)
        self.play(Write(subtitle3))

        # 重新创建列表
        data3 = [10, 20, 30, 40, 50]
        squares3, numbers_text3, index_text3 = self.create_list_visualization(data3, ORIGIN + DOWN * 0.5)

        self.play(
            Create(squares3),
            Write(numbers_text3),
            Write(index_text3)
        )
        self.wait(1)

        # 修改元素
        method4 = Text("numbers[2] = 35 - 修改索引2的值", font="SimSun", color=self.TEXT_COLOR, font_size=28)
        method4.next_to(subtitle3, DOWN, buff=0.3)
        self.play(Write(method4))
        self.wait(0.5)

        # 高亮要修改的元素
        self.play(
            squares3[2].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
            numbers_text3[2].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.2)
        )
        self.wait(0.5)

        # 修改值
        new_value = Text("35", font="SimSun", font_size=26, color=self.HIGHLIGHT_COLOR).move_to(numbers_text3[2])
        self.play(Transform(numbers_text3[2], new_value))
        self.wait(0.5)

        # 恢复正常颜色
        self.play(
            squares3[2].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
            numbers_text3[2].animate.set_color(self.TEXT_COLOR).scale(1/1.2)
        )
        self.wait(1)

        self.play(
            FadeOut(method4),
            FadeOut(squares3),
            FadeOut(numbers_text3),
            FadeOut(index_text3),
            FadeOut(subtitle3)
        )

        # ====== 第四部分：查找元素 ======
        subtitle4 = Text("4. 查找元素 (Read)", font="SimSun", color=self.CODE_COLOR, font_size=36)
        subtitle4.next_to(title, DOWN, buff=0.5)
        self.play(Write(subtitle4))

        # 重新创建列表
        data4 = [10, 20, 30, 40, 50]
        squares4, numbers_text4, index_text4 = self.create_list_visualization(data4, ORIGIN + DOWN * 0.5)

        self.play(
            Create(squares4),
            Write(numbers_text4),
            Write(index_text4)
        )
        self.wait(1)

        # 方法1: 通过索引访问
        method5 = Text("numbers[3] → 40", font="Courier New", color=self.TEXT_COLOR, font_size=28)
        method5.next_to(subtitle4, DOWN, buff=0.3)
        self.play(Write(method5))

        self.play(
            squares4[3].animate.set_stroke(color=self.HIGHLIGHT_COLOR, width=4),
            numbers_text4[3].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.3)
        )
        self.wait(1)

        self.play(
            squares4[3].animate.set_stroke(color=self.SQUARE_COLOR, width=2),
            numbers_text4[3].animate.set_color(self.TEXT_COLOR).scale(1/1.3),
            FadeOut(method5)
        )

        # 方法2: index() - 查找值的索引
        method6 = Text("numbers.index(30) → 2", font="Courier New", color=self.TEXT_COLOR, font_size=28)
        method6.next_to(subtitle4, DOWN, buff=0.3)
        self.play(Write(method6))

        self.play(
            squares4[2].animate.set_stroke(color=self.INDEX_COLOR, width=4),
            numbers_text4[2].animate.set_color(self.INDEX_COLOR).scale(1.3),
            index_text4[2].animate.set_color(self.HIGHLIGHT_COLOR).scale(1.5)
        )
        self.wait(1.5)

        # 结束
        self.play(
            FadeOut(method6),
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
