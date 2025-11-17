from manim import *
import numpy as np

class ListCopyAnimation(Scene):
    """列表深浅拷贝3D动画 - 引用、浅拷贝、深拷贝对比"""
    def __init__(self):
        super().__init__()
        self.camera.background_color = "#FFFFFF"

        # 颜色方案
        self.TEXT_COLOR = "#000000"
        self.REF_COLOR = "#E74C3C"  # 引用赋值 - 红色
        self.SHALLOW_COLOR = "#3498DB"  # 浅拷贝 - 蓝色
        self.DEEP_COLOR = "#2ECC71"  # 深拷贝 - 绿色
        self.NESTED_COLOR = "#9B59B6"  # 嵌套对象 - 紫色
        self.CODE_COLOR = "#E67E22"  # 代码 - 橙色
        self.ARROW_COLOR = "#34495E"  # 箭头 - 深灰

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

    def create_3d_box(self, text, color, position, width=1.2, height=0.8, depth=0.3):
        """创建伪3D方框"""
        # 前面板
        front_rect = Rectangle(
            width=width,
            height=height,
            stroke_color=color,
            stroke_width=3,
            fill_color=color,
            fill_opacity=0.1
        )

        # 右侧面（伪3D效果）
        right_points = [
            front_rect.get_corner(UR),
            front_rect.get_corner(UR) + np.array([depth*0.5, depth*0.3, 0]),
            front_rect.get_corner(DR) + np.array([depth*0.5, depth*0.3, 0]),
            front_rect.get_corner(DR)
        ]
        right_face = Polygon(
            *right_points,
            stroke_color=color,
            stroke_width=2,
            fill_color=color,
            fill_opacity=0.2
        )

        # 上面（伪3D效果）
        top_points = [
            front_rect.get_corner(UL),
            front_rect.get_corner(UL) + np.array([depth*0.5, depth*0.3, 0]),
            front_rect.get_corner(UR) + np.array([depth*0.5, depth*0.3, 0]),
            front_rect.get_corner(UR)
        ]
        top_face = Polygon(
            *top_points,
            stroke_color=color,
            stroke_width=2,
            fill_color=color,
            fill_opacity=0.3
        )

        # 文字
        text_obj = Text(
            text,
            font=self.CHINESE_FONT,
            color=self.TEXT_COLOR,
            font_size=24
        ).move_to(front_rect.get_center())

        box_group = VGroup(right_face, top_face, front_rect, text_obj)
        box_group.move_to(position)

        return box_group, front_rect

    def create_nested_3d_box(self, outer_text, inner_list, color, position):
        """创建包含嵌套列表的3D方框"""
        # 外层大框
        outer_box, outer_rect = self.create_3d_box(
            outer_text,
            color,
            position,
            width=3.5,
            height=1.5,
            depth=0.4
        )

        # 内层嵌套列表（小框）
        inner_boxes = VGroup()
        inner_rects = []

        # 在外框内部创建三个小框
        inner_y = position[1]
        spacing = 1.0

        for i, text in enumerate(inner_list):
            inner_pos = position + np.array([
                -1.2 + i * spacing,
                -0.2,
                0
            ])

            if text == "nested":
                # 嵌套列表用特殊颜色
                inner_box, inner_rect = self.create_3d_box(
                    "[2, 3]",
                    self.NESTED_COLOR,
                    inner_pos,
                    width=0.8,
                    height=0.5,
                    depth=0.25
                )
            else:
                inner_box, inner_rect = self.create_3d_box(
                    str(text),
                    color,
                    inner_pos,
                    width=0.6,
                    height=0.5,
                    depth=0.2
                )

            inner_boxes.add(inner_box)
            inner_rects.append(inner_rect)

        # 移除外层文字，只保留框架
        outer_box.remove(outer_box[-1])  # 移除文字

        full_group = VGroup(outer_box, inner_boxes)

        return full_group, outer_rect, inner_rects

    def construct(self):
        # 标题
        title = Text(
            "Python 列表复制：引用 vs 浅拷贝 vs 深拷贝",
            font=self.CHINESE_FONT,
            color=self.TEXT_COLOR,
            font_size=40
        )
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.5)

        # ====== 场景1：引用赋值（=） ======
        subtitle1 = Text(
            "方式1：引用赋值 (=)",
            font=self.CHINESE_FONT,
            color=self.REF_COLOR,
            font_size=32
        )
        subtitle1.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle1))

        # 代码
        code1 = VGroup(
            Text("list1 = [1, [2, 3], 4]", font="Courier New", color=self.TEXT_COLOR, font_size=24),
            Text("list2 = list1", font="Courier New", color=self.REF_COLOR, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        code1.next_to(subtitle1, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        self.play(Write(code1))
        self.wait(0.8)

        # 创建list1
        list1_data = [1, "nested", 4]
        list1_group, list1_rect, list1_inner = self.create_nested_3d_box(
            "list1",
            list1_data,
            self.REF_COLOR,
            ORIGIN + UP * 0.5
        )

        var_label1 = Text(
            "list1",
            font="Courier New",
            color=self.REF_COLOR,
            font_size=26
        ).next_to(list1_rect, UP, buff=0.4)

        self.play(
            Write(var_label1),
            Create(list1_group),
            run_time=2
        )
        self.wait(1)

        # 创建list2标签（指向同一对象）
        var_label2 = Text(
            "list2",
            font="Courier New",
            color=self.REF_COLOR,
            font_size=26
        ).next_to(list1_rect, DOWN, buff=0.8)

        # 箭头表示引用
        arrow1 = Arrow(
            var_label1.get_bottom() + DOWN * 0.1,
            list1_rect.get_top(),
            color=self.ARROW_COLOR,
            stroke_width=3,
            buff=0.1
        )

        arrow2 = Arrow(
            var_label2.get_top() + UP * 0.1,
            list1_rect.get_bottom(),
            color=self.ARROW_COLOR,
            stroke_width=3,
            buff=0.1
        )

        self.play(
            Create(arrow1),
            Write(var_label2),
            Create(arrow2),
            run_time=1.5
        )
        self.wait(0.8)

        # 说明
        explanation1 = Text(
            "⚠️ list1 和 list2 指向同一个内存地址\n修改任意一个，另一个也会改变",
            font=self.CHINESE_FONT,
            color=self.REF_COLOR,
            font_size=22,
            line_spacing=1.3
        )
        explanation1.next_to(list1_group, DOWN, buff=1.8)
        self.play(Write(explanation1))
        self.wait(2)

        # 清除场景1
        self.play(
            FadeOut(subtitle1),
            FadeOut(code1),
            FadeOut(var_label1),
            FadeOut(var_label2),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(list1_group),
            FadeOut(explanation1)
        )

        # ====== 场景2：浅拷贝（.copy()） ======
        subtitle2 = Text(
            "方式2：浅拷贝 (.copy())",
            font=self.CHINESE_FONT,
            color=self.SHALLOW_COLOR,
            font_size=32
        )
        subtitle2.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle2))

        # 代码
        code2 = VGroup(
            Text("list1 = [1, [2, 3], 4]", font="Courier New", color=self.TEXT_COLOR, font_size=24),
            Text("list2 = list1.copy()", font="Courier New", color=self.SHALLOW_COLOR, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        code2.next_to(subtitle2, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        self.play(Write(code2))
        self.wait(0.8)

        # 创建list1
        list2_data = [1, "nested", 4]
        list2_group, list2_rect, list2_inner = self.create_nested_3d_box(
            "list1",
            list2_data,
            self.SHALLOW_COLOR,
            LEFT * 2.5 + UP * 0.3
        )

        var_label3 = Text(
            "list1",
            font="Courier New",
            color=self.SHALLOW_COLOR,
            font_size=26
        ).next_to(list2_rect, LEFT, buff=0.5)

        self.play(
            Write(var_label3),
            Create(list2_group),
            run_time=2
        )
        self.wait(0.8)

        # 创建list2（浅拷贝）
        list3_data = [1, "nested", 4]
        list3_group, list3_rect, list3_inner = self.create_nested_3d_box(
            "list2",
            list3_data,
            self.SHALLOW_COLOR,
            RIGHT * 2.5 + UP * 0.3
        )

        var_label4 = Text(
            "list2",
            font="Courier New",
            color=self.SHALLOW_COLOR,
            font_size=26
        ).next_to(list3_rect, RIGHT, buff=0.5)

        self.play(
            TransformFromCopy(list2_group, list3_group),
            Write(var_label4),
            run_time=2
        )
        self.wait(0.8)

        # 关键：嵌套对象仍然共享
        # 在两个嵌套列表之间画双向箭头
        nested_arrow = DoubleArrow(
            list2_inner[1].get_right(),
            list3_inner[1].get_left(),
            color=self.NESTED_COLOR,
            stroke_width=4,
            buff=0.1
        )

        shared_label = Text(
            "共享引用",
            font=self.CHINESE_FONT,
            color=self.NESTED_COLOR,
            font_size=20
        ).next_to(nested_arrow, UP, buff=0.1)

        self.play(
            Create(nested_arrow),
            Write(shared_label)
        )
        self.wait(1)

        # 说明
        explanation2 = VGroup(
            Text("✅ 外层列表是独立的（不同对象）", font=self.CHINESE_FONT, color=self.SHALLOW_COLOR, font_size=22),
            Text("❌ 嵌套列表仍然共享（同一对象）", font=self.CHINESE_FONT, color=self.NESTED_COLOR, font_size=22),
            Text("", font=self.CHINESE_FONT, font_size=10),
            Text("修改 list2[0] = 99  →  list1[0] 不变 ✅", font="Courier New", color=self.SHALLOW_COLOR, font_size=20),
            Text("修改 list2[1][0] = 99  →  list1[1][0] 也变 ❌", font="Courier New", color=self.NESTED_COLOR, font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        explanation2.next_to(list2_group, DOWN, buff=1.5).shift(RIGHT * 1.2)
        self.play(Write(explanation2))
        self.wait(3)

        # 清除场景2
        self.play(
            FadeOut(subtitle2),
            FadeOut(code2),
            FadeOut(var_label3),
            FadeOut(var_label4),
            FadeOut(list2_group),
            FadeOut(list3_group),
            FadeOut(nested_arrow),
            FadeOut(shared_label),
            FadeOut(explanation2)
        )

        # ====== 场景3：深拷贝（deepcopy()） ======
        subtitle3 = Text(
            "方式3：深拷贝 (copy.deepcopy())",
            font=self.CHINESE_FONT,
            color=self.DEEP_COLOR,
            font_size=32
        )
        subtitle3.next_to(title, DOWN, buff=0.6)
        self.play(Write(subtitle3))

        # 代码
        code3 = VGroup(
            Text("import copy", font="Courier New", color=self.TEXT_COLOR, font_size=24),
            Text("list1 = [1, [2, 3], 4]", font="Courier New", color=self.TEXT_COLOR, font_size=24),
            Text("list2 = copy.deepcopy(list1)", font="Courier New", color=self.DEEP_COLOR, font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        code3.next_to(subtitle3, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        self.play(Write(code3))
        self.wait(0.8)

        # 创建list1
        list4_data = [1, "nested", 4]
        list4_group, list4_rect, list4_inner = self.create_nested_3d_box(
            "list1",
            list4_data,
            self.DEEP_COLOR,
            LEFT * 2.5 + UP * 0.3
        )

        var_label5 = Text(
            "list1",
            font="Courier New",
            color=self.DEEP_COLOR,
            font_size=26
        ).next_to(list4_rect, LEFT, buff=0.5)

        self.play(
            Write(var_label5),
            Create(list4_group),
            run_time=2
        )
        self.wait(0.8)

        # 创建list2（深拷贝 - 包括嵌套对象也是新的）
        list5_data = [1, "nested", 4]
        list5_group, list5_rect, list5_inner = self.create_nested_3d_box(
            "list2",
            list5_data,
            "#27AE60",  # 稍微不同的绿色表示完全独立
            RIGHT * 2.5 + UP * 0.3
        )

        var_label6 = Text(
            "list2",
            font="Courier New",
            color=self.DEEP_COLOR,
            font_size=26
        ).next_to(list5_rect, RIGHT, buff=0.5)

        self.play(
            TransformFromCopy(list4_group, list5_group),
            Write(var_label6),
            run_time=2
        )
        self.wait(0.8)

        # 标注完全独立
        independent_label1 = Text(
            "完全独立",
            font=self.CHINESE_FONT,
            color=self.DEEP_COLOR,
            font_size=22
        ).next_to(list4_group, DOWN, buff=0.4)

        independent_label2 = Text(
            "完全独立",
            font=self.CHINESE_FONT,
            color=self.DEEP_COLOR,
            font_size=22
        ).next_to(list5_group, DOWN, buff=0.4)

        # X标记表示不共享
        cross_line1 = Line(
            list4_inner[1].get_right(),
            list5_inner[1].get_left(),
            color=self.DEEP_COLOR,
            stroke_width=2
        )

        cross_line2 = Line(
            list4_inner[1].get_right() + UP * 0.3,
            list5_inner[1].get_left() + DOWN * 0.3,
            color=self.DEEP_COLOR,
            stroke_width=2
        )

        no_share_label = Text(
            "不共享",
            font=self.CHINESE_FONT,
            color=self.DEEP_COLOR,
            font_size=20
        ).move_to((list4_inner[1].get_right() + list5_inner[1].get_left()) / 2 + UP * 0.5)

        self.play(
            Write(independent_label1),
            Write(independent_label2),
            Create(cross_line1),
            Create(cross_line2),
            Write(no_share_label)
        )
        self.wait(1)

        # 说明
        explanation3 = VGroup(
            Text("✅ 所有层级都完全独立", font=self.CHINESE_FONT, color=self.DEEP_COLOR, font_size=24),
            Text("✅ 嵌套对象也被递归复制", font=self.CHINESE_FONT, color=self.DEEP_COLOR, font_size=24),
            Text("", font=self.CHINESE_FONT, font_size=10),
            Text("修改 list2 的任何元素都不会影响 list1 ✅", font=self.CHINESE_FONT, color=self.DEEP_COLOR, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        explanation3.next_to(independent_label1, DOWN, buff=0.8).shift(RIGHT * 1.2)
        self.play(Write(explanation3))
        self.wait(3)

        # 清除场景3
        self.play(
            FadeOut(subtitle3),
            FadeOut(code3),
            FadeOut(var_label5),
            FadeOut(var_label6),
            FadeOut(list4_group),
            FadeOut(list5_group),
            FadeOut(independent_label1),
            FadeOut(independent_label2),
            FadeOut(cross_line1),
            FadeOut(cross_line2),
            FadeOut(no_share_label),
            FadeOut(explanation3)
        )

        # ====== 总结对比 ======
        summary_title = Text(
            "三种方式对比总结",
            font=self.CHINESE_FONT,
            color=self.CODE_COLOR,
            font_size=36
        )
        summary_title.next_to(title, DOWN, buff=0.6)
        self.play(Write(summary_title))

        summary_table = VGroup(
            # 第1行：引用赋值
            VGroup(
                Text("list2 = list1", font="Courier New", color=self.REF_COLOR, font_size=26),
                Text("→", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=26),
                Text("同一对象，完全共享", font=self.CHINESE_FONT, color=self.REF_COLOR, font_size=24)
            ).arrange(RIGHT, buff=0.4),

            Text("", font=self.CHINESE_FONT, font_size=12),

            # 第2行：浅拷贝
            VGroup(
                Text("list2 = list1.copy()", font="Courier New", color=self.SHALLOW_COLOR, font_size=26),
                Text("→", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=26),
                Text("外层独立，嵌套共享", font=self.CHINESE_FONT, color=self.SHALLOW_COLOR, font_size=24)
            ).arrange(RIGHT, buff=0.4),

            Text("", font=self.CHINESE_FONT, font_size=12),

            # 第3行：深拷贝
            VGroup(
                Text("list2 = copy.deepcopy(list1)", font="Courier New", color=self.DEEP_COLOR, font_size=26),
                Text("→", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=26),
                Text("完全独立，递归复制", font=self.CHINESE_FONT, color=self.DEEP_COLOR, font_size=24)
            ).arrange(RIGHT, buff=0.4),

            Text("", font=self.CHINESE_FONT, font_size=16),

            # 使用建议
            Text("💡 使用建议", font=self.CHINESE_FONT, color=self.CODE_COLOR, font_size=28),
            Text("• 简单列表（无嵌套）：使用 .copy()", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=22),
            Text("• 嵌套列表：使用 copy.deepcopy()", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=22),
            Text("• 需要共享引用：使用 = 赋值", font=self.CHINESE_FONT, color=self.TEXT_COLOR, font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        summary_table.next_to(summary_title, DOWN, buff=0.5)

        self.play(Write(summary_table), run_time=5)
        self.wait(4)

        # 结束
        self.play(
            FadeOut(summary_title),
            FadeOut(summary_table),
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
