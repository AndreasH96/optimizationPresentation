from manim import *

def createDevoteamLogo():
    devoteamLogo = ImageMobject("./premadeImages/devoteam.png").scale(0.2).move_to(DOWN*3.2+LEFT*5)
    # if(animate):
    #     self.play(FadeIn(devoteamLogo))
    # else:
    #     self.add(devoteamLogo)
    return devoteamLogo