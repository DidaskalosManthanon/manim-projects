from manim import *
import pygments.styles as code_styles
from manim_voiceover import VoiceoverScene

from manim_voiceover.services.azure import AzureService

code_style = code_styles.get_style_by_name("one-dark")



class VoiceoverDemo(VoiceoverScene):
    def construct(self):
        # Initialize speech synthesis using Azure's TTS API
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newcast-casual", # global_speed=1.15
            )
        )
        banner = ManimBanner().scale(0.5)

        with self.voiceover(text="Hey Manim Community!"):
            self.play(
                banner.create(),
            )

        tracker = self.add_voiceover_text(
            "Today, I want to show you how you can generate voiceovers directly in your Python code."
        )

        self.play(banner.expand())
        self.wait(tracker.get_remaining_duration(buff=-1))
        self.play(FadeOut(banner))

        demo_code = Code(
            
        )
