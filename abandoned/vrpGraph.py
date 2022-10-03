from tkinter import BOTTOM
from manim import *
from manim_editor import PresentationSectionType

import networkx as nx

class VRPGraph(Scene):
    def construct(self):
        path = VMobject()
        start_pos = [-1,2,0]
        start_point = Dot(point=start_pos,color=GREEN)
        start_label = Text("Start",font_size=14).move_to(start_point.get_right() + RIGHT * .3)

        pen = Dot(point=start_pos,color=RED)

        points = [[.1,1,0],[.4,.7,0],[0,0,0]]
        dots = [Dot(point=p) for p in points]

        path.set_points_as_corners([pen.get_center(), pen.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([pen.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, pen,start_point,start_label)
        labels = [Text("A",font_size=14),Text("B",font_size=14),Text("C",font_size=14)]
        [l.move_to(d.get_right()+RIGHT*.2) for l,d in zip(labels,dots)]  
        self.add(*dots,*labels)
        for dot in dots:
            self.play(pen.animate.move_to(dot.get_center()))
            self.wait(1)

        new_points_1 = [[.8,1.2,0],[.5,1.8,0],[.1,2,0],[.3,-1,0],[.6,-0.5,0],[-.4,.2,0],[-.1,0.5,0],[-1,1.5,0],[-.8,-1,0],[-.41,-0.5,0]]
        new_dots_1 =  [Dot(point=p) for p in new_points_1]
        self.play(FadeIn(*new_dots_1))

        #imageObj = ImageMobject("")
        # autolayouts = ["spring", "circular", "kamada_kawai",
        #                "planar", "random", "shell",
        #                "spectral", "spiral"]
        # title = Title("Vehicle Routing Problem",include_underline=False)

        # self.next_section("VRPGraph",PresentationSectionType.NORMAL)
        # self.play(FadeIn(title))
        
        # small_graph_vertices = [1,2,3,4,5]
        # small_graph_edges = [(1,2),(2,5),(5,3),(3,4),(4,1)]
        # small_graph_layout = {1: [0,1, 0], 2: [0.5, 0.5, 0], 3: [1, -1, 0], 4: [0.4, -.7, 0],5:[0.7,-0.4,0]}
        # small_graph =  Graph(small_graph_vertices,small_graph_edges,layout=small_graph_layout,vertex_config={1:{"fill_color":RED}})

        
        
        # vertices = [1, 2, 3, 4, 5, 6, 7, 8]
        # edges = [(1, 7), (1, 8), (2, 3), (2, 4), (2, 5),
        #          (2, 8), (3, 4), (6, 1), (6, 2),
        #          (6, 3), (7, 2), (7, 4)]
        


        # largeGraph = Graph(vertices,edges,layout="circular")
        # self.add(small_graph.get_edge)
        #self.play(Write())