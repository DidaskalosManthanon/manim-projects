from manim import *



class GradientImageFromArray(Scene):
    def construct(self):
        n = 256
        imageArray = np.uint8(
            [[i * 256 / n for i in range(0, n)] for _ in range(0, n)]
        )
        image = ImageMobject(imageArray).scale(2)
        self.play(FadeIn(image))
        self.wait()
        image.background_rectangle = SurroundingRectangle(image, GREEN)
        self.play(Write(image.background_rectangle))
        self.wait()
