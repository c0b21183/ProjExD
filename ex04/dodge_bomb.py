import pygame as pg
import sys
import random
import pygame.mixer 

def sound():                                          #追加機能BGM
    pygame.mixer.init(frequency = 44100)
    pygame.mixer.music.load("fig/MusMus-BGM-128.mp3")
    pygame.mixer.music.play(1)

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600,900)) #Surface 
    screen_rct = screen_sfc.get_rect() #Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg") #Surface
    bgimg_rct = bgimg_sfc.get_rect() #Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct) #Surface

     
    kkimg_sfc = pg.image.load("fig/4.png")  #Surface
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)  #Surface 
    kkimg_rct = kkimg_sfc.get_rect() #Rect
    kkimg_rct.center = 900, 400
    kkimg_rct.centerx = random.randint(0, screen_rct.width)
    kkimg_rct.centery = random.randint(0, screen_rct.height)
    vx3, vy3 = +3, +3

    bmimg_sfc = pg.Surface((50,50)) #Surface
    bmimg_sfc.set_colorkey((0, 0, 0)) 
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (25,25), 25)
    bmimg_rct = bmimg_sfc.get_rect() #Rect
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = random.randint(0, screen_rct.height)
    vx, vy = +1, +1

    bmimg2_sfc = pg.Surface((20,20)) #Surface 
    bmimg2_sfc.set_colorkey((0, 0, 0)) 
    pg.draw.circle(bmimg2_sfc, (100, 30, 100), (10,10), 10)
    bmimg2_rct = bmimg2_sfc.get_rect() #Rect
    bmimg2_rct.centerx = random.randint(0, screen_rct.width)
    bmimg2_rct.centery = random.randint(0, screen_rct.height)
    vx2, vy2 = +2, +2

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct) 
        for event in pg.event.get():
            if event.type == pg.QUIT: return


        key_states = pg.key.get_pressed()#辞書
        if key_states[pg.K_UP] == True: kkimg_rct.centery -= 2
        if key_states[pg.K_DOWN] == True: kkimg_rct.centery += 2
        if key_states[pg.K_LEFT] == True: kkimg_rct.centerx -= 2
        if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx += 2
        if check_bound(kkimg_rct, screen_rct) != (1, 1):#領域外だったら
            if key_states[pg.K_UP] == True: kkimg_rct.centery += 2
            if key_states[pg.K_DOWN] == True: kkimg_rct.centery -= 2
            if key_states[pg.K_LEFT] == True: kkimg_rct.centerx += 2
            if key_states[pg.K_RIGHT] == True: kkimg_rct.centerx -= 2

        screen_sfc.blit(kkimg_sfc, kkimg_rct) 
        yoko, tate = check_bound(kkimg_rct, screen_rct) #追加機能
        vx3 *= yoko
        vy3 *= tate

        bmimg_rct.move_ip(vx, vy)
        bmimg2_rct.move_ip(vx2, vy2)
        kkimg_rct.move_ip(vx3, vy3)

        screen_sfc.blit(bmimg_sfc, bmimg_rct) 
        yoko, tate = check_bound(bmimg_rct, screen_rct)
        vx *= yoko
        vy *= tate

        screen_sfc.blit(bmimg2_sfc, bmimg2_rct) #追加機能
        yoko, tate = check_bound(bmimg2_rct, screen_rct)
        vx2 *= yoko
        vy2 *= tate

        if kkimg_rct.colliderect(bmimg_rct): 
            return
        if kkimg_rct.colliderect(bmimg2_rct): 
            return

        pg.display.update()
        clock.tick(1500)


def check_bound(rct, scr_rct): #rect:こうかとん or 爆弾のRect
                               #scr_rct:スクリーンのRect

    yoko, tate = +1, +1 
    if rct.left < scr_rct.left or scr_rct.right < rct.right:yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom:tate = -1
    return yoko, tate


if __name__ ==  "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
