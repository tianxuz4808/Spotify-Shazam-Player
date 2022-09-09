from Shazam import Shazam
import asyncio

if __name__ == "__main__":
    import record
    shazam = Shazam('testing.wav')
    asyncio.run(shazam.shazam())
