from manim import *


class Logo(Scene):
    def construct(self):

        # Change background color
        self.camera.background_color = GREEN_A
        
        # YouTube Logo
        YOUTUBE_RED = "#ff0033fc"
        rect = RoundedRectangle(
            width=5,
            height=3,
            corner_radius=0.5,
            color=YOUTUBE_RED,
            fill_opacity=1
        )

        
        # Bitcoin color
        BTC_YELLOW = "#F7931A"
        btc_logo = SVGMobject("./bitcoin-btc-logo.svg")

        FRENCH_BLUE = "#CE1126"
        FRENCH_RED = "#002654"
        name = MathTex(r"\textbf{Languages}").scale(3)\
            .set_color_by_gradient(FRENCH_RED, WHITE, FRENCH_BLUE)
        triangle = Triangle(color=WHITE, fill_opacity=1.0).scale(0.75)\
            .rotate(-PI/2)\
            .next_to(rect, DOWN, buff=-2.25)\
            .shift(RIGHT * 0.2)

        clap = Text(
            "CLAP"
        ).scale(1.5).set_color_by_gradient(FRENCH_RED, WHITE, FRENCH_BLUE)
        
        com = Text(
            "Commentez"
        ).scale(1.5).set_color_by_gradient(FRENCH_RED, WHITE, FRENCH_BLUE)
        
        like = Text(
            "Likez"
        ).scale(1.5).set_color_by_gradient(FRENCH_RED, WHITE, FRENCH_BLUE)
        # Like button
        #like_button_address = "./icons8-like-button-light/icons8-like-button-"
        #like_btn_adr24 = like_button_address + "24.png"
        like_btn = SVGMobject("./like-svg.svg").scale(0.35).to_edge(LEFT)
        
        sub = Text(
            "Abonnez-vous"
        ).scale(1.5).set_color_by_gradient(FRENCH_RED, WHITE, FRENCH_BLUE)
        sub_btn = ImageMobject("./sub.jpg").scale(0.5)
        
        share = Text(
            "Partagez"
        ).scale(1.5).set_color_by_gradient(FRENCH_RED, WHITE, FRENCH_BLUE)
        
        
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

        self.play(Write(name.next_to(rect, RIGHT)))
        self.wait(0.25)
         
        tri = Triangle().set_fill(opacity=1).set_z_index(2).scale(0.75).set_color(WHITE)
        always_rotate(tri, rate=2*PI, about_point=ORIGIN)
        self.add(tri)
        self.play(Write(clap.next_to(tri, RIGHT)))
        self.wait(0.25)
        
       
        self.play(
            Write(btc_logo.next_to(clap, DOWN + 4 * RIGHT))
        )
        

        self.play(
            Write(tri),
            Transform(clap[0], com.next_to(clap, DOWN + 5 * LEFT)),
            # Turn 1
            btc_logo.animate.rotate(2 * PI / 7).stretch_to_fit_height(2.5)
        )
        
        self.play(
            Transform(clap[1], like.next_to(com, DOWN)),
            # Turn 2
            btc_logo.animate.rotate(2 * PI / 7).stretch_to_fit_width(2.5)
        )
        self.play(
            like_btn.animate.to_edge(RIGHT),
            # Turn 3
            btc_logo.animate.rotate(2 * PI / 7).stretch_to_fit_height(3)
        )
        
        self.play(
            Transform(clap[2], sub.next_to(like, DOWN)),
            like_btn.animate.to_edge(LEFT),
            # Turn 4
            btc_logo.animate.rotate(
                2 * PI / 7
            ).stretch_to_fit_height(3).stretch_to_fit_width(3)
        )
        self.play(
            sub_btn.animate.next_to(clap[2], 2 * RIGHT),
            like_btn.animate.next_to(clap[1], 2 * RIGHT),
            # Turn 5
            btc_logo.animate.rotate(2 * PI / 7),
        )
        
        self.play(
            Transform(clap[3], share.next_to(sub, DOWN)),
            like_btn.animate.to_edge(RIGHT),
            # Turn 6
            btc_logo.animate.rotate(2 * PI / 7),
        )
        self.play(
            like_btn.animate.next_to(clap[1], 2 * LEFT),
            like_btn.animate.to_edge(LEFT),
            # Turn 7
            btc_logo.animate.rotate(
                2 * PI / 7
            ).shift(DOWN),
        )
        
        self.wait(0.25)
