import hub,utime
# import spike
# from spike.control import wait_for_seconds

A = 440
B = 494
Cis = 554
D = 587
E = 659
Fis = 698
hub.sound.volume(10)

notes = [A,   B,   Cis, D,   E,   Fis]
time  = [500, 500, 100, 200, 300, 1000]

hub.sound.beep(B, 500, 1)
# for i in range (1, 3):
#     hub.sound.beep(A, 500, 3)
#     wait_for_seconds(1)

for i in range(len(notes)):
    # hub.sound.beep(A, 1000, 1)
    hub.sound.beep(notes[i], time[i], 1) # note, time (ms), sinewave
