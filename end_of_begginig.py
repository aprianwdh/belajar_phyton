import time
from threading import Thread
import sys
import os

os.system("cls")

print(10*'='+" END OF BEGGINING "+10*'=')

lyrics = [
    ("Just trust me, you'll be fine", 0.09),
    ("And when I'm back in Chicago, I feel it", 0.09),
    ("Another version of me, I was in it", 0.09),
    ("I wave goodbye to the end of beginning", 0.08),
    ("Goodbye, goodbye, goodbye, goodbye", 0.1)
]
delays = [0, 5.0, 11.0, 17.0, 20.8]

def animasi_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def liric_proses(lyric, delay, speed):
    time.sleep(delay)
    animasi_text(lyric, speed)

def menyanyikan_lagu():
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=liric_proses, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    menyanyikan_lagu()