from manim import *

class FirstScene(Scene): # All classes that animate are a subclass of scene
        def construct(self):
                """
                All the animation code must lie within construct method.
                This method is invoked by manim.py
                """
                dot = Dot() # creating circle object
                self.add(dot) # adding that circle object to the scene
                dot.set_color(RED)
                equation = Tex('$x\\in \\mathbb{K}$')
                equation.shift(3*UP)
                equation.shift(3*LEFT)
                equation2 = Tex('$x\\in \\mathbb{R}$')
                equation2.shift(3*UP)
                equation2.shift(3*LEFT)
                self.play(Write(equation))



                self.play(ReplacementTransform(equation, equation2))
                valorsc = Tex('$x = 1$').next_to(equation, DOWN)
                self.play(Write(valorsc))
                valorsc2 = Tex('$x = -1$').next_to(equation, DOWN)

                dot2 = Dot(color=BLUE)
                self.play(ReplacementTransform(valorsc, valorsc2),Transform(dot,dot2))
                self.wait(2) # waiting for two second ~ time.sleep(2)

                valorsc3 = Tex('$x = 2$').next_to(equation, DOWN)
               
                dot3 = Dot(color=RED, radius=0.16)
                self.play(ReplacementTransform(valorsc2, valorsc3),Transform(dot2,dot3))
                self.wait(2) # waiting for two second ~ time.sleep(2)
                valorsc4 = Tex('$x = -2$').next_to(equation, DOWN)
               
                dot4 = Dot(color=BLUE, radius=-0.16)
                self.play(ReplacementTransform(valorsc3, valorsc4),Transform(dot3,dot4))
                self.wait(2) # waiting for two second ~ time.sleep(2)
#                self.play(dot.animate.set_color(RED)) 
                self.wait(2) # waiting for two second ~ time.sleep(2)


class scene2(ThreeDScene): # All classes that animate are a subclass of scene
        def construct(self):
            ## esta cosa busca ilustrar el algebra de vectores 

                ### definimos un vector en un espacio bidimensional
                equation = Tex('$v\\in \\mathbb{K}^2$')
                equation.shift(3.5*UP)
                equation.shift(4*LEFT)
                equation2 = Tex('$v\\in \\mathbb{R}^2$')
                equation2.shift(3.5*UP)
                equation2.shift(3.5*LEFT)
                self.play(Write(equation))

                ## dibujamos la base
                b1 = Tex('$e_1$')
                b1.shift(3.5*UP)
                b1.shift(3.5*RIGHT)
                b1.set_color(GREEN)
                b2 = Tex('$e_2$').next_to(b1,RIGHT)
                b2.set_color(PURPLE)

                self.play(ReplacementTransform(equation, equation2))
                
                vec = Vector([1,0])
                e1 = Vector([1,0]).set_color(GREEN)
                self.play(Write(b1),Write(e1))


                e2 = Vector([0,1]).set_color(PURPLE)
                self.play(Write(b2),Write(e2))

                self.wait(2) # waiting for two second ~ time.sleep(2)

                ## y un vector arbitrario
                valorsc = Tex('$v = \\lambda e_1 + \\alpha e_2$').next_to(equation, DOWN)
                self.play(Write(valorsc))
                vec2 = Arrow([0,0,0],[2,2,0],buff=0)
                vec2.set_color(RED)
                self.play(ReplacementTransform(vec, vec2))
                self.wait(2) # waiting for two second ~ time.sleep(2)

                ## mostramos el vector con igual aspecto y magnitud pero signo opuesto
                # que claro, es el inverso aditivo 
                vec3 = Vector([1,0])
                valorsc2 = Tex('$-v = -\\lambda e_1 - \\alpha e_2$').next_to(valorsc, DOWN)
                self.play(Write(valorsc2))
                vec4 = Vector([-2,-2])
                vec4.set_color(BLUE)
                self.play(ReplacementTransform(vec3, vec4))
                self.wait(2) # waiting for two second ~ time.sleep(2)

                valorsc3 = Tex('$w = \\gamma e_1 + \\beta e_2$').next_to(valorsc, DOWN)
                vec5 =Arrow([0,0,0],[1.3,0.5,0],buff=0) 
                vec5.set_color(RED)
                self.play(ReplacementTransform(vec4,vec5), ReplacementTransform(valorsc2, valorsc3))

                
                self.wait(2) # waiting for two second ~ time.sleep(2)

                # dibujamos la suma de los vectores
                vec6=Arrow([2,2,0],[3.3,2.5,0],buff=0)
                vec6.set_color(RED)
                valorsc4 = Tex('$v+w = (\\lambda + \\gamma) e_1 + (\\alpha+ \\beta) e_2$').next_to(valorsc3, DOWN)
                self.play(Write(valorsc4))
                self.play(ReplacementTransform(vec5,vec6))
                vec7=Arrow([0,0,0],[3.3,2.5,0],buff=0)
                vec7.set_color(RED)
                self.play(Write(vec7))


                self.wait(2)

                self.play(FadeOut(vec7, valorsc4))

                ## dibujamos el producto punto de vectores



                vec8=Arrow([0,0,0],[3,0,0],buff=0)
                vec8.set_color(RED)
                vec9=Arrow([0,0,0],[2,3,0],buff=0)
                vec9.set_color(RED)
                self.play(ReplacementTransform(vec6,vec8),ReplacementTransform(vec2,vec9), ReplacementTransform(valorsc2, valorsc3))
                valorsc5 = Tex('$v\\cdot w = \\lambda  \\gamma e_1 \cdot e_1 + \\alpha \\beta e_2 \cdot e_2+ \\lambda \\beta e_1 \\cdot e_2 + \\gamma \\alpha e_2 \cdot e_1$').next_to(valorsc3, DOWN)
                valorsc5.shift(2*RIGHT)
                angle = Angle(vec8, vec9, radius=1)
                self.play(Write(valorsc5), Write(angle))
                self.wait(2)
                valorsc6 = Tex('$v\\cdot w = \\lambda  \\gamma  + \\alpha \\beta =|v||w|cos\\theta$').next_to(valorsc3, DOWN)
                self.play(ReplacementTransform(valorsc5, valorsc6))
                self.play(FadeOut(angle, vec9))

                points=[]
                count = 0
                for i in range(10):
                        for j in range(5):
                                x_coord = -3 + i*0.75
                                y_coord = -1.25 + j*0.75
                                point = np.array([x_coord, y_coord,0])
                                if(count==0):
                                        points = point
                                else:
                                        points = np.vstack((points,point))
                                        count += 1
                                if(x_coord>0):
                                        self.play(Write(Dot(point, color=rgb_to_color([np.arctan(x_coord)*2/np.pi,0,0]), radius = x_coord*0.03)))
                                else:
                                        self.play(Write(Dot(point, color=rgb_to_color([0,0,np.arctan(-1*x_coord)*2/np.pi]), radius=x_coord*0.03)))                                        
                self.wait(2)
