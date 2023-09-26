from manim import *
import numpy as np


class Function1(Scene):
    def construct(self):
        # Define a quadratic function with changing parameters
        a_values = [100,0,0,100]
        b_values = [0,0.1,0,0.1]
        c_values = [0,0,3600,3600]

        # Create axes
        axes = Axes(
            x_range=[0, 1000,50],  # [xmin,xmax,xstep]
            y_range=[300,600,50],  # [ymin,ymax,ystep]
            axis_config={"color": BLUE},
        )

        # Add axes to the scene
        self.play(Create(axes))

        # Create a list to store the graph and equation objects
        graphs_and_equations = []

        # Animate the changing parameters and update the graph
        for a, b, c in zip(a_values, b_values, c_values):
            # Create the quadratic graph
            graph = self.get_graph(a, b, c)
            graph.set_color(ORANGE)

            # Create a text label to display the equation
            equation = MathTex(f"y = {a} + {b}x + {c}/x", color=WHITE)
            equation.to_corner(UL)

            # Append the graph and equation to the list
            graphs_and_equations.append((graph, equation))

        # Add the initial graph and equation to the scene
        self.play(Create(graphs_and_equations[0][0]))
        self.play(Create(graphs_and_equations[0][1]))

        # Animate the changing parameters
        for i in range(1, len(graphs_and_equations)):
            prev_graph, prev_equation = graphs_and_equations[0]
            new_graph, new_equation = graphs_and_equations[i]


            # Transform the equation
            self.play(Transform(prev_equation,new_equation))
            #self.play(Uncreate(prev_equation,run_time = 0.01))
            #self.play(Create(new_equation))


            # Transform the graph
            self.play(Create(new_graph))
            #self.play(Uncreate(prev_graph,run_time = 0.01))
            #self.play(Create(new_graph))

            # Wait for a moment
            self.wait(1)
       # graph.set_color(WHITE)



    def get_graph(self, a, b, c):
        # Define a quadratic function
        def func(x):
            return a + b * x + c*x**(-1)

        return ParametricFunction(lambda t: [t, func(t), 0], t_range=[100, 1000,5])

if __name__ == "__main__":
    config.pixel_height = 680
    config.pixel_width = 800
    config.frame_height = 7.0
    config.frame_width = 7.0
    config.frame_rate = 30

    scene = Function1()
    scene.render()

