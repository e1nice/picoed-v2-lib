from picoed_v2_lib import *
from machine import Pin

button_a = Button(Gpio.BUTTON_A)
button_b = Button(Gpio.BUTTON_B)
music = Music(Pin(Gpio.BUZZER))

button_a.was_pressed()
button_b.was_pressed()

playlist = [["BA_DING", music.BA_DING],
            ["BADDY", music.BADDY],
            ["BIRTHDAY", music.BIRTHDAY],
            ["BLUES", music.BLUES],
            ["CHASE", music.CHASE],
            ["DADADADUM", music.DADADADUM],
            ["ENTERTAINER", music.ENTERTAINER],
            ["FUNERAL", music.FUNERAL],
            ["FUNK", music.FUNK],
            ["JUMP_DOWN", music.JUMP_DOWN],
            ["JUMP_UP", music.JUMP_UP],
            ["NYAN", music.NYAN],
            ["ODE", music.ODE],
            ["POWER_DOWN", music.POWER_DOWN],
            ["POWER_UP", music.POWER_UP],
            ["PRELUDE", music.PRELUDE],
            ["PUNCHLINE", music.PUNCHLINE],
            ["PYTHON", music.PYTHON],
            ["RINGTONE", music.RINGTONE],
            ["WAWAWAWAA", music.WAWAWAWAA],
            ["WEDDING", music.WEDDING]]

# Beethoven’s 5th Symphony
notes = ['r4:2', 'g', 'g', 'g', 'eb:8', 'r:2', 'f', 'f', 'f', 'd:8']
music.play(notes)

index = 0
print("Button A to play next tune; button B to end.")

while not button_b.was_pressed():
    if button_a.was_pressed():
        print(playlist[index][0])
        music.play(playlist[index][1])
        index += 1
        if index >= len(playlist):
            index = 0
        button_a.reset_presses()
