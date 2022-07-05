import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("Pygame")
    screen = pg.display.set_mode((800,600))

    tori_image = pg.image.load("fig/4.png")
    tori_rct = tori_image.get_rect()
    tori_rct.center = 700, 400
    screen.blit(tori_image, tori_rct)
    pg.display.update()


    clock.tick(0.2)

if __name__ ==  "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()