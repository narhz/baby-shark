from playsound import playsound
import random
from time import sleep



while True:
    rand_time = random.randint(300, 3600)
#    sleep(rand_time)

    playsound('baby.mp3')