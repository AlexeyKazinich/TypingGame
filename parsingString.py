import pygame as pg
pg.init()

def mainScreen():
    screen = pg.display.set_mode((640,480))
    area = screen.get_rect()
    font = pg.font.Font(None,32)
    clock = pg.time.Clock()

    #text stuff
    Text = "This is a sentence or a text."
    TextArray = Text.split()
    TextLength = len(TextArray)
    
    #colors
    color_active = pg.Color('dodgerblue2')
    color_success = pg.Color(0,255,0)
    color_wrong = pg.Color(255,0,0)
    screen.fill((30,30,30))


    #conditionals
    done = False
    i = 0
    
    #location
    current_x = 0 #horizontal location of the word
    typed = 0 #word counter
    

    #Statics for the input box where the user writes the words
    input_box = pg.Rect(round(area.width/2-100), area.height-50, 30, 30)
    typedWord = "" #the word in the textbox
    color_active = pg.Color('dodgerblue2')
    inputBox_color = color_active

    while not done:      


        if i < TextLength:
            currentWord = TextArray[i]
            currentWordList = list(currentWord)
            typedWordList = list(typedWord)
            i += 1
            if(i <= typed):
                text_width, text_height = font.size(currentWord)
                Word_surface = font.render(str(currentWord),True,color_success)
                screen.blit(Word_surface,(current_x+10,150))
                current_x += text_width + 10
            
            else:
                text_width, text_height = font.size(currentWord)
                Word_surface = font.render(str(currentWord),True,color_active)
                screen.blit(Word_surface,(current_x+10,150))
                current_x += text_width + 10
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_BACKSPACE:
                    typedWord = typedWord[:-1]
                    i = 0
                    current_x = 0
                    screen.fill((30,30,30))

                elif event.key == pg.K_SPACE:
                    if typedWord == str(TextArray[typed]):
                        typed += 1
                        current_x = 0
                        screen.fill((30,30,30))
                        i = 0
                        typedWord = ""
                    
                    else:
                        current_x = 0
                        i = 0
                        screen.fill((30,30,30))
                        inputBox_color = color_wrong
                        typedWord = ""
                    
                else:
                    typedWord += event.unicode
                    inputBox_color = color_active
                    
                    
        if(typedWordList[len(typedWord)] != currentWordList[len(typedWord)]):
            inputBox_color = color_wrong
        else:
            inputBox_color = color_success
        
        if typed == TextLength:
            typed = 0
            screen.fill((30,30,30))
            i = 0


        #inputbox
        txt_surface = font.render(typedWord,True,inputBox_color)
        input_box.width = max(200,txt_surface.get_width()+10)
        input_box.x = round(area.width/2) - round(input_box.width/2)
        screen.blit(txt_surface,(input_box.x+5,input_box.y+5))
        pg.draw.rect(screen,inputBox_color,input_box,2)
        pg.display.flip()
        clock.tick(400)


running = True
while running:
    mainScreen()