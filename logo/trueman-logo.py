from manim import *


class Logo(Scene):
    def construct(self):

        # YouTube Logo
        YOUTUBE_RED = "#ff0033fc"

        # Bitcoin color
        BTC_YELLOW = "#F7931A"
        btc_logo = SVGMobject("./bitcoin-btc-logo.svg")
        
        rect = RoundedRectangle(
            width=5,
            height=3,
            corner_radius=0.5,
            color=YOUTUBE_RED,
            fill_opacity=1
        )
        name = MathTex(r"\textbf{TrueMan}").scale(3)\
            .set_color(BTC_YELLOW)
        triangle = Triangle(color=WHITE, fill_opacity=1.0).scale(0.75)\
            .rotate(-PI/2)\
            .next_to(rect, DOWN, buff=-2.25)\
            .shift(RIGHT * 0.2)

        clap = Text(
            "CLAP"
        ).scale(1.5).set_color(BTC_YELLOW)
        com = Text(
            "Commentez"
        ).scale(1.5).set_color(BTC_YELLOW)
        like = Text(
            "Likez"
        ).scale(1.5).set_color(BTC_YELLOW)
        sub = Text(
            "Abonnez-vous"
        ).scale(1.5).set_color(BTC_YELLOW)
        share = Text(
            "Partagez"
        ).scale(1.5).set_color(BTC_YELLOW)
        
        
        self.play(
            Create(rect),
            FadeIn(triangle),
            run_time=0.5
        )

        self.wait()

        group = VGroup(rect, triangle)

        self.play(
            group.animate.shift(1.75 * UP + LEFT * 4.25),
            run_time=0.5
        )

        self.play(Write(name.next_to(rect, 1.25 * RIGHT)))
        self.wait(0.25)
        
        self.play(Write(clap.next_to(name, DOWN)))
        self.wait(0.25)
        
        self.play(
            Transform(clap[0], com.next_to(clap, DOWN + 5 * LEFT))
        )
        
        self.play(
            Transform(clap[1], like.next_to(com, DOWN))
        )
        
        self.play(
            Transform(clap[2], sub.next_to(like, DOWN))
        )
        self.play(Write(btc_logo.next_to(sub, 3 * RIGHT)))
        
        self.play(
            Transform(clap[3], share.next_to(sub, DOWN))
        )
        self.play(btc_logo.animate.shift(3 * RIGHT))
        self.wait(0.25)
        
