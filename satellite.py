import pgzrun
from random import randint
from time import time
WIDTH=700
HEIGHT=600
TITLE='Connecting Satllites'
satellites=[]
lines=[]
start_time=0
total_time=0
end_time=0


next_satellites=0
number_satellite=8

def create_satellite():
    global start_time
    for count in range(number_satellite):
        satellite=Actor('satellite')
        satellite.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        satellites.append(satellite)
        start_time=time()

def draw():
    screen.clear()
    screen.fill('blueviolet')
    number=1
    for satellite in satellites:
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        number+=1
    total_time=time()-start_time
    screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

create_satellite()












pgzrun.go()