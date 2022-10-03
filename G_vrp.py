from tkinter import BOTTOM
from types import NoneType
from manim import *
from manim_editor import PresentationSectionType
from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.operator import BinaryTournamentSelection
from jmetal.operator.crossover import PMXCrossover
from jmetal.operator.mutation import PermutationSwapMutation
from jmetal.util.comparator import MultiComparator
from jmetal.util.density_estimator import CrowdingDistance
from jmetal.util.ranking import FastNonDominatedRanking
from jmetal.util.termination_criterion import StoppingByEvaluations
import cv2
from utils import createDevoteamLogo

first_gif_path = "./premadeImages/vrp_search_small.gif"
first_image_path = "./premadeImages/london_75_before.png"
second_image_path = "./premadeImages/london_75_after.png"

class G_VRPGraph(ThreeDScene):
    def construct(self):
        self.next_section("VRP_INTRO",PresentationSectionType.NORMAL)
        title = Title("Time to solve!")
        blist = BulletedList("Problem: Vehicle Routing Problem","Objectives: Fuel Consumption, Drive Time, Gini Index","Constraints: 8 hours drive time, Total load ...","Solver: Indicator Based Evolutionary Algorithm (IBEA)",font_size=28)
        self.play(FadeIn(title,blist))
        self.next_section("VRP_GIF",PresentationSectionType.NORMAL)
        self.play(FadeOut(blist))
        show_GIF(self,first_gif_path,0.2,position=DOWN*.9,scale=0.8)

        first_img = ImageMobject(first_image_path).move_to(DOWN)
        second_img = ImageMobject(second_image_path).move_to(DOWN*.9)
        self.play(FadeIn(first_img),Transform(title,Title("A larger example")))
        self.next_section("VRP large image.2",PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(first_img),FadeIn(second_img))
def show_GIF(self,path,waitAmount, position=None,scale=None):
    cap = cv2.VideoCapture(path)
    flag = True
    first=True
    frame_img = None
    while flag:
        flag, frame = cap.read()
        
        if flag:
            if frame_img != None:
                self.remove(frame_img)

            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_img = ImageMobject(frame)
            if(type(position) != NoneType):
                frame_img.move_to(position)
            if(type(scale) != NoneType):
                frame_img.scale(scale)
            self.add(frame_img)
            self.wait(waitAmount)
            if first:
                self.next_section("VRP_GIF_FIRST",PresentationSectionType.SUB_NORMAL)
                first=False
            
    cap.release()
    self.next_section("VRP_GIF_HOLD_MOVE_LAST",PresentationSectionType.SUB_NORMAL)
    blist = BulletedList("77.48L to 66.73L","6 to 3 vehicles",font_size=28).move_to(LEFT*4)
    new_img = frame_img.copy()
    new_img.move_to(RIGHT*2 + position)
    self.play(Transform(frame_img,new_img),FadeIn(blist))
    self.next_section("VRP_GIF_HOLDLAST",PresentationSectionType.SUB_NORMAL)
    self.play(FadeOut(frame_img,blist))

""" def create_VRP_animation(self,node_amount=10):
        problem = MyTSP("./vrpdata//kroA{}.tsp".format(node_amount))
        nodeArray = np.loadtxt("./vrpdata/temp_{}.txt".format(node_amount),dtype=int)
        path = VMobject()
        
        layout = {x[0]-1: [(x[1]-np.mean(nodeArray[:,1]))/100,(x[2]-np.mean(nodeArray[:,2]))/100,0] for x in nodeArray}
        graph = Graph(vertices=layout.keys(),edges=[],layout=layout,labels=True, vertex_config={0:{"fill_color":GREEN}})
        self.play(FadeIn(graph))
        
        max_evaluations = 100 * node_amount
        observer_update_interval = 60
        
        algorithm = GeneticAlgorithm(
            problem=problem,
            population_size=100,
            offspring_population_size=100,
            mutation=PermutationSwapMutation(1.0 / problem.number_of_variables),
            crossover=PMXCrossover(0.8),
            selection=BinaryTournamentSelection(
                MultiComparator([FastNonDominatedRanking.get_comparator(), CrowdingDistance.get_comparator()])
            ),
            termination_criterion=StoppingByEvaluations(max_evaluations=max_evaluations),
        )
        performance_observer = PerformanceObserver(max_iter=max_evaluations,frequency=observer_update_interval)
        algorithm.observable.register(observer=performance_observer)
        algorithm.run()
        node_amount_text = Text("{} Nodes".format(node_amount)).move_to(UP*10 + LEFT*5)
        self.add(node_amount_text)
        self.next_section("VRP_{}.1".format(node_amount),PresentationSectionType.SUB_NORMAL)
        current_cost = Text("Cost: ").move_to(UP*10)
        self.add(current_cost)
        unique_cost=set()
        for path,cost in zip(performance_observer.path_history,performance_observer.fitness_history):
            if (not cost[0]  in unique_cost):
                unique_cost.add(cost[0])

                first_edge = (list(layout.keys())[0],path[0]+1)
                final_edge = (path[-1]+1,list(layout.keys())[0])

                edges = [first_edge]
                edges.extend([(path[i]+1,path[i+1]+1) for i in range(len(path)-1)])
                edges.append(final_edge)
                self.wait(.4)
                self.remove(graph)
                graph = Graph(vertices=layout.keys(),edges=edges,layout=layout,labels=True,
                    vertex_config={0:{"fill_color":GREEN},},
                    edge_config={first_edge: {"stroke_color": GREEN},
                                final_edge: {"stroke_color": RED}})

                self.add(graph)
                self.play(Transform(current_cost,Text("Cost: {}".format(cost[0])).move_to(UP*10)))
           """