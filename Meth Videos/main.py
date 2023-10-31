from manim import *


class MatchingEquationParts(Scene):
    def construct(self):
        eq1 = MathTex(
            r"\dfrac{d^2x}{dt^2}", "+", "{ga^2", r"\over", "x^2}", "=", "0")
        eq2 = MathTex(
            r"\dfrac{d^2x}{dt^2}", "=", "-", "{ga^2", r"\over", "x^2}")
        eq3 = MathTex(
            "2", r"\dfrac{dx}{dt}", r"\dfrac{d^2x}{dt^2}", "=", "-", " 2", r" \dfrac{dx}{dt}", "{ga^2", r"\over", "x^2}")
        eq4 = MathTex(
            "\displaystyle\int", "2", r"\dfrac{dx}{dt}", r"\dfrac{d^2x}{dt^2}", "dt", "=", "-", " \displaystyle\int", " 2", r" \dfrac{dx}{dt}", "{ga^2", r"\over", "x^2}", " dt")
        eq5 = MathTex(
            "2", "\displaystyle\int", r"\dfrac{dx}{dt}", r"\dfrac{d^2x}{dt^2}", "dt", "=", "-", " 2", " \displaystyle\int", r" \dfrac{dx}{dt}", "{ga^2", r"\over", "x^2}", " dt")

        self.play(Write(eq1))
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(1)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(1)
        self.play(eq5.animate.scale(0.8).to_corner(UL))
        self.wait(0.5)
        self.play(FadeToColor(eq5[1:5], YELLOW))
        self.wait(1)
        let = MathTex(r"\text{Let }", "u", "=", r"\dfrac{dx}{dt}",
                      r"\text{, then }", "du", "=", r"\dfrac{d^2x}{dt^2}", r"dt")
        let.scale(0.8).next_to(eq5, DOWN).align_to(eq5, LEFT)
        self.play(Write(let))
        eq6 = MathTex("\displaystyle\int",
                      r"\dfrac{dx}{dt}", r"\dfrac{d^2x}{dt^2}", "dt")
        eq6.set_color(WHITE).scale(0.8).move_to(eq5[1:5].get_center())
        self.wait(1)
        self.play(eq6.animate.next_to(let, DOWN).align_to(let, LEFT))
        eq7 = MathTex("\displaystyle\int", r"u", "du")
        eq7.scale(0.8).move_to(eq6).align_to(eq6, LEFT)
        self.wait(1)
        self.play(TransformMatchingTex(eq6, eq7))
        self.wait(0.5)
        eq7_1 = MathTex("= ", r"\dfrac{1}{2}u^2")
        eq7_1.scale(0.8).next_to(eq7, RIGHT).align_to(eq7, DOWN)
        self.play(Write(eq7_1))
        eq8 = MathTex(
            "2", "\cdot", r"\dfrac{1}{2}u^2", "=", "-", " 2", " \displaystyle\int", r" \dfrac{dx}{dt}", "{ga^2", r"\over", "x^2}", " dt")
        eq8.scale(0.8).move_to(eq5).align_to(eq5, LEFT)
        self.wait(1)
        self.play(AnimationGroup(TransformMatchingTex(
            Group(eq5, eq7_1), eq8), FadeOut(eq7), let.animate.to_corner(UR)))
        eq9 = MathTex(
            r"u^2", "=", "-", " 2", " \displaystyle\int", r" \dfrac{dx}{dt}", "{ga^2", r"\over", "x^2}", " dt")
        eq9.scale(0.8).move_to(eq8).align_to(eq8, LEFT)
        self.wait(1)
        self.play(TransformMatchingTex(eq8, eq9))
        let_1 = MathTex(r"\dfrac{dx}{dt}")
        let_1.scale(0.8).move_to(let[3]).align_to(let[3], DOWN)
        self.wait(1)
        eq10 = MathTex(
            r"\bigg(", r"\dfrac{dx}{dt}", r"\bigg)^2", "=", "-", " 2", " \displaystyle\int", r" \dfrac{dx}{dt}", "{ga^2", r"\over", "x^2}", " dt")
        eq10.scale(0.8).move_to(eq9).align_to(eq9, LEFT)
        self.play(AnimationGroup(TransformMatchingTex(
            Group(eq9, let_1), eq10), FadeOut(let)))
        self.wait(0.5)
        self.play(eq10.animate.move_to(ORIGIN).scale(1.25))
        self.play(eq10[6:].animate.set_color(YELLOW))
        self.wait(1)
        eq11 = MathTex(
            r"\bigg(", r"\dfrac{dx}{dt}", r"\bigg)^2", "=", "-", " 2", " \displaystyle\int", "{ga^2", r"\over", "x^2}", r" \dfrac{dx}{dt}", " dt")
        eq11[6:].set_color(YELLOW)
        self.play(TransformMatchingTex(eq10, eq11))
        self.wait(1)
        eq12 = MathTex(
            r"\bigg(", r"\dfrac{dx}{dt}", r"\bigg)^2", "=", "-", " 2", " \displaystyle\int", "{ga^2", r"\over", "x^2}", " dx")
        eq12[6:].set_color(YELLOW)
        self.play(TransformMatchingTex(eq11, eq12))
        self.wait(1)
        eq13 = MathTex(
            r"\bigg(", r"\dfrac{dx}{dt}", r"\bigg)^2", "=", "-", " 2", "ga^2", " \displaystyle\int", "{1", r"\over", "x^2}", " dx")
        eq13[6:].set_color(YELLOW)
        self.play(TransformMatchingTex(eq12, eq13))
        self.wait(1)
        eq14 = MathTex(
            r"\bigg(", r"\dfrac{dx}{dt}", r"\bigg)^2", "=", "-", " 2", "ga^2", " \displaystyle\int", r"x^{-2}", " dx")
        eq14[6:].set_color(YELLOW)
        self.play(TransformMatchingTex(eq13, eq14))
        self.wait(1)
        eq15 = MathTex(
            r"\bigg(", r"\dfrac{dx}{dt}", r"\bigg)^2", "=", "-", " 2", "ga^2", "\left(-", r"{1", r"\over", "x}", r"\right)", "+", "C")
        eq15[6:].set_color(YELLOW)
        self.play(TransformMatchingTex(eq14, eq15))
        self.wait(1)
        eq16 = MathTex(
            r"\bigg(", r"\dfrac{dx}{dt}", r"\bigg)^2", "=", r"{2ga^2", r"\over", "x}", "+", "C")
        self.play(TransformMatchingTex(eq15, eq16))
        self.wait(1)
