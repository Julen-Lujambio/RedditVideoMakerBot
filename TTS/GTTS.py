import random

from gtts import gTTS

from utils import settings

from pydub import AudioSegment



class GTTS:
    def __init__(self):
        self.max_chars = 5000
        self.voices = []

    def adjust_speed(self, filepath, speed_ratio=1.25):
        # Get the audiosegment from the file
        orig_mp3_obj = AudioSegment.from_file(filepath)
        # Speed it up
        speed_update = orig_mp3_obj.speedup(speed_ratio)
        # Overwrite original file with new mp3
        speed_update.export(filepath, format="mp3")

    def run(self, text, filepath):
        tts = gTTS(
            text=text,
            lang=settings.config["reddit"]["thread"]["post_lang"] or "en",
            slow=False,
        )
        tts.save(filepath)
        self.adjust_speed(filepath)




    def randomvoice(self):
        return random.choice(self.voices)
