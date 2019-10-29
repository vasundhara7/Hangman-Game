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
        
################################################################ DRAWING THE ENTERED ALPHABETS IN ORDER
myfont = p.font.SysFont("None", 34)
m = myfont.render(chr(i), True, (white))
m = m.convert_alpha()
screen.blit(m,(50,dx))
dx+=25
