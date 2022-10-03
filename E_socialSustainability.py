from tkinter import BOTTOM
from manim import *
from manim_editor import PresentationSectionType
from utils import createDevoteamLogo

class E_SocialSustainability(Scene):
    def construct(self):
        title = Title("Social Sustainability")
        mogdhani = Tex('\\textit{“...most of GVRPs model just consider the environmental and economical aspect of routing problem, and social factors are mostly overlooked in the literature.”} - (Moghdani et al. 2021)',font_size=30)
        self.next_section("SocialSustainability",PresentationSectionType.NORMAL)
        self.play(FadeIn(title,mogdhani,createDevoteamLogo()))


        chart = BarChart(
            values=[7, 4, 3, 8],
            bar_names=["Alice", "Bob", "Clara", "David"],
            y_range=[0, 10, 2],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36}
        ).scale(0.7)
        y_label = chart.get_y_axis_label("Work time (Hours)").scale(0.6).move_to(chart.get_left()+LEFT*.3).rotate(PI/2)
        c_bar_lbls = chart.get_bar_labels(font_size=48)


        self.next_section("SocialSustainability.0",PresentationSectionType.SUB_NORMAL)
        bulletList = BulletedList("8 hour workday","Equal work distribution",font_size=32)
        self.play(FadeOut(mogdhani),FadeIn(bulletList))
        self.next_section("SocialSustainability.0.5",PresentationSectionType.SUB_NORMAL)
        whyDoWeNeedIt = Tex("Why do we need to care?",font_size=32)
        self.play(FadeOut(bulletList),FadeIn(whyDoWeNeedIt))
        self.next_section("SocialSustainability.1",PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(whyDoWeNeedIt),FadeIn(chart, c_bar_lbls,y_label))
        self.next_section("SocialSustainability.2",PresentationSectionType.SUB_NORMAL)
        chart2 = chart.copy()
        chart2.change_bar_values([7,7.5,10,8])
        self.play(Transform(chart,chart2),Transform(c_bar_lbls,chart2.get_bar_labels(font_size=48)))
        self.next_section("SocialSustainability.2",PresentationSectionType.SUB_NORMAL)
        chart3 = chart2.copy()
        chart3.change_bar_values([7,7.5,7,8])
        self.play(Transform(chart,chart3),Transform(c_bar_lbls,chart3.get_bar_labels(font_size=48)))