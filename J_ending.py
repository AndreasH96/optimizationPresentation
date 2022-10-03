from tkinter import BOTTOM
from manim import *
from manim_editor import PresentationSectionType
from utils import createDevoteamLogo



class J_Ending(Scene):
    def construct(self):
        title = Title("Obvious discussions to have")
        blist = BulletedList("Electric vehicles","Autonomous vehicles",font_size=30)
        self.play(FadeIn(title,blist,createDevoteamLogo()))
        self.next_section("Final section",PresentationSectionType.NORMAL)
        title2 = Title("Thank you for listening!")
        text = Tex("Contact: andreas.haggstrom@devoteam.com or at Slack",font_size=30)
        self.play(Transform(title,title2),FadeOut(blist),FadeIn(text))