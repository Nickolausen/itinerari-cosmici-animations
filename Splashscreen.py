from manim import *
from random import *

class Splashscreen(Scene):
    def construct(self):
        galaxy = ImageMobject("./galaxy.png").set_opacity(.3).scale_to_fit_width(self.camera.frame_width).scale_to_fit_height(self.camera.frame_height)
        title = Tex(r"$\mathbb{I}$\textsc{tinerari} $\mathbb{C}$\textsc{osmici}").scale(2)
        subtitle = Tex(r"Un viaggio ai confini dell'Universo").next_to(title, DOWN, .3)
        logo = ImageMobject("./logo_bp.png").scale(.25).next_to(title, UP, .3).set_color(WHITE)

        max_width = self.camera.frame_width
        max_height = self.camera.frame_height

        stars = VGroup()
        stars_target = VGroup()

        for _ in range(0,15):
            random_x = randint(-int(max_width/2)*2, -int(max_width/2))
            random_y = randint(int(max_height), int(max_height) * 2)
            random_length = randint(1, 6)

            star = Line(
                start=[random_x, random_y, 0], 
                end=[random_x + random_length, random_y - random_length, 0])
            star.set_opacity(.5) 

            star_target = Line(
                start=[random_x, random_y, 0], 
                end=[random_x + (random_length*100), random_y - (random_length*100), 0])
            star_target.set_opacity(0)

            stars.add(star)
            stars_target.add(star_target)

        dots = VGroup()
        for _ in range(0, 80):
            random_x = (random() * max_width) - (max_width * .5)
            random_y = (random() * max_height) - (max_height * .5)
            
            dot = Dot(point=[random_x, random_y, 0], radius=(random() * DEFAULT_DOT_RADIUS) + 0.01)
            dot.set_opacity(randint(20, 50) * .01)
            dots.add(dot)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.play(FadeIn(logo))

        for dot in dots:
            self.play(FadeIn(dot))

        idx = 0
        for star in stars:
            self.play(FadeIn(star))
            self.play(MoveAlongPath(star, stars_target[idx]), run_time=2)
            self.play(FadeOut(star))

            idx += 1

        self.play(Unwrite(title))
        self.play(Unwrite(subtitle))
        self.play(FadeOut(logo))

        self.play(FadeOut(dots))