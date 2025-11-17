from manim import *

class LinearSearchAnimation(Scene):

    def create_comparison_text(self, num1, num2, operation):
        # 创建一个VGroup来组合不同颜色的文本
        text_group = VGroup()
        
        # 第一个数字
        first_num = Text(
            num1,
            font="SimSun",
            font_size=32,
            color=self.TEXT_COLOR
        )
        
        # 操作符
        op = Text(
            f" {operation} ",
            font="SimSun",
            font_size=32,
            color=self.TEXT_COLOR
        ).next_to(first_num, RIGHT, buff=0.1)
        
        # 目标值（红色）
        second_num = Text(
            num2,
            font="SimSun",
            font_size=32,
            color=self.NOT_FOUND_COLOR  # 使用红色
        ).next_to(op, RIGHT, buff=0.1)
        
        text_group.add(first_num, op, second_num)
        text_group.arrange(RIGHT, buff=0.1)
        return text_group




    def create_reasoning_text(self, text):
        return Text(
            text,
            font="SimSun",
            font_size=28,
            color=self.TEXT_COLOR
        )

    def __init__(self):
        super().__init__()
        # 设置背景颜色为浅灰色背景
        self.camera.background_color = "#FFFFFF"
        
        # 优化颜色方案
        self.TEXT_COLOR = "#000000"      # 深蓝灰色文字
        self.SQUARE_COLOR = "#95A5A6"     # 柔和的灰色方块边框
        self.CURRENT_COLOR = "#3498DB"    # 当前检查的元素颜色
        self.HIGHLIGHT_COLOR = "#2ECC71"  # 找到目标时的颜色
        self.NOT_FOUND_COLOR = "#E74C3C"  # 未找到时的颜色（红色）
        self.SCANNED_COLOR = "#9B59B6"    # 已扫描标记颜色（紫色）

                
        watermark = Text(
            "作者：温程远", 
            font="SimSun",
            color=self.TEXT_COLOR,
            font_size=24
        ).to_corner(DR, buff=0.3)  # DR表示右下角
        watermark.set_opacity(0.3)  # 设置透明度
        
        # 将水印添加到场景
        self.add(watermark)

        # 使用与二分查找相同的数组
        self.numbers = [2, 5, 8, 13, 17, 22, 26, 31, 35, 39, 44, 48, 53, 57, 62, 66, 71, 75, 80, 85]
        self.target = 53

        # 创建标题
        self.title = Text("线性查找演示", font="SimSun", color=self.TEXT_COLOR).to_edge(UP, buff=0.3)
        self.play(Write(self.title))
        
        # 创建数组可视化
        self.squares = VGroup()
        self.numbers_text = VGroup()
        self.index_text = VGroup()
        
        # 设置方块属性
        self.square_size = 0.7
        self.stroke_width = 2
        
        # 创建方块、数字和索引
        for i, num in enumerate(self.numbers):
            square = Square(
                side_length=self.square_size,
                stroke_width=self.stroke_width,
                stroke_color=self.SQUARE_COLOR
            ).shift(RIGHT * i * (self.square_size + self.stroke_width/100))
            self.squares.add(square)
            
            # 如果数字等于目标值，使用红色显示
            number_color = self.NOT_FOUND_COLOR if num == self.target else self.TEXT_COLOR
            number = Text(
                str(num), 
                font="SimSun", 
                font_size=24, 
                color=number_color
            ).move_to(square.get_center())
            self.numbers_text.add(number)
            
            index = Text(str(i), font="SimSun", font_size=20, color=self.TEXT_COLOR).next_to(square, DOWN, buff=0.2)
            self.index_text.add(index)
        
        self.array_group = VGroup(self.squares, self.numbers_text, self.index_text)
        self.array_group.move_to(ORIGIN + UP * 0.5)
        self.array_group.scale_to_fit_width(config.frame_width - 1)
        
        self.play(
            Create(self.squares),
            Write(self.numbers_text),
            Write(self.index_text)
        )
        

        
        # 添加用于存储已检查和已跳过元素的标记
        self.scanned_marks = VGroup()  # 已扫描标记
        
        # 为每个方块预创建标记（初始时不可见）
        for square in self.squares:
            # 创建已扫描标记（交叉线）
            scanned = VGroup(
                Line(
                    square.get_corner(UL), 
                    square.get_corner(DR),
                    color=self.SCANNED_COLOR,
                    stroke_width=2
                ),
                Line(
                    square.get_corner(UR),
                    square.get_corner(DL),
                    color=self.SCANNED_COLOR,
                    stroke_width=2
                )
            ).set_opacity(0)
            self.scanned_marks.add(scanned)

                
        # 修改目标值文本，将目标值显示为红色
        target_text_group = VGroup(
            Text("查找目标值: ", font="SimSun", font_size=36, color=self.TEXT_COLOR),
            Text(str(self.target), font="SimSun", font_size=36, color=self.NOT_FOUND_COLOR)
        ).arrange(RIGHT, buff=0.1)
        
        self.target_text = target_text_group.next_to(self.title, DOWN, buff=0.3)
        self.play(Write(self.target_text))


    def mark_scanned(self, index):
        """标记已扫描的元素"""
        return AnimationGroup(
            self.squares[index].animate.set_stroke(opacity=0.6),
            self.numbers_text[index].animate.set_opacity(0.6),
            self.index_text[index].animate.set_opacity(0.6),
            self.scanned_marks[index].animate.set_opacity(1),
            lag_ratio=0.1
        )

    def construct(self):
        # 创建当前索引指示器
        pointer = Arrow(
            start=DOWN * 0.4,
            end=UP * 0.4,
            color=self.CURRENT_COLOR,
            max_tip_length_to_length_ratio=0.3,
            max_stroke_width_to_length_ratio=5,
            tip_length=0.2
        ).next_to(self.squares[0], DOWN, buff=0.7)
        
        pointer_label = Text("current", font="SimSun", color=self.CURRENT_COLOR, font_size=24).next_to(pointer, DOWN, buff=0.1)
        
        self.play(
            Create(pointer),
            Write(pointer_label)
        )

        found = False
        
        for i in range(len(self.numbers)):
            # 更新指针位置
            self.play(
                pointer.animate.next_to(self.squares[i], DOWN, buff=0.7),
                pointer_label.animate.next_to(self.squares[i], DOWN, buff=1.2)
            )
            
            # 高亮当前检查的元素
            self.play(self.squares[i].animate.set_stroke(color=self.CURRENT_COLOR))
            
            # 创建比较过程的文本
            
            comparison_text = self.create_comparison_text(
                f"list[{i}]", 
                str(self.target),
                "==" if self.numbers[i] == self.target else ("<" if self.numbers[i] < self.target else ">")
            ).next_to(self.target_text, DOWN, buff=2).shift(DOWN*1.5)

            self.play(Write(comparison_text))
            
            if self.numbers[i] == self.target:
                found = True
                # 找到目标值
                reasoning = self.create_reasoning_text(
                    f"找到目标值！位于索引 {i}"
                ).next_to(comparison_text, DOWN, buff=0.3)
                
                self.play(
                    Write(reasoning),
                    self.squares[i].animate.set_stroke(color=self.HIGHLIGHT_COLOR)
                )
                break
            else:
                # 未找到，继续搜索
                reasoning = self.create_reasoning_text(
                    f"不是目标值，继续向后搜索"
                ).next_to(comparison_text, DOWN, buff=0.3)
                
                self.play(Write(reasoning))
                
                self.play(self.mark_scanned(i))



                # 恢复方块颜色并移除文本
                self.play(
                    self.squares[i].animate.set_stroke(color=self.SQUARE_COLOR),
                    FadeOut(comparison_text),
                    FadeOut(reasoning)
                )

        if not found:
            # 目标值不在数组中
            not_found_text = Text(
                f"目标值 {self.target} 不存在于数组中！",
                font="SimSun",
                color=self.NOT_FOUND_COLOR,
                font_size=36
            ).next_to(self.target_text, DOWN, buff=1.5)
            
            self.play(Write(not_found_text))

        self.wait(2)

if __name__ == "__main__":
    config.pixel_height = 1080
    config.pixel_width = 1920
    config.frame_rate = 30
    
    with tempconfig({"quality": "production_quality", "preview": True}):
        scene = LinearSearchAnimation()
        scene.render()