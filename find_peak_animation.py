from manim import *

class PeakFindingScene(Scene):
    def construct(self):
        # Corner cases - 展示二分查找过程中的特殊指针位置关系
        cases = [
            # Case 1: [L=peak-1, R=peak+1] 左右指针分别在峰值的左右相邻位置
            ([3, 4, 9, 6, 4], 2, "Corner Case 1: L=peak-1, R=peak+1"),
            
            # Case 2: [L=peak, R=peak+2] 左指针在峰值，右指针在峰值后两位
            ([3, 9, 6, 4, 2], 1, "Corner Case 2: L=peak, R=peak+2"),
            
            # Case 3: [L=peak-2, R=peak] 左指针在峰值前两位，右指针在峰值
            ([3, 4, 9, 6, 4], 2, "Corner Case 3: L=peak-2, R=peak"),
            
            # Case 4: [L=0, R=2] 左边界情况
            ([9, 6, 4, 2, 1], 0, "Corner Case 4: L=L_boundary, R=L_boundary+2"),
            
            # Case 5: [L=n-3, R=n-1] 右边界情况
            ([1, 4, 9], 2, "Corner Case 5: L=R_boundary-2, R=R_boundary")
        ]

        for case_idx, (arr, peak, description) in enumerate(cases):
            # 创建数组可视化
            dots, lines, numbers, indices = self.create_array_visualization(arr)
            
            # 显示标题和描述
            title = Text(f"Corner Case {case_idx + 1}", font_size=36).to_edge(UP)
            desc = Text(description, font_size=24).next_to(title, DOWN, buff=0.5)
            
            # 创建信息显示区域（右侧）
            info_group = VGroup()
            info_group.to_edge(RIGHT).shift(UP * 2)
            
            self.play(
                Write(title),
                Write(desc),
                *[Create(dot) for dot in dots],
                *[Create(line) for line in lines],
                *[Write(num) for num in numbers],
                *[Write(idx) for idx in indices]
            )
            self.wait(1)

            # 直接展示特定的指针位置
            if case_idx == 0:  # L=peak-1, R=peak+1
                left, right = peak-1, peak+1
            elif case_idx == 1:  # L=peak, R=peak+2
                left, right = peak, peak+2
            elif case_idx == 2:  # L=peak-2, R=peak
                left, right = peak-2, peak
            elif case_idx == 3:  # L=0, R=2
                left, right = 0, 2
            else:  # L=n-3, R=n-1
                left, right = len(arr)-3, len(arr)-1

            # 显示初始指针位置
            pointers = self.show_pointers(dots, left, (left + right) // 2, right)
            
            # 显示关键信息
            key_info = VGroup(
                Text(f"Initial L={left}, R={right}", font_size=24),
                Text(f"Peak at index {peak}", font_size=24),
                Text(f"arr[peak]={arr[peak]}", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT)
            key_info.next_to(info_group, DOWN, buff=0.5)
            
            self.play(Write(key_info))
            self.wait(1)

            # 展示一次迭代后的结果
            mid = (left + right) // 2
            next_info = VGroup(
                Text(f"mid = ({left} + {right}) // 2 = {mid}", font_size=24),
                Text(f"Compare: arr[{mid}]={arr[mid]}", font_size=24)
            ).arrange(DOWN, aligned_edge=LEFT)
            next_info.next_to(key_info, DOWN, buff=0.5)
            
            self.play(Write(next_info))
            self.wait(1)

            # 高亮显示峰值
            peak_highlight = dots[peak].copy().set_color(GREEN)
            self.play(Transform(dots[peak], peak_highlight))
            self.wait(1)

            # 清除场景
            self.play(*[FadeOut(mob) for mob in self.mobjects])
            self.wait(0.5)

    def show_pointers(self, dots, left, mid, right):
        pointers = []
        # Left pointer
        left_arrow = Arrow(start=DOWN, end=UP, color=BLUE).next_to(dots[left], DOWN)
        left_text = Text("L", color=BLUE).next_to(left_arrow, DOWN)
        pointers.extend([left_arrow, left_text])
        
        # Mid pointer
        mid_arrow = Arrow(start=DOWN, end=UP, color=YELLOW).next_to(dots[mid], DOWN)
        mid_text = Text("M", color=YELLOW).next_to(mid_arrow, DOWN)
        pointers.extend([mid_arrow, mid_text])
        
        # Right pointer
        right_arrow = Arrow(start=DOWN, end=UP, color=RED).next_to(dots[right], DOWN)
        right_text = Text("R", color=RED).next_to(right_arrow, DOWN)
        pointers.extend([right_arrow, right_text])

        self.play(*[Create(p) for p in pointers])
        return pointers

    def create_array_visualization(self, arr):
        dots = []
        lines = []
        numbers = []
        indices = []
        
        # 创建点和连线
        for i, val in enumerate(arr):
            # 创建点
            dot = Dot(point=np.array([i - len(arr)/2, val/2, 0]))
            dots.append(dot)
            
            # 创建数字标签（值）
            number = Text(str(val), font_size=24).next_to(dot, UP, buff=0.3)
            numbers.append(number)
            
            # 创建索引标签
            index = Text(str(i), font_size=20, color=GRAY).next_to(dot, DOWN, buff=0.3)
            indices.append(index)
            
            # 创建连线
            if i > 0:
                line = Line(dots[i-1].get_center(), dot.get_center())
                lines.append(line)
        
        return dots, lines, numbers, indices

def main():
    config.media_width = "1920"
    config.media_height = "1080"
    config.video_dir = "./videos"
    config.output_file = "peak_finding_boundary_cases"
    
    scene = PeakFindingScene()
    scene.render()

if __name__ == "__main__":
    main() 