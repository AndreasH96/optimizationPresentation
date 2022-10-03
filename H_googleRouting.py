from numpy import*
from manim import *
from manim_editor import PresentationSectionType
from utils import createDevoteamLogo

google_gif_path = "./premadeImages/Ireland_route_full_flow.gif"

class H_GoogleRoutingSlides(ThreeDScene):
    def construct(self):
        self.next_section("InternetBrowser",PresentationSectionType.NORMAL)
        title = Title('Now to the internet Bowser!')
        koopaImg = ImageMobject("./premadeImages/koopa.png")
        self.play(FadeIn(title,koopaImg,createDevoteamLogo()))
        