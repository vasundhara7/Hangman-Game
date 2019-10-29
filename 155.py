def Stage0(Bg):
        p.draw.line(Bg,white,(600,100),(600,70),5)
        p.draw.line(Bg,white,(600,70),(750,70),5)
        p.draw.line(Bg,white,(750,70),(750,470),5)
        p.draw.line(Bg,white,(650,470),(850,470),5)
        screen.blit(Bg,(0,0))
def Stage1(Bg):
        
        p.draw.circle(Bg,white,(600,150),50,5)
        menu=True
        time=p.time.get_ticks()
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

############################################# DRAW THE STAGES BASED ON COUNTER
for i in range(counter+1):
        f=d[i]
        f(Bg)
        p.display.flip()
                                
