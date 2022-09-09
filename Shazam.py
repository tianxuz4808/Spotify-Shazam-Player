from Song import Song
from shazamio import Shazam
import asyncio

class Shazam:
    def __init__(self, audio_file) -> None:
        self.audio_file = audio_file
        pass

    async def shazam(self):
        shazam = Shazam()
        song = await shazam.recongnize_song(self.audio_file)
        print(song)

