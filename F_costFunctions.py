from manim import *
from manim_editor import PresentationSectionType
from utils import createDevoteamLogo


class F_CostFunctions(Scene):
    def construct(self):
        title_text = Title("Cost functions").move_to(UP*3.5)
        self.play(FadeIn(title_text,createDevoteamLogo()))    
        economic_title = Title("Economic",include_underline=False)
        environmental_title = Title("Environmental",include_underline=False)
        social_title = Title("Social",include_underline=False)

        cost_title_place= UP*2 + RIGHT *3

        time_title = Title("Drive Time",include_underline=False).move_to(cost_title_place)
        fuel_title = Title("Fuel Consumption",include_underline=False).move_to(cost_title_place)
        gini_title = Title("Gini Index",include_underline=False).move_to(cost_title_place)

        cost_place = RIGHT * 3 
        time_cost = MathTex("O_T"," = \sum^{E}_","{(i,j) \in E}","{T_{i,j}","x_{i,j}} ").move_to(cost_place)
        fuel_cost = MathTex("O_F = \sum^{E}_{(i,j) \in E}{F_{i,j}x_{i,j}} ").move_to(cost_place)
        gini_cost = MathTex("G = 2 \int_{0}^{1} [p - L(p)]dp").move_to(cost_place)
        framebox1 = SurroundingRectangle(time_cost[0],buff=0.1)
        framebox2 = SurroundingRectangle(time_cost[2],buff=0.1)
        framebox3 = SurroundingRectangle(time_cost[4],buff=0.1)
        framebox4 = SurroundingRectangle(time_cost[3],buff=0.1)
        cmem_table_raw = r"""\begin{table}[H]
            \centering
            \begin{tabular}{c|c}
                Notation & Description  \\
                \hline
                $\xi$ & Fuel-to-air mass ratio  \\
                $\kappa$ & Heating value of diesel \\
                $\psi$ & Conversion factor (g/L)  \\
                $k$ & Engine friction factor (kJ/rev/L) \\
                $N_e$ & Engine speed (rev/s)  \\
                $V$ & Engine displacement (L)  \\
                $C_d$ & Aerodynamic drag coefficient  \\
                $\rho$ & Air density (kg/$m^3$)  \\
                $\mu$ & Vehicle gross weight (kg) \\
                $g$ & Gravitational constant (m/$s^2$)  \\
                $\phi$ & Road gradient  \\
                $C_r$ & Rolling resistance coefficient  \\
                $\varepsilon$ & Drive train efficiency \\
                $\varpi$ & Efficiency parameter for diesel engines  \\
                $v$ & Vehicle Speed (m/s) \\
                $f$ & Vehicle load weight (kg)  \\
            \end{tabular}
        \end{table}"""



        titles = VGroup(economic_title,environmental_title,social_title).arrange(direction=DOWN, aligned_edge=LEFT).move_to(LEFT*4.5)
        titles.set_opacity(0.3)
        self.play(FadeIn(titles))
        self.next_section("Drive time",PresentationSectionType.NORMAL)
        titles.submobjects[0].set_opacity(1)
        self.play(Transform(titles,titles),FadeIn(time_title,time_cost))
        
        self.next_section("Drive time.1",PresentationSectionType.SUB_NORMAL)
        self.play(Create(framebox1))
        self.next_section("Drive time.2",PresentationSectionType.SUB_NORMAL)
        self.play(ReplacementTransform(framebox1,framebox2))
        self.next_section("Drive time.3",PresentationSectionType.SUB_NORMAL)
        self.play(ReplacementTransform(framebox2,framebox3))
        self.next_section("Drive time.4",PresentationSectionType.SUB_NORMAL)
        self.play(ReplacementTransform(framebox3,framebox4))
        self.next_section("Fuel consumption",PresentationSectionType.NORMAL)
        titles.set_opacity(0.3)
        titles.submobjects[1].set_opacity(1)
        self.play(Transform(titles,titles),FadeOut(time_title,time_cost,framebox4),FadeIn(fuel_title,fuel_cost))
        
        self.next_section("Fuel consumption in depth 1",PresentationSectionType.SUB_NORMAL)
        fuel_cost_temp = fuel_cost.copy()
        cmem_model_text = Tex("CMEM model",font_size=24).move_to(cost_title_place + DOWN)
    
        fuel_rate_func= MathTex(r"FR = \frac{\xi}{\kappa\psi}\left( kN_eV + \frac{0.5C_d\rho v^3 + (\mu + f)v(gsin\phi + gC_rcos\phi)}{1000\varepsilon\varpi}\right)",font_size=26).move_to(cost_place)
        self.play(Transform(fuel_cost,fuel_rate_func,replace_mobject_with_target_in_scene=False),FadeIn(cmem_model_text))
        
        self.next_section("Fuel consumption in depth 1 table",PresentationSectionType.SUB_NORMAL)
        cmem_table = Tex(cmem_table_raw).move_to(LEFT*4).scale(.5)
        self.play(FadeIn(cmem_table),FadeOut(titles),)

        self.next_section("Fuel consumption in depth 2",PresentationSectionType.SUB_NORMAL)
        fuel_func = MathTex(r"F_{i,j} = \lambda\left( kN_eV\frac{d_{i,j}}{v_{i,j}} + \gamma\beta d_{i,j} v_{i,j}^2 + \gamma\alpha(\mu_{i} + f)d_{i,j} \right)",font_size=26).move_to(cost_place)
        self.play(Transform(fuel_cost,fuel_func,replace_mobject_with_target_in_scene=False))

        self.next_section("Fuel consumption back to normal",PresentationSectionType.SUB_NORMAL)
        self.play(Transform(fuel_cost,fuel_cost_temp,fuel_cost_temp=False),FadeOut(cmem_model_text,cmem_table),FadeIn(titles))

        self.next_section("Gini Index",PresentationSectionType.NORMAL)
        titles.set_opacity(0.3)
        titles.submobjects[2].set_opacity(1)
        self.play(Transform(titles,titles),FadeOut(fuel_title,fuel_cost),FadeIn(gini_title,gini_cost))

        self.next_section("Gini index in depth",PresentationSectionType.SUB_NORMAL)
        lorens_text = Tex("Lorenz curve: The worlds poorest 20\% only earn  1\% of the income",font_size=24).move_to(cost_title_place+DOWN)
        lorens_eq = MathTex("L(0.20) = 0.01").move_to(cost_place)
        gini_cost_temp = gini_cost.copy()
        self.play(FadeIn(lorens_text),Transform(gini_cost,lorens_eq,replace_mobject_with_target_in_scene=False))

        self.next_section("Gini index back from depth",PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(lorens_text),Transform(gini_cost,gini_cost_temp,replace_mobject_with_target_in_scene=False))