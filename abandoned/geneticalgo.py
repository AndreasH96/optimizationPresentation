
from numpy import*
from manim import *
from manim_editor import PresentationSectionType
from utils import createDevoteamLogo
import pandas as pd 
import numpy as np 


def create_textbox(color, string):
    result = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        height=1, width=1, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Text(string).move_to(box.get_center()) # create text
    result.add(box, text) # add both objects to the VGroup
    return result

class GeneticAlgorithm(ThreeDScene):
    def construct(self):
        title = Title("Optimization Solver Example: Genetic Algorithm")
        self.next_section("Title",PresentationSectionType.NORMAL)
        self.add(title,createDevoteamLogo())
        parent1 = Tex("{1,2,3,4}",font_size=24).move_to(LEFT*2)
        parent2 = Tex("{8,5,9,3}",font_size=24).move_to(RIGHT*2)
         # create text box
        parent1 = [
            create_textbox(color=BLUE, string="2").move_to(LEFT*5+UP*2),
            create_textbox(color=BLUE, string="4").move_to(LEFT*4+UP*2),
            create_textbox(color=BLUE, string="1").move_to(LEFT*3+UP*2),
            create_textbox(color=BLUE, string="3").move_to(LEFT*2+UP*2)]

        self.play(FadeIn(*parent1))

        # move text box around
        #self.play(textbox.animate.shift(2*RIGHT), run_time=3)
        #self.play(textbox.animate.shift(2*UP), run_time=3)
        self.wait()

        #child = 