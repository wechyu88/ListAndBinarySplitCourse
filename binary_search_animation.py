from manim import *
import random

class BinarySearchAnimation(Scene):
    def create_comparison_text(self, num1, num2, operation):
        return VGroup(
            Text(f"list[{num1.split(']')[0].split('[')[1]}]", font="SimSun", font_size=32, color=self.TEXT_COLOR),
            Text(f" {operation} ", font="SimSun", font_size=32, color=self.TEXT_COLOR),
            Text(str(num2), font="SimSun", font_size=32, color=RED)
        ).arrange(RIGHT, buff=0.1)

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
        
        # 创建水印
        
        # 优化颜色方案
        self.TEXT_COLOR = "#000000"      # 深蓝灰色文字
        self.SQUARE_COLOR = "#95A5A6"     # 柔和的灰色方块边框
        self.LOW_COLOR = "#3498DB"        # 明亮的蓝色
        self.HIGH_COLOR = "#E67E22"       # 温暖的橙色
        self.MID_COLOR = "#9B59B6"        # 优雅的紫色
        self.HIGHLIGHT_COLOR = "#2ECC71"  # 清新的绿色
        self.NOT_FOUND_COLOR = "#FF0000"  # 红色
        self.SCANNED_COLOR = "#9B59B6"    # 已扫描标记颜色（紫色）
        self.SKIPPED_COLOR = "#95A5A6"    # 已跳过标记颜色（灰色）
        
        
        watermark = Text(
            "作者：温程远", 
            font="SimSun",
            color=self.TEXT_COLOR,
            font_size=24
        ).to_corner(DR, buff=0.3)  # DR表示右下角
        watermark.set_opacity(0.3)  # 设置透明度
        
        # 将水印添加到场景
        self.add(watermark)
        # 创建一个固定的有序数组，选择一个需要多次查找的目标值
        #self.numbers = [3, 7, 12, 15, 18, 22, 26, 31, 35, 40, 44, 49, 53, 58, 62, 67]
        #self.target = 62  # 选择靠后的数字，确保需要多次查找
            # 创建一个更长的有序数组，选择一个位于中间偏后的值作为目标
        self.numbers = [2, 5, 8, 13, 17, 22, 26, 31, 35, 39, 44, 48, 53, 57, 62, 66, 71, 75, 80, 85]
        self.target = 53  # 选
            # 创建标题
        self.title = Text("二分查找演示", font="SimSun", color=self.TEXT_COLOR).to_edge(UP, buff=0.3)
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
            
            # 如果当前数字等于目标值，则显示为红色
            number_color = RED if num == self.target else self.TEXT_COLOR
            number = Text(
                str(num), 
                font="SimSun", 
                font_size=24, 
                color=number_color
            ).move_to(square.get_center())
            self.numbers_text.add(number)
            
            index = Text(
                str(i), 
                font="SimSun", 
                font_size=20, 
                color=self.TEXT_COLOR
            ).next_to(square, DOWN, buff=0.2)
            self.index_text.add(index)
        
        self.array_group = VGroup(self.squares, self.numbers_text, self.index_text)
        self.array_group.move_to(ORIGIN + UP * 0.5)
        self.array_group.scale_to_fit_width(config.frame_width - 1)
        
        self.play(
            Create(self.squares),
            Write(self.numbers_text),
            Write(self.index_text)
        )
        
        self.target_text = VGroup(
            Text("查找目标值: ", font="SimSun", font_size=36, color=self.TEXT_COLOR),
            Text(str(self.target), font="SimSun", font_size=36, color=RED)
        ).arrange(RIGHT, buff=0.1).next_to(self.title, DOWN, buff=0.3)
        
        self.play(Write(self.target_text))
        
        # 创建指针，调整位置使它们不会完全重叠
        self.arrow_config = {
            "stroke_width": 4,
            "max_tip_length_to_length_ratio": 0.3,
            "max_stroke_width_to_length_ratio": 5,
            "tip_length": 0.2
        }
        
        def create_pointer(color, index, offset=0):
            return Arrow(
                start=DOWN * 0.4 + RIGHT * offset,
                end=UP * 0.4 + RIGHT * offset,
                color=color,
                **self.arrow_config
            ).next_to(self.squares[index], DOWN, buff=0.7)
        
        self.pointer_low = create_pointer(self.LOW_COLOR, 0, -0.15)
        self.pointer_high = create_pointer(self.HIGH_COLOR, -1, 0.15)
        self.pointer_mid = create_pointer(self.MID_COLOR, 0)
        
        # 创建标签文字，水平错开
        self.label_low = Text("low", font="SimSun", color=self.LOW_COLOR, font_size=24).next_to(self.pointer_low, DOWN, buff=0.1).shift(LEFT * 0.15)
        self.label_high = Text("high", font="SimSun", color=self.HIGH_COLOR, font_size=24).next_to(self.pointer_high, DOWN, buff=0.1).shift(RIGHT * 0.15)
        self.label_mid = Text("mid", font="SimSun", color=self.MID_COLOR, font_size=24).next_to(self.pointer_mid, DOWN, buff=0.1)
        
        self.play(
            Create(self.pointer_low),
            Create(self.pointer_high),
            Write(self.label_low),
            Write(self.label_high)
        )
        
        self.left, self.right = 0, len(self.numbers) - 1
        
        # 添加用于存储已检查和已跳过元素的标记
        self.scanned_marks = VGroup()  # 已扫描标记
        self.skipped_marks = VGroup()  # 已跳过标记
        
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
            
            # 创建已跳过标记（半透明背景）
            skipped = Square(
                side_length=self.square_size,
                stroke_width=0,
                fill_color=self.SKIPPED_COLOR,
                fill_opacity=0
            ).move_to(square.get_center())
            self.skipped_marks.add(skipped)

    def mark_scanned(self, index):
        """标记已扫描的元素"""
        return AnimationGroup(
            self.squares[index].animate.set_stroke(opacity=0.6),
            self.numbers_text[index].animate.set_opacity(0.6),
            self.index_text[index].animate.set_opacity(0.6),
            self.scanned_marks[index].animate.set_opacity(1),
            lag_ratio=0.1
        )

    def mark_skipped_range(self, start, end):
        """标记被跳过的范围"""
        animations = []
        for i in range(start, end + 1):
            animations.extend([
                self.squares[i].animate.set_stroke(opacity=0.3),
                self.numbers_text[i].animate.set_opacity(0.3),
                self.index_text[i].animate.set_opacity(0.3),
                self.skipped_marks[i].animate.set_fill_opacity(0.3)
            ])
        return animations

    def construct(self):
        while self.left <= self.right:
            mid = (self.left + self.right) // 2

            # 更新指针指向方块的颜色
            self.play(
                self.squares[self.left].animate.set_stroke(color=self.LOW_COLOR),
                self.squares[self.right].animate.set_stroke(color=self.HIGH_COLOR)
            )
            
            # 更新mid指针位置
            self.pointer_mid.next_to(self.squares[mid], DOWN, buff=0.7)
            self.label_mid.next_to(self.squares[mid], DOWN, buff=1.2)
            
            # 显示计算过程
            calc_text = Text(
                f"mid = (low + high) // 2 = ({self.left} + {self.right}) // 2 = {mid}", 
                font="SimSun", 
                font_size=32,
                color=self.TEXT_COLOR
            ).next_to(self.target_text, DOWN, buff=0.4)
            
            self.play(
                Create(self.pointer_mid),
                Write(self.label_mid),
                Write(calc_text)
            )
            
            # 高亮当前元素
            self.play(self.squares[mid].animate.set_stroke(color=self.MID_COLOR))
            
            comparison_text = self.create_comparison_text(
                f"list[{mid}]", 
                str(self.target),
                "==" if self.numbers[mid] == self.target else ("<" if self.numbers[mid] < self.target else ">")
            ).next_to(calc_text, DOWN, buff=2).shift(DOWN*1)
            
            self.play(Write(comparison_text))
            
            if self.numbers[mid] == self.target:
                reasoning = self.create_reasoning_text(
                    f"目标值位于索引 {mid}"
                ).next_to(comparison_text, DOWN, buff=0.3)
                
                self.play(Write(reasoning))
                break
                
            elif self.numbers[mid] < self.target:
                reasoning = self.create_reasoning_text(
                    f"更新 low = mid + 1 = {mid + 1}"
                ).next_to(comparison_text, DOWN, buff=0.3)
                
                self.play(Write(reasoning))
                
                # 标记当前检查的元素为已扫描
                self.play(self.mark_scanned(mid))
                
                # 标记左半部分为已跳过
                exclude_animations = self.mark_skipped_range(self.left, mid-1)
                self.play(*exclude_animations)
                
                self.left = mid + 1
                self.play(
                    AnimationGroup(
                        self.pointer_low.animate.next_to(self.squares[self.left], DOWN, buff=0.7).shift(LEFT * 0.2 + DOWN * 0.3),
                        self.label_low.animate.next_to(self.squares[self.left], DOWN, buff=1.2).shift(LEFT * 0.2 + DOWN * 0.3),
                        FadeOut(calc_text),
                        FadeOut(comparison_text),
                        FadeOut(reasoning),
                        lag_ratio=0.1
                    )
                )
                
            else:
                reasoning = self.create_reasoning_text(
                    f"更新 high = mid - 1 = {mid - 1}"
                ).next_to(comparison_text, DOWN, buff=0.3)
                
                self.play(Write(reasoning))
                
                # 标记当前检查的元素为已扫描
                self.play(self.mark_scanned(mid))
                
                # 标记右半部分为已跳过
                exclude_animations = self.mark_skipped_range(mid+1, self.right)
                self.play(*exclude_animations)
                
                self.right = mid - 1
                self.play(
                    AnimationGroup(
                        self.pointer_high.animate.next_to(self.squares[self.right], DOWN, buff=0.7).shift(RIGHT * 0.2 + UP * 0.3),
                        self.label_high.animate.next_to(self.squares[self.right], DOWN, buff=1.2).shift(RIGHT * 0.2 + UP * 0.3),
                        FadeOut(calc_text),
                        FadeOut(comparison_text),
                        FadeOut(reasoning),
                        lag_ratio=0.1
                    )
                )
            
            self.play(
                FadeOut(self.pointer_mid),
                FadeOut(self.label_mid)
            )

        self.wait(2)

if __name__ == "__main__":
    config.pixel_height = 2160
    config.pixel_width = 3840
    config.frame_rate = 30
    
    with tempconfig({"quality": "production_quality", "preview": True}):
        scene = BinarySearchAnimation()
        scene.render()

