################################################### IMPORT STATEMENTS
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
################################################### DRAWING FUNCTIONS FOR HANGMAN
def Stage0(Bg):
        p.draw.line(Bg,white,(600,100),(600,70),5)
        p.draw.line(Bg,white,(600,70),(750,70),5)
        p.draw.line(Bg,white,(750,70),(750,470),5)
        p.draw.line(Bg,white,(650,470),(850,470),5)
        screen.blit(Bg,(0,0))
def Stage1(Bg):
        
        p.draw.circle(Bg,white,(600,150),50,5)
        #menu=True
        #time=p.time.get_ticks()
        p.draw.circle(Bg,white,(580,135),5,5)
        p.draw.circle(Bg,white,(620,135),5,5)
        p.draw.line(Bg,white,(585,160),(615,160),5)
        p.draw.arc(Bg,white,(585,145,30,30),pi,2*pi,5)
        screen.blit(Bg,(0,0))
        return
def Stage2(Bg):
        
        p.draw.line(Bg,white,(600,200),(600,330),5)
        p.draw.arc(Bg,white,(585,145,30,30),pi,2*pi,5)
        p.draw.line(Bg,color,(585,160),(615,160),5)
        screen.blit(Bg,(0,0))
        return
def Stage3(Bg):
        
        p.draw.line(Bg,white,(600,330),(550,420),5)        
        p.draw.line(Bg,color,(585,160),(615,160),5)
        p.draw.arc(Bg,color,(585,145,30,30),pi,2*pi,5)
        p.draw.line(Bg,white,(585,165),(615,165),5)       
        screen.blit(Bg,(0,0))
def Stage4(Bg):
        music_stage2()
        p.draw.line(Bg,white,(600,330),(650,420),5)
        p.draw.arc(Bg,color,(585,145,30,30),pi,2*pi,5)
        p.draw.line(Bg,color,(585,165),(615,165),5)
        p.draw.line(Bg,color,(585,160),(615,160),5)
        p.draw.circle(Bg,white,(600,165),10,5)
        screen.blit(Bg,(0,0))
def Stage5(Bg):
        p.draw.line(Bg,white,(600,240),(550,290),6)
        p.draw.line(Bg,color,(585,160),(615,160),5)
        p.draw.arc(Bg,color,(585,145,30,30),pi,2*pi,5)
        p.draw.line(Bg,color,(585,165),(615,165),5)
        p.draw.circle(Bg,color,(600,165),10,5)
        p.draw.arc(Bg,white,(585,158,30,30),pi/2,pi,5)
        p.draw.arc(Bg,white,(585,158,30,30),0,pi/2,5)
        screen.blit(Bg,(0,0))
def Stage6(Bg):
        
        music_stage3()
        p.draw.line(Bg,white,(600,240),(650,290),6)
        p.draw.circle(Bg,color,(580,135),5,5)
        p.draw.circle(Bg,color,(620,135),5,5)
        p.draw.arc(Bg,white,(560,120,30,30),3*pi/2,2*pi,5)
        p.draw.arc(Bg,white,(610,120,30,30),pi,3*pi/2,5)
        p.draw.line(Bg,color,(585,160),(615,160),5)
        p.draw.arc(Bg,color,(585,145,30,30),pi,2*pi,5)
        p.draw.line(Bg,color,(585,165),(615,165),5)
        p.draw.circle(Bg,color,(600,165),10,5)
        p.draw.arc(Bg,white,(585,158,30,30),pi/2,pi,5)
        p.draw.arc(Bg,white,(585,158,30,30),0,pi/2,5)
        screen.blit(Bg,(0,0))
def Stage7(Bg):
        p.draw.line(Bg,white,(600,150),(600,70),10)
        p.draw.line(Bg,white,(600,70),(750,70),10)
        p.draw.line(Bg,white,(750,70),(750,470),10)
        p.draw.line(Bg,white,(650,470),(850,470),10)
        p.draw.circle(Bg,white,(570,190),50,5)
        p.draw.line(Bg,white,(550,177),(560,187),5)
        p.draw.line(Bg,white,(560,177),(550,187),5)
        p.draw.line(Bg,white,(580,175),(590,185),5)
        p.draw.line(Bg,white,(590,175),(580,185),5)
        p.draw.line(Bg,white,(560,210),(580,210),5)
        p.draw.line(Bg,white,(600,200),(600,330),5)
        p.draw.line(Bg,white,(600,330),(550,420),5)
        p.draw.line(Bg,white,(600,330),(650,420),5)
        p.draw.line(Bg,white,(600,240),(550,290),6)
        p.draw.line(Bg,white,(600,240),(650,290),6)
        screen.blit(Bg,(0,0))
def backS(Bg,screen):
        Bg.fill(color)
        screen.blit(Bg,(0,0))

def music():
        p.mixer.music.load("intro.mp3")
        p.mixer.music.play(-1)

def music_stage1():
        p.mixer.music.load("Outlast.mp3")
        p.mixer.music.play(-1)
def music_stage2():
        p.mixer.music.load("out.mp3")
        p.mixer.music.play(-1)
def music_stage3():
        p.mixer.music.load("final.mp3")
        p.mixer.music.play(-1)

        

def icon():
        icon=p.image.load("k.jpg")
        p.display.set_caption("HANGMAN-Please Die")
        p.display.set_icon(icon)

############################################## WINDOW CREATION
p.init()
screen=p.display.set_mode((1280,720))
clock = p.time.Clock()

############################################## ICON AND TITLE CREATION
icon()
############################################## START MUSIC

############################################# MENU SCREEN TEXT DRAWING

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button_1(msg,x,y,w,h,ic,ac,action=None):
        mouse = p.mouse.get_pos()
        click = p.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
                p.draw.rect(screen, ac,(x,y,w,h))

                if click[0] == 1 and action != None:
                    action()
        else:
                p.draw.rect(screen, ic,(x,y,w,h))

        smallText = p.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)

def button_2(msg,x,y,w,h,ic,ac,action=None):
        mouse = p.mouse.get_pos()
        click = p.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
                p.draw.rect(screen, ac,(x,y,w,h))

                if click[0] == 1 and action != None:
                        global category
                        category = msg
                        action()
                        
        else:
                p.draw.rect(screen, ic,(x,y,w,h))

        smallText = p.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)


def button_3(msg,x,y,w,h,ic,ac,action=None):
        mouse = p.mouse.get_pos()
        click = p.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
                p.draw.rect(screen, ac,(x,y,w,h))

                if click[0] == 1 and action != None:
                    global difficulty
                    difficulty = msg
                    action()
        else:
                p.draw.rect(screen, ic,(x,y,w,h))

        smallText = p.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)

def quitgame():
        p.quit()
        quit()

def losing_screen(Bg,word):
        myfont = p.font.SysFont("None", 40)
        myi = myfont.render("GAME OVER! YOU ARE DEAD! WORD= "+word, True, (255,255,255))
        myi1 = myfont.render("Press C to Continue", True, white)
        myi = myi.convert_alpha()
        myi1 = myi1.convert_alpha()
        screen.blit(myi,(10,500))
        screen.blit(myi1,(10,550))
                                    ################################## DEATH SCREEN INTERACTION
        while True:
                for e in p.event.get():
                        if e.type==p.QUIT:
                                                #sys.exit()
                                p.quit()
                                quit()
                        if e.type==p.KEYDOWN and e.key==p.K_c:
                                game_intro()
                                game_category()
                                game_difficulty()
                                game_loop()
                p.display.flip()


def winning_screen(Bg):
        Bg.fill(black)
        Bg=Bg.convert()
        screen.blit(Bg,(0,0))
        p.display.flip()
        myfont = p.font.SysFont("None", 40)
        mytext = myfont.render('CONGRATULATIONS YOU WIN!', True, (255,255,255))
        mytext1 = myfont.render('Press C to Continue', True, (255,255,255))
        mytext = mytext.convert_alpha()
        mytext1 = mytext1.convert_alpha()
        screen.blit(mytext,(800//2,650//2))
        screen.blit(mytext1,(930//2,730//2))
        p.display.flip()

                                    
                                    ################################################### VICTORY PAGE INTERACTION
        while True:
                for e in p.event.get():
                        if e.type==p.QUIT:
                                                #sys.exit()
                                p.quit()
                                quit()
                        if e.type==p.KEYDOWN and e.key==p.K_c:
                                game_intro()
                                game_category()
                                game_difficulty()
                                game_loop()
                p.display.flip()        

def game_intro():
        music()
        intro = True
        Bg = p.Surface((1280,720))
        Bg.fill(black)
        Bg = Bg.convert()
        screen.blit(Bg,(0,0))
        image=p.image.load('hng1.JPG')
        '''p.image.load('limbo.JPG')'''
        screen.blit(image,(0,0))
        intro = True
        while intro:
                for event in p.event.get():
                        #print(event)
                        if event.type == p.QUIT:
                                p.quit()
                                quit()

                myfont = p.font.SysFont("None", 100)
                mytext = myfont.render('Hangman', True, white)
                mytext = mytext.convert_alpha()
                screen.blit(mytext,(900//2,400//2))

                button_1("Start New Game",500,300,250,50,dark_red,red,game_category)
                button_1("Instructions",500,400,250,50,dark_green,green,instructions)
                button_1("Exit",500,500,250,50,dark_blue,blue,quitgame)

                
                
                p.display.update()
                clock.tick(15)

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


def game_category():
        intro = True
        Bg = p.Surface((1280,720))
        Bg.fill(black)
        Bg = Bg.convert()
        image=p.image.load('hng7.JPG')
        screen.blit(image,(0,0))
        
        while intro:
                for event in p.event.get():
                        print(event)
                        if event.type == p.QUIT:
                                p.quit()
                                quit()

                myfont = p.font.SysFont("None", 100)
                mytext = myfont.render('Categories', True, white)
                mytext = mytext.convert_alpha()
                screen.blit(mytext,(900//2,180//2))

                button_2("Animals",500,240,250,50,dark_red,red,game_difficulty)
                button_2("Countries",500,320,250,50,dark_yellow,yellow,game_difficulty)
                button_2("Cartoons",500,400,250,50,dark_blue,blue,game_difficulty)
                button_2("Harry Potter",500,480,250,50,dark_purple,purple,game_difficulty)
                button_2("Marvel",500,560,250,50,dark_green,green,game_difficulty)
                button_2("Brands",500,640,250,50,dark_orange,orange,game_difficulty)

                p.display.update()
                clock.tick(15)


def game_difficulty():
        intro = True
        Bg = p.Surface((1280,720))
        Bg.fill(black)
        Bg = Bg.convert()
        screen.blit(Bg,(0,0))
        image=p.image.load('hng5.JPG')
        screen.blit(image,(0,0))
        while intro:
                for event in p.event.get():
                        print(event)
                        if event.type == p.QUIT:
                                p.quit()
                                quit()

                myfont = p.font.SysFont("None", 70)
                mytext = myfont.render('Difficulty', True, white)
                mytext = mytext.convert_alpha()
                screen.blit(mytext,(1000//2,40//2))


                button_3("Easy",500,100,250,50,dark_yellow,yellow,game_loop)
                button_3("Medium",500,200,250,50,dark_blue,blue,game_loop)
                button_3("Hard",500,300,250,50,dark_red,red,game_loop)

                
                p.display.update()
                clock.tick(15)

############################################ FUNCTION TO BLIT ALL THE TEXT FIELDS AFTER REFRESHING THE SCREEN
def blitscreens(mytext,my,xt):
        global dx
        screen.blit(mytext,(50,50))
        screen.blit(my,(50,200))
        screen.blit(xt,(50,300))
                     
def text_fields(msg):
        myfont = p.font.SysFont("None", 34)
        mytext = myfont.render(msg, True, (white))
        mytext = mytext.convert_alpha()
        return mytext

        
        
        
############################################# CREATING THE MAIN GAME SCREEN
def game_loop():
        

        mainloop=True
        Bg=p.Surface((1280,720))
        Bg.fill(color)
        Bg=Bg.convert()
        screen.blit(Bg,(0,0))
        ############################################ OBTAINING RANDOM WORD FROM WORDLIST
        FILE = "b.csv"
        file=open(FILE,'r')
        words=file.readlines()
        #print("Words:",words)
        for i in range(len(words)):
                if(category in words[i] and difficulty in words[i]):
                        i=i+random.randint(0,2)
                        t=words[i].split(",")
                        h=t[2]
                        word=h[0:len(h)-1]
                        break
        ############################################ FIRST TEXT FIELD
        
        mytext=text_fields("GUESS A LETTER")
        screen.blit(mytext,(50,50))
        ############################################ SECOND TEXT FIELD
        myfont = p.font.SysFont("None", 34)
        my = myfont.render('_ '*len(word), True, (white))
        my = my.convert_alpha()
        screen.blit(my,(50,200))
        ############################################ INITIALISING DX
        dx=350
        ############################################ THIRD TEXT FIELD
        
        xt=text_fields("GUESSED LETTERS:")
        screen.blit(xt,(50,300))
        ############################################ VARIABLES TO STORE GAME DATA
        correct_guess=[]
        counter=0
        guess=[]
        ############################################ THE MAIN GAME INTERACTION
        while mainloop:
            for event in p.event.get():
                if event.type==p.QUIT:
                        p.quit()
                        quit()
                if event.type==p.KEYDOWN:
                    if event.key==p.K_ESCAPE:
                        p.quit()
                        quit()
                    l=p.key.get_pressed() ###### RECEIVING DATA INPUT FROM KEYBOARD

                    for i in range(len(l)):
                        if l[i]==1:
                            if i>=256:
                                break
                            s=chr(i)
                            if s in guess:
                                break
                            ################################################################ DRAWING THE ENTERED ALPHABETS IN ORDER
                            myfont = p.font.SysFont("None", 34)
                            m = myfont.render(chr(i), True, (white))
                            m = m.convert_alpha()
                            screen.blit(m,(50,dx))
                            dx+=25
                            ################################################################ CHECK IF LETTER IS VALID AND FILL UP
                            guess.append(s)
                            if s in word:
                                w=word
                                my.fill(color)
                                screen.blit(my,(50,200))
                                correct_guess.append(s)
                                i=0
                                while i<len(w):
                                    if w[i] not in correct_guess:
                                        w=w[:i]+'_ '+w[i+1:]
                                        i+=1
                                    if w[i] in correct_guess:
                                        w=w[:i+1]+' '+w[i+1:]
                                        i+=1
                                    i+=1
                            ################################################################ UPDATE THE BLANKS
                                my = myfont.render(w, True, (white))
                                my = my.convert_alpha()
                                blitscreens(mytext,my,xt)
                            ################################################################ VICTORY CONDITION CHECK
                                if '_' not in w:
                                    winning_screen(Bg)    
                                    
                            ################################################################ IF WRONG LETTER
                            else:
                                d={0:Stage0,1:Stage1,2:Stage2,3:Stage3,4:Stage4,5:Stage5,6:Stage6,7:Stage7,8:backS}
                                if counter>=7: ######### IF YOU ARE DEAD
                                    mytext.fill(color)
                                    my.fill(color)
                                    xt.fill(color)
                                    blitscreens(mytext,my,xt)
                                    f=d[counter+1]
                                    f(Bg,screen)
                                    f=d[counter]
                                    f(Bg)
                                    losing_screen(Bg,word)
                                    
                                ############################################# DRAW THE STAGES BASED ON COUNTER
                                for i in range(counter+1):
                                    f=d[i]
                                    f(Bg)
                                p.display.flip()
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
