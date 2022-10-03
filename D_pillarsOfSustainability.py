from tkinter import BOTTOM
from manim import *
from manim_editor import PresentationSectionType
from utils import createDevoteamLogo

class D_PillarsOfSustainability(Scene):
    def construct(self):
        devoteamLogo = createDevoteamLogo()
        ellipse1 = Ellipse(
            width=4.0, height=4.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT*5+UP)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to( UP+LEFT*2)
        ellipse3 = ellipse1.copy().set_color(color=GREEN).move_to(LEFT*3.5+ DOWN*1.5)

        title_text = Title("Pillars of sustainability").move_to(UP*3.5)

        text_font_size=20
        economic_text = Tex("Economic Viability",font_size=text_font_size).move_to(ellipse1.get_center())
        social_text = Tex("Social Equity",font_size=text_font_size).move_to(ellipse2.get_center())
        environmental_text = Tex("Environmental Protection",font_size=text_font_size).move_to(ellipse3.get_center())

        economic_group = Group(ellipse1,economic_text)
        social_group = Group(ellipse2,social_text)
        environmental_group = Group(ellipse3,environmental_text)


        self.next_section("Sustainability",PresentationSectionType.NORMAL)
        text = Tex("What should we then optimize \\underline{for}?",font_size=30)
        self.play(FadeIn(title_text,devoteamLogo,text))

        self.next_section("Sustainability.1",PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(text),FadeIn(economic_group))

        self.next_section("Sustainability.2",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(social_group))

        self.next_section("Sustainability.3",PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(environmental_group),FadeOut(devoteamLogo))

        self.next_section("Sustainability.7",PresentationSectionType.SUB_NORMAL)
        ramosEtAl = Tex("\"...the three dimensions of sustainability\n - economic, environmental and social - \nneed to be considered when addressing sustainable systems\" \n(Elkington 1997,  Ramos et al. 2014)",font_size=text_font_size).move_to(RIGHT *3 + DOWN*2)
        self.play(FadeIn(ramosEtAl))
        i_4 = Intersection(ellipse1, ellipse2,ellipse3, color=WHITE, fill_opacity=0.5)
        self.play(FadeIn(i_4))

        self.next_section("Sustainability.8",PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(i_4))
        self.play(
            ellipse1.animate.scale(0.1),
            ellipse2.animate.scale(0.1),
            ellipse3.animate.scale(0.1,),
            economic_text.animate.move_to(LEFT*3.5 +UP),
            social_text.animate.move_to(LEFT*3.3+DOWN),
            environmental_text.animate.move_to(LEFT*4),
            FadeOut(ramosEtAl)
        )
        self.play(ellipse1.animate.move_to(LEFT*2+UP),
                    ellipse2.animate.move_to(LEFT*2+DOWN),
                    ellipse3.animate.move_to(LEFT*2),
                    FadeIn(devoteamLogo)     
                    )
        self.next_section("Sustainability.9",PresentationSectionType.SUB_NORMAL)
        economic_text2 = Tex("Estimation of income? Amount of deliveries? Distance?",font_size=20).next_to(ellipse1.get_right())
        self.play(FadeIn(economic_text2))
        self.next_section("Sustainability.10",PresentationSectionType.SUB_NORMAL)
        environmental_text2 = Tex("Fuel consumption? Pollution?",font_size=20).next_to(ellipse3.get_right())
        self.play(FadeIn(environmental_text2))
        self.next_section("Sustainability.11",PresentationSectionType.SUB_NORMAL)
        social_text2 = Tex("?",font_size=20).next_to(ellipse2.get_right())
        self.play(FadeIn(social_text2))