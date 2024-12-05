from tkinter import CENTER
import numpy as np
from manim import *
from manim_pptx import PPTXScene
class shortestPath(PPTXScene):
    def construct(self):
        self.begin()
        self.makeGraph()
        self.psuedoAlgo()

    def begin(self):
        title_bfs = Text("BFS Application : Shortest Path", font="Calibri", font_size=65, color=BLUE_D, weight=BOLD)
        
        # Center 'BFS' in the middle of the screen
        title_bfs.move_to(ORIGIN)

        # Animate the 'BFS' title
        self.play(Write(title_bfs))
        self.wait(2)

        # Move the title up
        title_bfs.generate_target()
        title_bfs.target.to_edge(UP)
        self.play(MoveToTarget(title_bfs))
        
        # Manually adjust the text for each bullet point
        bullet_point_1_text = (
            "By using BFS We can find Single-Sorce Shortest Path of\n"
            "Unweighted Graph or Graph with equal weight edges."
        )
        bullet_point_2_text = (
            "It runs with a time complexity of O(V+E)."
        )
        bullet_point_3_text = (
            "We can also use BFS in Weighted graph by modifying\n"
            "each edges Ei have Wi unit weight into Wi edges each\n "
            "having Weight 1 unit. We dont use this due to its\n"
            "Time Complexity."
        )
        # Bullet Point 1
        bullet_point_1 = Text(
            bullet_point_1_text,
            t2c={"Unweighted Graph or Graph with equal weight edges": RED}
        ).scale(0.7)
        bullet_point_1.next_to(title_bfs.target, DOWN, buff=1)
        self.play(Write(bullet_point_1))
        self.wait(2)

        # Bullet Point 2
        bullet_point_2 = Text(
            bullet_point_2_text,
            t2c={"O(V+E)": RED}
        ).scale(0.7)
        bullet_point_2.next_to(bullet_point_1, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(bullet_point_2))
        self.wait(2)

        # Bullet Point 3
        bullet_point_3 = Text(
            bullet_point_3_text,
            
        ).scale(0.7)
        bullet_point_3.next_to(bullet_point_2, DOWN, aligned_edge=LEFT, buff=0.5)
        self.play(Write(bullet_point_3))
        self.wait(2)

        # Fade out all elements
        self.play(FadeOut(title_bfs, bullet_point_1, bullet_point_2, bullet_point_3))
        
    def makeGraph(self):
        self.node_R = Circle(color=BLUE,radius=0.35).shift(LEFT * 4 + UP * 2)
        self.node_S = Circle(color=BLUE,radius=0.35).shift(UP * 2 + LEFT * 2)
        self.node_V = Circle(color=BLUE,radius=0.35).shift(LEFT * 4)
        self.node_W = Circle(color=BLUE,radius=0.35).shift(LEFT * 2)
        self.node_T = Circle(color=BLUE,radius=0.35).shift(UP * 2)
        self.node_X = Circle(color=BLUE,radius=0.35)
        self.node_U = Circle(color=BLUE,radius=0.35).shift(RIGHT * 3 + UP * 2)
        self.node_Y = Circle(color=BLUE,radius=0.35).shift(RIGHT * 3)
        
        self.edge2 = Line(self.node_R, self.node_S, buff=0.05)
        self.edge3 = Line(self.node_S, self.node_W, buff=0.05)
        self.edge4 = Line(self.node_R, self.node_V, buff=0.05)
        self.edge5 = Line(self.node_W, self.node_X, buff=0.05)
        self.edge6 = Line(self.node_W, self.node_T, buff=0.05)
        self.edge7 = Line(self.node_T, self.node_U, buff=0.05)
        self.edge8 = Line(self.node_T, self.node_X, buff=0.05)
        self.edge9 = Line(self.node_X, self.node_U, buff=0.05)
        self.edge10 = Line(self.node_U, self.node_Y, buff=0.05)
        self.edge1 = Line(self.node_X, self.node_Y, buff=0.05)


        node_R_label = Text("R").next_to(self.node_R, UP).scale(0.5)
        node_S_label = Text("S").next_to(self.node_S, UP).scale(0.5)
        node_V_label = Text("V").next_to(self.node_V, DOWN).scale(0.5)
        node_W_label = Text("W").next_to(self.node_W, DOWN).scale(0.5)
        node_T_label = Text("T").next_to(self.node_T, UP).scale(0.5)
        node_X_label = Text("X").next_to(self.node_X, DOWN).scale(0.5)
        node_U_label = Text("U").next_to(self.node_U, UP).scale(0.5)
        node_Y_label = Text("Y").next_to(self.node_Y, DOWN).scale(0.5)

        labels = [node_R_label, node_S_label, node_V_label, node_W_label, node_T_label, node_X_label, node_U_label, node_Y_label]

        # Add labels to the scene
        self.play(*[Create(label) for label in labels])
        
        self.group=VGroup(self.node_S,self.node_R,self.node_Y,self.node_X,self.node_T,self.node_U,self.node_V,self.node_W,self.edge1,self.edge2,self.edge3,self.edge4,self.edge5,self.edge6,self.edge7,self.edge8,self.edge9,self.edge10)

        # self.play(Create(edge), Write(weight_label))
        # Display nodes and edge
        nodeGroup = Group(self.node_S, self.node_R, self.node_Y, self.node_X, self.node_T, self.node_U, self.node_V, self.node_W)
        self.play(FadeIn(nodeGroup))

        # Create and display edges
        self.play(Create(self.edge1), Create(self.edge2), Create(self.edge3), Create(self.edge4), Create(self.edge5), Create(self.edge6),
                Create(self.edge7), Create(self.edge8), Create(self.edge9), Create(self.edge10))

        # Create and display infinity symbol at different positions
        infinity_sign = MathTex("\\infty").scale(0.75)

        # Set the position of the infinity sign
        positions = [self.node_R, self.node_Y, self.node_X, self.node_T, self.node_U, self.node_V, self.node_W]

        t1 = Tex(0).scale(0.75)
        t1.move_to(self.node_S)
        self.play(Create(t1))
        self.add(t1)
        for position in positions:
            current_infinity_sign = infinity_sign.copy().move_to(position)
            self.play(Create(current_infinity_sign))
            self.add(current_infinity_sign)


        self.node_S = Circle(color= GREEN, fill_opacity=0.35,radius=0.35).shift(UP * 2 + LEFT * 2)
        self.edge2 = Line(self.node_R, self.node_S, buff=0.05,color = GREEN)
        self.edge3 = Line(self.node_S, self.node_W, buff=0.05,color = GREEN)
        self.play(Create(self.node_S),Create(self.edge3),Create(self.edge2))
  
        title = Tex("Queue : ",color = BLUE).move_to(DOWN * 2 + LEFT * 3)
        self.play(Create(title))
        # Add elements to the queue (you can customize this part based on your needs)
        element = Text(str("S"), font_size=20)  # Adjust font size if needed
        visited_s = Rectangle(width=0.5,height=0.5, color=GREEN, fill_opacity=0.2)
        visited_s.add(element)

        # Set the position of the queue below the graph
        visited_s.move_to(DOWN * 2 + LEFT * 1.5)  # Adjust the vertical distance

        context = Tex("Now S is dequed and it's neighbours R and W added to the queue and then distance of neighbours will be updated as 0 + 1 = 1",color = RED,font_size=30).move_to(DOWN * 3)
        self.play(Create(context))
        # Display the queue
        self.play(Create(visited_s))

        self.node_S = Circle(color= RED, fill_opacity=0.35,radius=0.35).shift(UP * 2 + LEFT * 2)
        self.edge3 = Line(self.node_S, self.node_W, buff=0.05,color = RED)
        self.edge2 = Line(self.node_S, self.node_R, buff=0.05,color = RED)
        self.play(Create(self.node_S),Create(self.edge3),Create(self.edge2))

        self.node_R = Circle(color=BLACK,radius=0.35,fill_opacity=1).shift(LEFT * 4 + UP * 2)
        self.node_W = Circle(color=BLACK,radius=0.35,fill_opacity=1).shift(LEFT * 2)
        self.play(Create(self.node_R),Create(self.node_W))
        self.node_R = Circle(color=GREEN,radius=0.35,fill_opacity=0.35).shift(LEFT * 4 + UP * 2)
        self.node_W = Circle(color=GREEN,radius=0.35,fill_opacity=0.35).shift(LEFT * 2)
        self.play(Create(self.node_R),Create(self.node_W))
        new_element = MathTex("1").scale(0.75)  # You can customize this with your desired symbol or text
        new_element.move_to(positions[0])  # Replace '1' with the index of the position you want to replace
        self.add(new_element)
        new_element = MathTex("1").scale(0.75)  # You can customize this with your desired symbol or text
        new_element.move_to(positions[6])  # Replace '1' with the index of the position you want to replace
        self.add(new_element)

        
        self.play(FadeOut(context,visited_s))

        element = Text(str("W"), font_size=20)  # Adjust font size if needed
        visited_w = Rectangle(width=0.5,height=0.5, color=GREEN, fill_opacity=0.2)
        visited_w.add(element)
        # Set the position of the queue below the graph
        visited_w.move_to(DOWN * 2 + LEFT * 1.5)  # Adjust the vertical distance
        element = Text(str("R"), font_size=20)  # Adjust font size if needed
        visited_r = Rectangle(width=0.5,height=0.5, color=GREEN, fill_opacity=0.2)
        visited_r.add(element)
        # Set the position of the queue below the graph
        visited_r.move_to(DOWN * 2 + LEFT * 0.9)
        self.play(Create(visited_w),Create(visited_r))

        context = Tex("W is deqeued and it's neighbour T and X added into the queue then thier distance will updated as 1 + 1 = 2",color = RED,font_size=30).move_to(DOWN * 3)
        self.play(Create(context))

        self.node_W = Circle(color= RED, fill_opacity=0.35,radius=0.35).shift(LEFT * 2)
        self.edge5 = Line(self.node_W, self.node_T, buff=0.05,color = RED)
        self.edge6 = Line(self.node_W, self.node_X, buff=0.05,color = RED)
        self.play(Create(self.node_W),Create(self.edge5),Create(self.edge6))

        self.node_T = Circle(color=BLACK,radius=0.35,fill_opacity=1).shift(UP * 2)
        self.node_X = Circle(color=BLACK,radius=0.35,fill_opacity=1)
        self.play(Create(self.node_T),Create(self.node_X))
        self.node_T = Circle(color=GREEN,radius=0.35,fill_opacity=0.35).shift(UP * 2)
        self.node_X = Circle(color=GREEN,radius=0.35,fill_opacity=0.35)
        self.play(Create(self.node_T),Create(self.node_X))
        new_element = MathTex("2").scale(0.75)  # You can customize this with your desired symbol or text
        new_element.move_to(positions[2])  # Replace '1' with the index of the position you want to replace
        self.add(new_element)
        new_element = MathTex("2").scale(0.75)  # You can customize this with your desired symbol or text
        new_element.move_to(positions[3])  # Replace '1' with the index of the position you want to replace
        self.add(new_element)

        
        self.play(FadeOut(visited_w))
        visited_r.move_to(DOWN * 2 + LEFT * 1.5)
        element = Text(str("X"), font_size=20)  # Adjust font size if needed
        visited_x = Rectangle(width=0.5,height=0.5, color=GREEN, fill_opacity=0.2)
        visited_x.add(element)
        # Set the position of the queue below the graph
        visited_x.move_to(DOWN * 2 + LEFT * 0.3)  # Adjust the vertical distance
        element = Text(str("T"), font_size=20)  # Adjust font size if needed
        visited_t = Rectangle(width=0.5,height=0.5, color=GREEN, fill_opacity=0.2)
        visited_t.add(element)
        # Set the position of the queue below the graph
        visited_t.move_to(DOWN * 2 + LEFT * 0.9)
        self.play(Create(visited_x),Create(visited_t))

        self.play(FadeOut(context))


        context = Tex("R is deqeued and it's neighbour V added into the queue then thier distance will updated as 1 + 1 = 2",color = RED,font_size=30).move_to(DOWN * 3)
        self.play(Create(context))

        self.node_R = Circle(color= RED, fill_opacity=0.35,radius=0.35).shift(LEFT * 4 + UP * 2)

        self.play(Create(self.node_R))
        
        self.node_V = Circle(color=BLACK,radius=0.35,fill_opacity=1).shift(LEFT * 4)
        self.play(Create(self.node_V))
        self.node_V = Circle(color=GREEN,radius=0.35,fill_opacity=0.35).shift(LEFT * 4)
        self.play(Create(self.node_V))
        self.edge4 = Line(self.node_R, self.node_V, buff=0.05,color = RED)
        self.play(Create(self.edge4))
        new_element = MathTex("2").scale(0.75)  # You can customize this with your desired symbol or text
        new_element.move_to(positions[5])  # Replace '1' with the index of the position you want to replace
        self.add(new_element)


        self.play(FadeOut(visited_r))
        visited_t.move_to(DOWN * 2 + LEFT * 1.5)
        visited_x.move_to(DOWN * 2 + LEFT * 0.9)
        element = Text(str("V"), font_size=20)  # Adjust font size if needed
        visited_v = Rectangle(width=0.5,height=0.5, color=GREEN, fill_opacity=0.2)
        visited_v.add(element)
        # Set the position of the queue below the graph
        visited_v.move_to(DOWN * 2 + LEFT * 0.3)
        self.play(Create(visited_v))
  
        self.play(FadeOut(context))


        context = Tex("T is deqeued and it's neighbour U added into the queue then thier distance will updated as 1 + 2 = 3",color = RED,font_size=30).move_to(DOWN * 3)
        self.play(Create(context))

        self.node_T = Circle(color= RED, fill_opacity=0.35,radius=0.35).shift(UP * 2)
        self.edge7 = Line(self.node_U, self.node_T, buff=0.05,color = RED)
        self.edge8 = Line(self.node_X, self.node_T, buff=0.05,color = RED)
        self.play(Create(self.node_T),Create(self.edge7),Create(self.edge8))

        self.node_U = Circle(color=BLACK,radius=0.35,fill_opacity=1).shift(RIGHT * 3 + UP * 2)
        self.play(Create(self.node_U))
        self.node_U = Circle(color=GREEN,radius=0.35,fill_opacity=0.35).shift(RIGHT * 3 + UP * 2)
        self.play(Create(self.node_U))
        new_element = MathTex("3").scale(0.75)  # You can customize this with your desired symbol or text
        new_element.move_to(positions[4])  # Replace '1' with the index of the position you want to replace
        self.add(new_element)
        
        self.play(FadeOut(visited_t))
        visited_x.move_to(DOWN * 2 + LEFT * 1.5)
        visited_v.move_to(DOWN * 2 + LEFT * 0.9)
        element = Text(str("U"), font_size=20)  # Adjust font size if needed
        visited_u = Rectangle(width=0.5,height=0.5, color=GREEN, fill_opacity=0.2)
        visited_u.add(element)
        # Set the position of the queue below the graph
        visited_u.move_to(DOWN * 2 + LEFT * 0.3)  # Adjust the vertical distance
        self.play(Create(visited_u))

        self.play(FadeOut(context))

        context = Tex("X is deqeued and it's neighbour Y added into the queue then thier distance will updated as 1 + 2 = 3",color = RED,font_size=30).move_to(DOWN * 3)
        self.play(Create(context))

        self.node_X = Circle(color= RED, fill_opacity=0.35,radius=0.35)
        self.edge1 = Line(self.node_X, self.node_Y, buff=0.05,color = RED)
        self.play(Create(self.node_X),Create(self.edge1))

        self.node_Y = Circle(color=BLACK,radius=0.35,fill_opacity=1).shift(RIGHT * 3)
        self.play(Create(self.node_Y))
        self.node_Y = Circle(color=GREEN,radius=0.35,fill_opacity=0.35).shift(RIGHT * 3)
        self.play(Create(self.node_Y))
        new_element = MathTex("3").scale(0.75)  # You can customize this with your desired symbol or text
        new_element.move_to(positions[1])  # Replace '1' with the index of the position you want to replace
        self.add(new_element)
        
        self.play(FadeOut(visited_x))
        visited_v.move_to(DOWN * 2 + LEFT * 1.5)
        visited_u.move_to(DOWN * 2 + LEFT * 0.9)
        element = Text(str("Y"), font_size=20)  # Adjust font size if needed
        visited_y = Rectangle(width=0.5,height=0.5, color=GREEN, fill_opacity=0.2)
        visited_y.add(element)
        # Set the position of the queue below the graph
        visited_y.move_to(DOWN * 2 + LEFT * 0.3)  # Adjust the vertical distance
        self.play(Create(visited_y))

        self.play(FadeOut(context))

        context = Tex("Vertices V, U, and Y do not have any unvisited neighbors. Consequently, they will be dequeued one by one, resulting in an empty queue, indicating the completion of the algorithm.",color = RED,font_size=30).move_to(DOWN * 3)
        self.play(Create(context))
        self.play(FadeOut(visited_v))
        visited_u.move_to(DOWN * 2 + LEFT * 1.5)
        visited_y.move_to(DOWN * 2 + LEFT * 0.9)
        self.node_V = Circle(color= RED, fill_opacity=0.35,radius=0.35).shift(LEFT * 4)
        self.play(Create(self.node_V))

        self.play(FadeOut(visited_u))
        visited_y.move_to(DOWN * 2 + LEFT * 1.5)
        self.node_U = Circle(color= RED, fill_opacity=0.35,radius=0.35).shift(RIGHT * 3 + UP * 2)
        self.play(Create(self.node_U))

        self.play(FadeOut(visited_y))
        self.node_Y = Circle(color= RED, fill_opacity=0.35,radius=0.35).shift(RIGHT * 3)
        self.play(Create(self.node_Y))

        self.play(FadeOut(*self.mobjects))

        
        
    def psuedoAlgo(self):
        title = Tex("Implementing the BFS Shortest Path finding algorithm", color=BLUE, font_size=40)
        self.play(Write(title))
        
        self.play(FadeOut(title))
        code_scale = 0.5
        buffer=0.4
        map = { "$n$":GOLD,"$o$": GOLD,"Green":GREEN,"Red": RED,"$\leftarrow$":GREEN ,"$r$":GOLD, "$f$":GOLD, "\{":ORANGE,"\}":ORANGE,"\cup":GREEN,"while":RED_D,"if":RED_D}
        code = []
        code.append(("BFS (G,s)"))
        code.append(("Let Q be Priority Queue."))
        code.append(("$f$","$o$","$r$"," each u","$\in$", " G.V","$-$","(","$s$",")"))
        code.append(("u.color", "$\leftarrow$", "Black"))
        code.append(("u.d","$\leftarrow$","$\infty$"))
        code.append(("u.prev","$\leftarrow$","NIL"))
        code.append(("s.color", "$\leftarrow$", "\\text{Green}"))
        code.append(("s.d","$\leftarrow$","$0$"))
        code.append(("Q.enqueue","$($","$s$","$)$"))
        code.append(("while ","$($","Q is not empty","$)$"))
        code.append(("u","$\leftarrow$","Q.dequeue","$($","$)$"))
        code.append(("u.color", "$\leftarrow$", "Red"))
        code.append(("$f$","$o$","$r$"," each v ","$\in$","G.adj","$($","$u$","$)$"))
        code.append(("if","$($" "v.color" ,"$==$","Black","$)$"))
        code.append(("v.color" ,"$\leftarrow$","Green"))
        code.append(("v.d" ,"$\leftarrow$","u.d + 1"))
        code.append(("v.prev" ,"$\leftarrow$","u"))
        code.append(("Q.enqueue","$($","$v$","$)$"))
        

        
        line = [None]*18
        linenumber = [None]*18
        surround = [None]*18
        for i in range(len(line)):
            line[i] = Tex(*[x for x in code[i]])
            line[i].scale(code_scale)
            line[i].set_color_by_tex_to_color_map(map)
            linenumber[i] = Tex(str(i+1))
            linenumber[i].scale(code_scale*0.6)

            if i == 0:
                linenumber[i].shift(np.array([-4,3.5,0])).to_edge(LEFT)
                line[i].shift(np.array([-4,3.5,0])).to_edge(LEFT).shift(RIGHT*0.5)
            elif i==3 or i==10 or i==12 or i==13:
                linenumber[i].align_to(linenumber[i-1],LEFT+DOWN).shift(DOWN*buffer).to_edge(LEFT)
                line[i].align_to(line[i-1],LEFT+DOWN).shift(DOWN*buffer).shift(RIGHT)

            elif i==6:
                linenumber[i].align_to(linenumber[i-1],LEFT+DOWN).shift(DOWN*buffer).to_edge(LEFT)
                line[i].align_to(line[i-1],DOWN).align_to(line[0],LEFT).shift(DOWN*buffer)
            else:
                linenumber[i].align_to(linenumber[i-1],LEFT+DOWN).shift(DOWN*buffer).to_edge(LEFT)
                line[i].align_to(line[i-1],LEFT+DOWN).shift(DOWN*buffer)
            surround[i]=SurroundingRectangle(linenumber[i],corner_radius=0.1,color=MAROON)
        


        # self.play(*[Write(x) for x in line],*[Create(x) for x in linenumber],*[Create(x) for x in surround])
        
        for x in line:
            self.play(Write(x))
            self.wait(0.5)

      

        tn = Tex("TIME COMPLEXITY : O(V + E)", color=RED, font_size=30)
        tn.move_to(3 * UP + 3* RIGHT)
        self.play(Write(tn))
        tn = Tex("Which is same as BFS Traversal", color=GREEN, font_size=25)
        tn.move_to(2.5 * UP + 3* RIGHT)
        self.play(Write(tn))

        self.wait(5)

        
        
         # Step 1: Display the heading "Time Complexity Analysis" in yellow at the top-left corner
       