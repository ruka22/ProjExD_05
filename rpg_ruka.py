import pygame as pg
import sys

def main():
    pg.display.set_caption("RPG of くそげー")
    screen = pg.display.set_mode((1150, 650))
    clock  = pg.time.Clock()
    bg_img = pg.transform.rotozoom(pg.image.load("ex05/fig/back.png"), 0, 0.6)
    bgw, bgh = pg.display.get_surface().get_size()
    kk_img = pg.transform.rotozoom(pg.image.load("ex05/fig/suraimu.png"), 0, 0.5)
    box_imgs = [pg.transform.scale(pg.image.load("ex05/fig/box_big.jpg"), (bgw/5*3, 150)),
                pg.transform.rotozoom(pg.image.load("ex05/fig/box_choice.jpg"), 0, 0.6),
                pg.transform.rotozoom(pg.image.load("ex05/fig/box_status.jpg"), 0, 0.8)]
    fontos  = [pg.font.Font("ex05/font/JKG-L_3.ttf", 50),
               pg.font.Font("ex05/font/JKG-L_3.ttf", 40),]
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img,[0,0])
        screen.blit(kk_img,[bgw/2-50,bgh/2-50])
        screen.blit(box_imgs[0], [bgw/2-pg.Surface.get_width(box_imgs[0])/2, 10])  #すらいむがあらわれた
        screen.blit(box_imgs[1], [bgw/2-pg.Surface.get_width(box_imgs[1])/2, bgh-pg.Surface.get_height(box_imgs[1])-10]) #なにする？
        screen.blit(box_imgs[2], [10,200])     #すらいむステータス
        screen.blit(box_imgs[2], [bgw-pg.Surface.get_width(box_imgs[2])-10,bgh-pg.Surface.get_height(box_imgs[2])-10]) #勇者ステータス
        

        
        sras = [fontos[0].render("すらいむがあらわれた！", True, (255, 255, 255)),
                fontos[0].render("すらいむがしんだ", True, (255, 255, 255)),
                fontos[0].render("すらいむがなかまになった", True, (255, 255, 255)),
                fontos[1].render("すらいむ", True, (255, 255, 255))]
        sentaku = fontos[1].render("なにする？", True, (255, 255, 255))
        koudou = [fontos[1].render("@こーげき", True, (255, 255, 255)),
                  fontos[1].render("@ぼうぎょ", True, (255, 255, 255)),
                  fontos[1].render("@かいふく", True, (255, 255, 255)),
                  fontos[1].render("@ていむ", True, (255, 255, 255))]
        screen.blit(sras[2], [bgw/2-pg.Surface.get_width(sras[2])/2, 60])
        screen.blit(sentaku, [300, 450])  #なにする？
        screen.blit(koudou[0], [300,510])
        screen.blit(koudou[1], [300,570])
        screen.blit(koudou[2], [600,510])
        screen.blit(koudou[3], [600,570])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()