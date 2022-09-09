from MyShazam import MyShazam
import asyncio

if __name__ == "__main__":
    import record
    shazam = MyShazam('testing.wav')
    asyncio.run(shazam.shazam())
