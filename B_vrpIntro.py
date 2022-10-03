
import math
from tkinter import font
from numpy import*
from manim import *
from manim_editor import PresentationSectionType
from utils import createDevoteamLogo
import pandas as pd 
import numpy as np 


def basicVRPGraph(self):
    path = VMobject()
    start_pos = [3,1,0]
    font_size=18
    start_point = Dot(point=start_pos,color=GREEN)
    start_label = Text("Start",font_size=font_size).move_to(start_point.get_right() + RIGHT * .4)

    pen = Dot(point=start_pos,color=RED)

    points = [[4.1,0,0],[4,-.5,0],[4.5,-1,0]]
    dots = [Dot(point=p) for p in points]

    path.set_points_as_corners([pen.get_center(), pen.get_center()])

    def update_path(path):
        previous_path = path.copy()
        previous_path.add_points_as_corners([pen.get_center()])
        path.become(previous_path)

    path.add_updater(update_path)
    self.next_section("vrpgraph.1",PresentationSectionType.SUB_NORMAL)
    self.play(FadeIn(path, pen,start_point,start_label))
    labels = [Text("A",font_size=font_size),Text("B",font_size=font_size),Text("C",font_size=font_size)]
    [l.move_to(d.get_right()+RIGHT*.2) for l,d in zip(labels,dots)]  
    self.play(FadeIn(*dots,*labels))
    self.next_section("vrpgraph.2",PresentationSectionType.SUB_NORMAL)
    for dot in dots:
        self.play(pen.animate.move_to(dot.get_center()))
        self.wait(1)

    new_points_1 = [[4.8,1.2,0],[4.5,1.8,0],[4.1,2,0],[4.3,-1,0],[4.6,-0.5,0],[3.6,.2,0],[3.9,0.5,0],[3,1.5,0],[3.2,-1,0],[3.59,-0.5,0]]
    new_dots_1 =  [Dot(point=p) for p in new_points_1]
    self.next_section("vrpgraph.3",PresentationSectionType.SUB_NORMAL)
    self.play(FadeIn(*new_dots_1))
    self.next_section("simpleVrpGraphHold",PresentationSectionType.SUB_NORMAL)
    self.play(FadeOut(*new_dots_1,path,pen,start_point,start_label,*dots,*labels))

def barchartSlide(self):
    data = pd.read_csv("./emission_data.csv")
    title = Title("CO2 emissions from trucks in Sweden")
    self.add(createDevoteamLogo())
    self.play(FadeIn(title))
    chart = BarChart(
            values=  np.round(data["Lätta lastbilar"] + data["Tunga lastbilar"],2),
            bar_names=data.get("Year"),
            y_range=[0, 7, 1],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 24}
        
        ).scale(0.7)
    y_label = chart.get_y_axis_label("CO2 (Megaton) ").scale(0.6).move_to(chart.get_left()+LEFT*.3).rotate(PI/2)
    c_bar_lbls = chart.get_bar_labels(font_size=24)
    self.play(FadeIn(chart,c_bar_lbls,y_label))
    self.next_section("barchartHold.1",PresentationSectionType.SUB_NORMAL)
    chart2 = BarChart(
            values=  np.round(((data["Lätta lastbilar"] + data["Tunga lastbilar"])/data["Totalt"])*100,1),
            bar_names=data.get("Year"),
            y_range=[0, 50, 5],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 24}
        ).scale(0.7)
    title2 = Title("CO2\% of Swedish traffic from trucks ")
    y_label2 = chart2.get_y_axis_label("CO2\%").scale(0.6).move_to(chart2.get_left()+LEFT*.3).rotate(PI/2)
    c_bar_lbls2 = chart2.get_bar_labels(font_size=24)

    self.play(Transform(chart,chart2),Transform(y_label,y_label2),Transform(c_bar_lbls,c_bar_lbls2),Transform(title,title2))
    
    self.next_section("naturvardsverket.1",PresentationSectionType.SUB_NORMAL)
    naturvardsverket_text = Tex("\\textit{\"Domestic transport accounts for almost a third of Sweden's total emissions of greenhouse gases, and is dominated by emissions from road traffic.\"}",font_size=24)
    naturvardsverket = Tex("- The Swedish Environmental Protection Agency (2021)",font_size=24).move_to(naturvardsverket_text.get_bottom()+DOWN*.5)
    naturvardsverket_link = Tex("Translated quote from https://www.naturvardsverket.se/data-och-statistik/klimat/vaxthusgaser-utslapp-fran-inrikes-transporter",font_size=14).move_to(naturvardsverket_text.get_bottom() + DOWN)
    self.play(FadeOut(chart,y_label,c_bar_lbls,title),FadeIn(naturvardsverket_text,naturvardsverket,naturvardsverket_link))

    self.next_section("naturvardsverket.2",PresentationSectionType.SUB_NORMAL)
    naturvardsverket_text2 = Tex("\\textit{\"Over 95 percent of heavy trucks [in Sweden] are diesel-powered. In order to achieve the \\ climate goals, in addition to the use of biofuel and more energy efficient vehicles, smarter logistics are also needed.\"}",font_size=24)
    self.play(FadeOut(naturvardsverket_text),FadeIn(naturvardsverket_text2))


class B_VrpIntro(ThreeDScene):
    def construct(self):
        title = Title("Vehicle routing problem")
        self.next_section("Title",PresentationSectionType.NORMAL)
        self.add(title,createDevoteamLogo())
        bullets = BulletedList("Problem: Route multiple vehicles between A, B, C, D...","Minimize or maximize objectives","Satisfy constraints",font_size=24).move_to(LEFT*3)
        self.play(FadeIn(bullets))
        basicVRPGraph(self)
        self.next_section("showSwedenMap",PresentationSectionType.NORMAL)
        sweden_img = ImageMobject("./premadeImages/sweden.png").move_to(RIGHT*3.3+DOWN*.5).scale(0.8)

        self.next_section("showSwedenMap",PresentationSectionType.NORMAL)
        permList = BulletedList("15 nodes:","50 nodes:","75 nodes:",font_size=24).move_to(LEFT*3)

        self.play(FadeIn(sweden_img))
        self.next_section("bulletTransform",PresentationSectionType.SUB_NORMAL)
        self.play(Transform(bullets,permList))
        perm1 = Tex("{:.2E}".format(math.perm(15,15)),font_size=24).move_to(permList[0].get_right()+RIGHT)
        perm2 = Tex("{:.2E}".format(math.perm(50,50)),font_size=24).move_to(permList[1].get_right()+RIGHT)
        perm3 = Tex("{:.2E}".format(math.perm(75,75)),font_size=24).move_to(permList[2].get_right()+RIGHT)
        self.play(FadeIn(perm1))
        self.play(FadeIn(perm2))
        self.play(FadeIn(perm3))
        self.next_section("starsInUniverse",PresentationSectionType.SUB_NORMAL)
        stars = Tex("Stars in universe: 2.0E+23",font_size=24).move_to(perm3.get_bottom()+DOWN+LEFT*.85)
        self.play(FadeIn(stars))



        self.next_section("barcharts",PresentationSectionType.NORMAL)
        self.clear()
        barchartSlide(self)
        
            