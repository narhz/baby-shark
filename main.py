import playsound as ps
import random
from time import sleep



while True:
    rand_time = random.randint(300, 3600)
    sleep(rand_time)

    ps.playsound('baby.mp3')