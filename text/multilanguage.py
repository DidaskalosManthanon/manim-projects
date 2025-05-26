from manim import *


class MultiLanguage(Scene):
    def construct(self):
        fr_01 = MarkupText("Bonjour Anna.", font="Zapfino").scale(0.5)
        fr_02 = MarkupText(
            "En guise de cadeau de Noël,",
            font="Zapfino"
        ).scale(0.5)
        fr_03 = MarkupText(
            "je vais t'apprendre la programmation Python.",
            font="Zapfino"
        ).scale(0.5)
        fr_04 = MarkupText(
            "De cette façon tu vas pouvoir créer ",
            font="Zapfino"
        ).scale(0.5)
        fr_05 = MarkupText("tes propres vidéos ", font="Zapfino").scale(0.5)
        fr_06 = MarkupText("grâce à la bibliothèque de code Manim.",
            font="Zapfino"
        ).scale(0.5)
        fr = [fr_01, fr_02, fr_03, fr_04, fr_05, fr_06]
        
        en_01 = MarkupText("Hello Anna.", font="American Typewriter")
        en_02 = MarkupText("As a Christmas gift, ", font="American Typewriter")
        en_03 = MarkupText(
            "I am going to teach you ",
            font="American Typewriter"
        )
        en_04 = MarkupText(
            "Python programming. This way, ",
            font="American Typewriter"
        )
        en_05 = MarkupText(
            "you will be able to create your own ",
            font="American Typewriter"
        )
        en_06 = MarkupText(
            "videos using the Manim code library.",
            font="American Typewriter"
        )
        en = [en_01, en_02, en_03, en_04, en_05, en_06]

        ru_01 = MarkupText("Привет, Анна.", font="sans-serif")
        ru_02 = MarkupText(
            "Качестве рождественского подарка ",
            font="sans-serif"
        )
        ru_03 = MarkupText(
            "я научу тебя программировать на Python.",
            font="sans-serif"
        )
        ru_04 = MarkupText(
            "Таким образом ты сможешь создавать ",
            font="sans-serif"
        )
        ru_05 = MarkupText("свои собственные видео ", font="sans-serif")
        ru_06 = MarkupText(
            "с помощью библиотеки кода Маним.",
            font="sans-serif"
        )
        ru = [ru_01, ru_02, ru_03, ru_04, ru_05, ru_06]

         
        for lang in [fr, en, ru]:
            lang[0] = lang[0].to_edge(UP)
            self.play(Write(lang[0]), run_time=3)
            for i in range(1, 6):
                lang[i] = lang[i].next_to(lang[i - 1], DOWN)
                self.play(Write(lang[i]), run_time=3)
            self.wait(2)
            if lang == ru:
                self.wait()
                break
            else: self.play(*[FadeOut(lang[i]) for i in range(6)])
        
                
