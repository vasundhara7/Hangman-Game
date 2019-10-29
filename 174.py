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
                        print(event)
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
