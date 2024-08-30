import pygame as pg
import sys

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption("rolety")
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

            exit()

    screen.fill("grey")
    pg.display.flip()
    clock.tick(60)
    

