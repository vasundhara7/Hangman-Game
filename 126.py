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

                            
