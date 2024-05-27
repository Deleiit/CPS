import mouse
import os
import time

def detecter_cps():
    last_time = time.time()
    keystrokes = 0
    while True:
        if time.time() - last_time > 1:
            cps = keystrokes / (time.time() - last_time)
            print("CPS:", cps)
            if cps > 5:
                os.system("shutdown /s /t 1")
                break
            keystrokes = 0
            last_time = time.time()
        if mouse.is_pressed(button='right'):
            actions += 1

detecter_cps()