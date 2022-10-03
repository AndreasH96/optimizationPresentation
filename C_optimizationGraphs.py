from math import pi
from numpy import*
from manim import *
from manim_editor import PresentationSectionType
from utils import createDevoteamLogo

class C_OptimizationGraphs(ThreeDScene):
    def construct(self):
            devoteamLogo = createDevoteamLogo()
            title = Title("Optimization")
            self.add(title)
            blist = BulletedList("Define problem (VRP)","Define fitness function","Select solver","Victory",font_size=28).move_to(LEFT*2)
            self.add(devoteamLogo)
            self.play(FadeIn(blist))
            self.next_section("OptimizationGraphs",PresentationSectionType.NORMAL)
            self.play(FadeOut(title,blist,devoteamLogo))
            ax = ThreeDAxes(
                x_range=[0, 6], y_range=[0, 5], z_range=[0,8], axis_config={"include_tip": False},z_axis_config={"stroke_width":0}
            )
            labels = ax.get_axis_labels(x_label="x", y_label="Cost")

            t = ValueTracker(1)
            t2 = ValueTracker(3)
            t3 = ValueTracker(4)
            t4 = ValueTracker(1)
            def func(x):
                return (x-3) ** 2

            def func2(x):
                return 3 + (x-3)**4 + (x-3)**3 - 2*(x-3)**2

            def func3(x,y):
                return  np.cos(x-y) * np.cos(x) * x + 3.5

            graph = ax.plot(func, color=MAROON)
            graph2 = ax.plot(func2,color=MAROON)
            graph3 = ax.plot_surface(func3,resolution=(24,24),v_range=[0,7],u_range=[0,7],colorscale=[(RED,0),(YELLOW,3),(BLUE,6)], colorscale_axis=2)

            initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
            initial_point2 = [ax.coords_to_point(t2.get_value(), func2(t2.get_value()))]
            initial_point3 = [ax.coords_to_point(t3.get_value(), func2(t3.get_value()))]
            initial_point4 = [ax.coords_to_point(t4.get_value(), func2(t4.get_value()))]
            dot = Dot(point=initial_point)
            dot2 = Dot(point=initial_point2)
            dot3 = Dot(point=initial_point3)
            dot4 = Dot(point=initial_point4)
            dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
            dot2.add_updater(lambda x: x.move_to(ax.c2p(t2.get_value(), func2(t2.get_value()))))
            dot3.add_updater(lambda x: x.move_to(ax.c2p(t3.get_value(), func2(t3.get_value()))))
            dot4.add_updater(lambda x: x.move_to(ax.c2p(t4.get_value(), func2(t4.get_value()))))

            x_space = np.linspace(*ax.x_range[:2],200)
            minimum_index = func(x_space).argmin()
            
            local_optima = func2(x_space[100:]).argmin()
            global_optima = func2(x_space).argmin()

            self.camera.set_zoom(0.6)
            blist = BulletedList("Evaluate with fitness function","Generate new candidates","Select new solution if improvement","Repeat",font_size=36).move_to(LEFT*8.5)

            self.play(FadeIn(ax, labels, graph, dot,blist))
            #=================================================#

            self.next_section("OptimizationGraphs.1",PresentationSectionType.SUB_NORMAL)
            potential_dot1 = Dot(point=[ax.coords_to_point(1.05, func(1.05))],color=BLUE) 
            potential_dot2 = Dot(point=[ax.coords_to_point(0.95, func(0.95))],color=BLUE) 
            self.play(FadeIn(potential_dot1,potential_dot2))

            self.next_section("OptimizationGraphs.1.1",PresentationSectionType.SUB_NORMAL)
            circle = Circle(radius=0.2,color=GREEN).move_to(potential_dot1.get_center())
            self.play(FadeOut(potential_dot2),FadeIn(circle))

            self.next_section("OptimizationGraphs.1.2",PresentationSectionType.SUB_NORMAL)
            self.play(t.animate.set_value(1.05),FadeOut(potential_dot1,circle))

            self.next_section("OptimizationGraphs.1.3",PresentationSectionType.SUB_NORMAL)
            self.play(t.animate.set_value(x_space[minimum_index]))
            
            self.next_section("OptimizationGraphs.2",PresentationSectionType.SUB_NORMAL)
            self.remove(dot)
            self.play(Transform(graph, graph2),FadeOut(blist))

            self.next_section("OptimizationGraphs.3",PresentationSectionType.SUB_NORMAL)
            self.add(dot2)
            self.wait(2)
            self.play(t2.animate.set_value(x_space[100+local_optima]))

            self.next_section("OptimizationGraphs.4",PresentationSectionType.SUB_NORMAL)
            self.add(dot3)
            self.add(dot4)
            self.wait(2)
            self.play(t3.animate.set_value(x_space[100+local_optima]))
            self.play(t4.animate.set_value(x_space[global_optima]))

            self.next_section("OptimizationGraphs.5",PresentationSectionType.SUB_NORMAL)
        
            self.remove(labels)
            new_labels = ax.get_axis_labels(x_label="x", y_label="y")
            z_label = ax.get_z_axis_label("Cost")
            self.play(Unwrite(graph))
            self.remove(dot,dot2,dot3,dot4)
            ax.z_axis.set_stroke(width=1)
            self.move_camera(phi=60 * DEGREES,theta=-85*DEGREES,zoom=0.4)
            self.add(new_labels,z_label)
            self.play(Write(graph3))

            self.next_section("OptimizationGraphs.6",PresentationSectionType.SUB_NORMAL)
            self.begin_ambient_camera_rotation(rate=0.6)
            self.wait(5)
            self.stop_ambient_camera_rotation()
        
            self.next_section("OptimizationGraphs.7",PresentationSectionType.SUB_NORMAL)
            self.clear()
            self.set_camera_orientation(0,0,90*DEGREES)
            self.move_camera(zoom=1)
            text = Tex("All we can do is find a \\textbf{\"Good enough\"} solution",font_size=28)
            self.play(FadeIn(text,devoteamLogo))

            self.next_section("OptimizationGraphs.8",PresentationSectionType.SUB_NORMAL)
            title = Title("Algorithms")
            blist = BulletedList("Simulated Annealing","Genetic Algorithm","Artificial Ant Colony",font_size=28)
            self.play(FadeOut(text),FadeIn(title,blist))