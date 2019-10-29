import pygame as p
import random
import sys
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
dark_red=(170,0,0)
green=(0,255,0)
dark_green=(0,170,0)
blue=(0,0,255)
dark_blue=(0,0,170)
purple=(255,0,255)
dark_purple=(170,0,170)
yellow=(255,255,0)
dark_yellow=(170,170,0)
orange=(255,191,0)
dark_orange=(170,121,0)
color=((0,26,13))
category="Animals"
difficulty="Easy"
pi=3.141592653
random.seed()

def instructions():
        intro = True
        Bg = p.Surface((1280,720))
        Bg.fill(black)
        Bg = Bg.convert()
        screen.blit(Bg,(0,0))
        image=p.image.load('hng8.JPG')
        screen.blit(image,(0,0))
        intro = True
        while intro:
                for event in p.event.get():
                        print(event)
                        if event.type == p.QUIT:
                                p.quit()
                                quit()

                myfont = p.font.SysFont("None", 100)
                mytext = myfont.render('Instructions', True, white)
                mytext = mytext.convert_alpha()
                screen.blit(mytext,(850//2,100//2))

                myfont1 = p.font.SysFont("None", 40)
                mytext1 = myfont1.render('Hangman is a puzzle of letters. Your goal is to try to figure out the word.', True, white)
                mytext1 = mytext1.convert_alpha()
                screen.blit(mytext1,(300//2,400//2))
                mytext2 = myfont1.render('For this you have eight attempts to guess whether a letter belongs to the word or not', True, white)
                mytext2 = mytext2.convert_alpha()
                screen.blit(mytext2,(190//2,500//2))
                mytext3 = myfont1.render('There are several categories in Hangman and thousands of words to guess!!', True, white)
                mytext3 = mytext3.convert_alpha()
                screen.blit(mytext3,(300//2,600//2))
                mytext4 = myfont1.render('The game has a beautiful and fun design, in order to make the gameplay', True, white)
                mytext4 = mytext4.convert_alpha()
                screen.blit(mytext4,(300//2,700//2))
                mytext5 = myfont1.render('better and enjoyable to the player.', True, white)
                mytext5 = mytext5.convert_alpha()
                screen.blit(mytext5,(850//2,800//2))

                
                button_1("Play",500,500,250,50,dark_red,red,game_category)
                

                p.display.update()
                clock.tick(15)

def text_fields(msg):
        myfont = p.font.SysFont("None", 34)
        mytext = myfont.render(msg, True, (white))
        mytext = mytext.convert_alpha()
        return mytext

def icon():
        icon=p.image.load("k.jpg")
        p.display.set_caption("HANGMAN-Please Die")
        p.display.set_icon(icon)

############################################## WINDOW CREATION
p.init()
screen=p.display.set_mode((1280,720))
clock = p.time.Clock()

 ######################################## UPDATE ALL THE ENTERED ALPHABETS
dx=350
    for i in guess:
        m = myfont.render(i, True, (white))
        m = m.convert_alpha()
        screen.blit(m,(50,dx))
        dx+=25
    blitscreens(mytext,my,xt)
    counter+=1
                        ############################################################### UPDATE GAME SCREEN EACH FRAME
p.display.flip()

game_intro()
game_category()
game_difficulty()
game_loop()
p.quit()
quit()
        ################################################################### END OF GAME



