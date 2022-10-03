from math import pi
from multiprocessing.connection import wait
from numpy import*
from manim import *
from manim_editor import PresentationSectionType
import pandas as pd 
from utils import createDevoteamLogo



def secondSlide(self):
    slide_title = Title("Outline")
    blist = BulletedList("Vehicle routing problem","Introduction to optimization","Sustainability within VRP","Solving the problem","Industrial applications", height=5, width=5)
    self.add(createDevoteamLogo())
    self.play(FadeIn(slide_title),FadeIn(blist))


def motivationSlide(self):
    title = Title("Who am I and why am I having this presentation?")
    text1 = Tex("Andreas Häggström, Halmstad Office",font_size=24).move_to(UP*2.5)
    self.add(createDevoteamLogo())
    self.play(FadeIn(title,text1))

    self.next_section("Motivation.1",PresentationSectionType.SUB_NORMAL)
    mastersThesisImg = ImageMobject("./premadeImages/masterThesis.png").scale(0.7).move_to(DOWN*1)
    self.play(FadeIn(mastersThesisImg))

    self.next_section("Motivation.2",PresentationSectionType.SUB_NORMAL)
    swedenImg = ImageMobject("./premadeImages/sweden.png").scale(0.8).move_to(DOWN*0.6)
    self.play(FadeOut(mastersThesisImg,text1),FadeIn(swedenImg))

    self.next_section("Motivation.3",PresentationSectionType.SUB_NORMAL)
    ukImg = ImageMobject("./premadeImages/london_75_before.png").move_to(DOWN*.2)
    self.play(FadeOut(swedenImg),FadeIn(ukImg))

class A_OptimizationPresentation(ThreeDScene):
    def construct(self):
        title = Title('"Good enough!"')
        subtitle = Tex("An introduction to optimization, vehicle routing and its sustainability aspects",font_size=24)

        self.next_section("Title",PresentationSectionType.NORMAL)
        self.play(FadeIn(title,createDevoteamLogo()))

        self.next_section("Subtitle",PresentationSectionType.NORMAL)
        self.play(FadeIn(subtitle))

        self.next_section("Outline",PresentationSectionType.NORMAL)
        self.clear()
        secondSlide(self)
        
        self.next_section("Motivation",PresentationSectionType.NORMAL)
        self.clear()
        motivationSlide(self)

    
