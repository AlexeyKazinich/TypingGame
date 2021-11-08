import pygame as pg
from stopwatch import Stopwatch
from nltk.corpus import words
from random import randrange
import sys, random, math, time
import pickle
from os import path
#PROBLEMS#
#BAD FPS
#LINE 732 cant multiply sequence by non-int of type 'float'


pg.init()
#Dictionary = words.words()
Dictionary = pickle.load(open("SAVE_DATA/Data/MyDictionary.txt","rb")) #file which contains all the words for the tpying game

cSec = 0
cFrame = 0
FPS = 0
def count_fps():
    global cSec, cFrame, FPS, deltatime

    if cSec == time.strftime("%S"):
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS

def settingsScreen():
    screen = pg.display.set_mode((640,480))
    area = screen.get_rect()
    clock = pg.time.Clock()

    #statics
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    font = pg.font.Font(None,32)
    font_fps = pg.font.Font(None,12)

    #buttons#

    #back button
    back_button = pg.Rect(0,0,150,32)
    back_button_color = color_inactive
    back_button_txt = 'back'
    color_fps = pg.Color(0,255,0) #BRIGHT GREEN

    #Resolution box

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            
            elif event.type == pg.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    done = True
        screen.fill((30,30,30))

        #render the texts
        back_button_txt_Surface = font.render(back_button_txt,True,back_button_color)

        #blit the text
        screen.blit(back_button_txt_Surface,(back_button.x+5,back_button.y+5))

        #blit the buttons
        pg.draw.rect(screen,back_button_color,back_button,2)

        #FPS COUNTER
        FPS_counter_surface = font_fps.render(str(math.floor(FPS))+"FPS",True,color_fps)
        screen.blit(FPS_counter_surface,(area.width-FPS_counter_surface.get_width(),0))
        count_fps()
        
        #statics
        pg.display.flip()
        clock.tick(100)

def updateValues(userData): #converts the imported data into the correct variable name. 
    #data that is saved [easy highscore, normal highscore, hard highscore,[List of the 10 best Highscores]]
    global saveData
    saveData = userData
    if saveData[5][2] == 0:
        saveData[5][2] = 10
    print(saveData) #here to make sure the correct data is being loaded

def leaderboardScreen():
    global running, global_performance
    screen = pg.display.set_mode((640,480))
    area = screen.get_rect()
    clock = pg.time.Clock()
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color_firstPlace = pg.Color("MOCCASIN")
    color_topFive = pg.Color("ORANGE")
    color_topTen = pg.Color("DARKVIOLET")
    color_fps = pg.Color(0,255,0)
    font = pg.font.Font(None,32)
    font_fps = pg.font.Font(None,12)

    #back button
    back_button = pg.Rect(0,0,70,32)
    back_color = color_inactive
    back_txt = 'back'
    #all the rectangles for the table
    Rect_01 = pg.Rect((area.width/3)-75,(area.height*1/6),150,32)
    Rect_01_txt = 'Player'
    Rect_01_color = color_inactive

    Rect_02 = pg.Rect((Rect_01.x+Rect_01.width),(Rect_01.y),150,32)
    Rect_02_txt = 'Global'
    Rect_02_color = color_inactive

    Rect_03 = pg.Rect((Rect_02.x+Rect_02.width),(Rect_02.y),150,32)
    Rect_03_txt = 'performance'
    Rect_03_color = color_inactive

    Rect_04 = pg.Rect((Rect_01.x),(Rect_01.y+Rect_01.height),150,32)
    Rect_04_txt = 'name'

    Rect_05 = pg.Rect((Rect_04.x+Rect_04.width),(Rect_04.y),150,32)
    Rect_05_txt = 'pp'

    Rect_06 = pg.Rect((Rect_05.x+Rect_05.width),(Rect_05.y),150,32)
    Rect_06_txt = 'mode'

    Rect_07 = pg.Rect((Rect_04.x),(Rect_04.y+Rect_04.height),150,32)
    Rect_07_txt = ''

    Rect_08 = pg.Rect((Rect_07.x+Rect_07.width),(Rect_07.y),150,32)
    Rect_08_txt = ''

    Rect_09 = pg.Rect((Rect_08.x+Rect_08.width),(Rect_08.y),150,32)
    Rect_09_txt = ''

    Rect_10 = pg.Rect((Rect_07.x),(Rect_07.y+Rect_07.height),150,32)
    Rect_10_txt = ''

    Rect_11 = pg.Rect((Rect_10.x+Rect_10.width),(Rect_10.y),150,32)
    Rect_11_txt = ''

    Rect_12 = pg.Rect((Rect_11.x+Rect_11.width),(Rect_11.y),150,32)
    Rect_12_txt = ''

    Rect_13 = pg.Rect((Rect_10.x),(Rect_10.y+Rect_10.height),150,32)
    Rect_13_txt = ''

    Rect_14 = pg.Rect((Rect_13.x+Rect_13.width),(Rect_13.y),150,32)
    Rect_14_txt = ''

    Rect_15 = pg.Rect((Rect_14.x+Rect_14.width),(Rect_14.y),150,32)
    Rect_15_txt = ''

    Rect_16 = pg.Rect((Rect_13.x),(Rect_13.y+Rect_13.height),150,32)
    Rect_16_txt = ''

    Rect_17 = pg.Rect((Rect_16.x+Rect_16.width),(Rect_16.y),150,32)
    Rect_17_txt = ''

    Rect_18 = pg.Rect((Rect_17.x+Rect_17.width),(Rect_17.y),150,32)
    Rect_18_txt = ''

    Rect_19 = pg.Rect((Rect_16.x),(Rect_16.y+Rect_16.height),150,32)
    Rect_19_txt = ''

    Rect_20 = pg.Rect((Rect_19.x+Rect_19.width),(Rect_19.y),150,32)
    Rect_20_txt = ''

    Rect_21 = pg.Rect((Rect_20.x+Rect_20.width),(Rect_20.y),150,32)
    Rect_21_txt = ''

    Rect_22 = pg.Rect((Rect_19.x),(Rect_19.y+Rect_19.height),150,32)
    Rect_22_txt = ''

    Rect_23 = pg.Rect((Rect_22.x+Rect_22.width),(Rect_22.y),150,32)
    Rect_23_txt = ''

    Rect_24 = pg.Rect((Rect_23.x+Rect_23.width),(Rect_23.y),150,32)
    Rect_24_txt = ''

    Rect_25 = pg.Rect((Rect_22.x),(Rect_22.y+Rect_22.height),150,32)
    Rect_25_txt = ''

    Rect_26 = pg.Rect((Rect_25.x+Rect_25.width),(Rect_25.y),150,32)
    Rect_26_txt = ''

    Rect_27 = pg.Rect((Rect_26.x+Rect_26.width),(Rect_26.y),150,32)
    Rect_27_txt =''

    Rect_28 = pg.Rect((Rect_25.x),(Rect_25.y+Rect_25.height),150,32)
    Rect_28_txt = ''

    Rect_29 = pg.Rect((Rect_28.x+Rect_28.width),(Rect_28.y),150,32)
    Rect_29_txt = ''

    Rect_30 = pg.Rect((Rect_29.x+Rect_29.width),(Rect_29.y),150,32)
    Rect_30_txt = ''

    Rect_31 = pg.Rect((Rect_28.x),(Rect_28.y+Rect_28.height),150,32)
    Rect_31_txt = ''

    Rect_32 = pg.Rect((Rect_31.x+Rect_31.width),(Rect_31.y),150,32)
    Rect_32_txt = ''

    Rect_33 = pg.Rect((Rect_32.x+Rect_32.width),(Rect_32.y),150,32)
    Rect_33_txt = ''
    
    Rect_34 = pg.Rect((Rect_31.x),(Rect_31.y+Rect_31.height),150,32)
    Rect_34_txt = ''

    Rect_35 = pg.Rect((Rect_34.x+Rect_34.width),(Rect_34.y),150,32)
    Rect_35_txt = ''

    Rect_36 = pg.Rect((Rect_35.x+Rect_35.width),(Rect_35.y),150,32)
    Rect_36_txt = ''


    
    state = 'global'
    done = False
    while not done:
        if state == 'player':
            #sets the color of the button
            Rect_01_color = color_active
            Rect_02_color = color_inactive
            Rect_03_color = color_inactive
            #resets rect 06
            Rect_06_txt = "mode"

            #settings all the usernames
            Rect_07_txt = username_txt
            Rect_10_txt = username_txt
            Rect_13_txt = username_txt
            Rect_16_txt = username_txt
            Rect_19_txt = username_txt
            Rect_22_txt = username_txt
            Rect_25_txt = username_txt
            Rect_28_txt = username_txt
            Rect_31_txt = username_txt
            Rect_34_txt = username_txt

            #setting all the highscores
            Rect_08_txt = str(saveData[3][0])
            Rect_11_txt = str(saveData[3][1])
            Rect_14_txt = str(saveData[3][2])
            Rect_17_txt = str(saveData[3][3])
            Rect_20_txt = str(saveData[3][4])
            Rect_23_txt = str(saveData[3][5])
            Rect_26_txt = str(saveData[3][6])
            Rect_29_txt = str(saveData[3][7])
            Rect_32_txt = str(saveData[3][8])
            Rect_35_txt = str(saveData[3][9])

            #settings all the difficulties
            Rect_09_txt = saveData[4][0]
            Rect_12_txt = saveData[4][1]
            Rect_15_txt = saveData[4][2]
            Rect_18_txt = saveData[4][3]
            Rect_21_txt = saveData[4][4]
            Rect_24_txt = saveData[4][5]
            Rect_27_txt = saveData[4][6]
            Rect_30_txt = saveData[4][7]
            Rect_33_txt = saveData[4][8]
            Rect_36_txt = saveData[4][9]

        elif state == 'global':
            #sets the color of the button
            Rect_02_color = color_active
            Rect_01_color = color_inactive
            Rect_03_color = color_inactive
            # resets Rect 06
            Rect_06_txt = "mode"
            #settings all the usernames
            Rect_07_txt = global_highscores[0][0]
            Rect_10_txt = global_highscores[0][1]
            Rect_13_txt = global_highscores[0][2]
            Rect_16_txt = global_highscores[0][3]
            Rect_19_txt = global_highscores[0][4]
            Rect_22_txt = global_highscores[0][5]
            Rect_25_txt = global_highscores[0][6]
            Rect_28_txt = global_highscores[0][7]
            Rect_31_txt = global_highscores[0][8]
            Rect_34_txt = global_highscores[0][9]

            #setting all the scores
            Rect_08_txt = str(global_highscores[1][0])
            Rect_11_txt = str(global_highscores[1][1])
            Rect_14_txt = str(global_highscores[1][2])
            Rect_17_txt = str(global_highscores[1][3])
            Rect_20_txt = str(global_highscores[1][4])
            Rect_23_txt = str(global_highscores[1][5])
            Rect_26_txt = str(global_highscores[1][6])
            Rect_29_txt = str(global_highscores[1][7])
            Rect_32_txt = str(global_highscores[1][8])
            Rect_35_txt = str(global_highscores[1][9])

            #setting all the difficulties
            Rect_09_txt = global_highscores[2][0]
            Rect_12_txt = global_highscores[2][1]
            Rect_15_txt = global_highscores[2][2]
            Rect_18_txt = global_highscores[2][3]
            Rect_21_txt = global_highscores[2][4]
            Rect_24_txt = global_highscores[2][5]
            Rect_27_txt = global_highscores[2][6]
            Rect_30_txt = global_highscores[2][7]
            Rect_33_txt = global_highscores[2][8]
            Rect_36_txt = global_highscores[2][9]

        elif state == 'performance':
            #sets the color of the button
            Rect_02_color = color_inactive
            Rect_01_color = color_inactive
            Rect_03_color = color_active
            #resets Rect 06 
            Rect_06_txt = "Level"
            #settings all the usernames
            Rect_07_txt = global_performance[0][0]
            Rect_10_txt = global_performance[0][1]
            Rect_13_txt = global_performance[0][2]
            Rect_16_txt = global_performance[0][3]
            Rect_19_txt = global_performance[0][4]
            Rect_22_txt = global_performance[0][5]
            Rect_25_txt = global_performance[0][6]
            Rect_28_txt = global_performance[0][7]
            Rect_31_txt = global_performance[0][8]
            Rect_34_txt = global_performance[0][9]

            #setting all the scores
            Rect_08_txt = str(global_performance[1][0])
            Rect_11_txt = str(global_performance[1][1])
            Rect_14_txt = str(global_performance[1][2])
            Rect_17_txt = str(global_performance[1][3])
            Rect_20_txt = str(global_performance[1][4])
            Rect_23_txt = str(global_performance[1][5])
            Rect_26_txt = str(global_performance[1][6])
            Rect_29_txt = str(global_performance[1][7])
            Rect_32_txt = str(global_performance[1][8])
            Rect_35_txt = str(global_performance[1][9])

            #setting all the difficulties
            Rect_09_txt = str(global_performance[2][0])
            Rect_12_txt = str(global_performance[2][1])
            Rect_15_txt = str(global_performance[2][2])
            Rect_18_txt = str(global_performance[2][3])
            Rect_21_txt = str(global_performance[2][4])
            Rect_24_txt = str(global_performance[2][5])
            Rect_27_txt = str(global_performance[2][6])
            Rect_30_txt = str(global_performance[2][7])
            Rect_33_txt = str(global_performance[2][8])
            Rect_36_txt = str(global_performance[2][9])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    done = True
                if Rect_01.collidepoint(event.pos):
                    state = 'player'
                elif Rect_02.collidepoint(event.pos):
                    state = 'global'
                elif Rect_03.collidepoint(event.pos):
                    state = 'performance'

            
        screen.fill((30,30,30))

        #render  text for the buttons
        back_button_txt_Surface =font.render(back_txt,True,back_color)
        Rect_01_txt_surface = font.render(Rect_01_txt,True,Rect_01_color)
        Rect_02_txt_surface = font.render(Rect_02_txt,True,Rect_02_color)
        Rect_03_txt_surface = font.render(Rect_03_txt,True,Rect_03_color)
        Rect_04_txt_surface = font.render(Rect_04_txt,True,color_inactive)
        Rect_05_txt_surface = font.render(Rect_05_txt,True,color_inactive)
        Rect_06_txt_surface = font.render(Rect_06_txt,True,color_inactive)
        Rect_07_txt_surface = font.render(Rect_07_txt,True,color_firstPlace)
        Rect_08_txt_surface = font.render(Rect_08_txt,True,color_firstPlace)
        Rect_09_txt_surface = font.render(Rect_09_txt,True,color_firstPlace)
        Rect_10_txt_surface = font.render(Rect_10_txt,True,color_topFive)
        Rect_11_txt_surface = font.render(Rect_11_txt,True,color_topFive)
        Rect_12_txt_surface = font.render(Rect_12_txt,True,color_topFive)
        Rect_13_txt_surface = font.render(Rect_13_txt,True,color_topFive)
        Rect_14_txt_surface = font.render(Rect_14_txt,True,color_topFive)
        Rect_15_txt_surface = font.render(Rect_15_txt,True,color_topFive)
        Rect_16_txt_surface = font.render(Rect_16_txt,True,color_topFive)
        Rect_17_txt_surface = font.render(Rect_17_txt,True,color_topFive)
        Rect_18_txt_surface = font.render(Rect_18_txt,True,color_topFive)
        Rect_19_txt_surface = font.render(Rect_19_txt,True,color_topFive)
        Rect_20_txt_surface = font.render(Rect_20_txt,True,color_topFive)
        Rect_21_txt_surface = font.render(Rect_21_txt,True,color_topFive)
        Rect_22_txt_surface = font.render(Rect_22_txt,True,color_topTen)
        Rect_23_txt_surface = font.render(Rect_23_txt,True,color_topTen)
        Rect_24_txt_surface = font.render(Rect_24_txt,True,color_topTen)
        Rect_25_txt_surface = font.render(Rect_25_txt,True,color_topTen)
        Rect_26_txt_surface = font.render(Rect_26_txt,True,color_topTen)
        Rect_27_txt_surface = font.render(Rect_27_txt,True,color_topTen)
        Rect_28_txt_surface = font.render(Rect_28_txt,True,color_topTen)
        Rect_29_txt_surface = font.render(Rect_29_txt,True,color_topTen)
        Rect_30_txt_surface = font.render(Rect_30_txt,True,color_topTen)
        Rect_31_txt_surface = font.render(Rect_31_txt,True,color_topTen)
        Rect_32_txt_surface = font.render(Rect_32_txt,True,color_topTen)
        Rect_33_txt_surface = font.render(Rect_33_txt,True,color_topTen)
        Rect_34_txt_surface = font.render(Rect_34_txt,True,color_topTen)
        Rect_35_txt_surface = font.render(Rect_35_txt,True,color_topTen)
        Rect_36_txt_surface = font.render(Rect_36_txt,True,color_topTen)

        #FPS COUNTER
        FPS_counter_surface = font_fps.render(str(math.floor(FPS))+"FPS",True,color_fps)
        screen.blit(FPS_counter_surface,(area.width-FPS_counter_surface.get_width(),0))
        count_fps()

        #blit the text
        screen.blit(back_button_txt_Surface,(back_button.x+5,back_button.y+5))
        screen.blit(Rect_01_txt_surface,(Rect_01.x+5,Rect_01.y+5))
        screen.blit(Rect_02_txt_surface,(Rect_02.x+5,Rect_02.y+5))
        screen.blit(Rect_03_txt_surface,(Rect_03.x+5,Rect_03.y+5))
        screen.blit(Rect_04_txt_surface,(Rect_04.x+5,Rect_04.y+5))
        screen.blit(Rect_05_txt_surface,(Rect_05.x+5,Rect_05.y+5))
        screen.blit(Rect_06_txt_surface,(Rect_06.x+5,Rect_06.y+5))
        screen.blit(Rect_07_txt_surface,(Rect_07.x+5,Rect_07.y+5))
        screen.blit(Rect_08_txt_surface,(Rect_08.x+5,Rect_08.y+5))
        screen.blit(Rect_09_txt_surface,(Rect_09.x+5,Rect_09.y+5))
        screen.blit(Rect_10_txt_surface,(Rect_10.x+5,Rect_10.y+5))
        screen.blit(Rect_11_txt_surface,(Rect_11.x+5,Rect_11.y+5))
        screen.blit(Rect_12_txt_surface,(Rect_12.x+5,Rect_12.y+5))
        screen.blit(Rect_13_txt_surface,(Rect_13.x+5,Rect_13.y+5))
        screen.blit(Rect_14_txt_surface,(Rect_14.x+5,Rect_14.y+5))
        screen.blit(Rect_15_txt_surface,(Rect_15.x+5,Rect_15.y+5))
        screen.blit(Rect_16_txt_surface,(Rect_16.x+5,Rect_16.y+5))
        screen.blit(Rect_17_txt_surface,(Rect_17.x+5,Rect_17.y+5))
        screen.blit(Rect_18_txt_surface,(Rect_18.x+5,Rect_18.y+5))
        screen.blit(Rect_19_txt_surface,(Rect_19.x+5,Rect_19.y+5))
        screen.blit(Rect_20_txt_surface,(Rect_20.x+5,Rect_20.y+5))
        screen.blit(Rect_21_txt_surface,(Rect_21.x+5,Rect_21.y+5))
        screen.blit(Rect_22_txt_surface,(Rect_22.x+5,Rect_22.y+5))
        screen.blit(Rect_23_txt_surface,(Rect_23.x+5,Rect_23.y+5))
        screen.blit(Rect_24_txt_surface,(Rect_24.x+5,Rect_24.y+5))
        screen.blit(Rect_25_txt_surface,(Rect_25.x+5,Rect_25.y+5))
        screen.blit(Rect_26_txt_surface,(Rect_26.x+5,Rect_26.y+5))
        screen.blit(Rect_27_txt_surface,(Rect_27.x+5,Rect_27.y+5))
        screen.blit(Rect_28_txt_surface,(Rect_28.x+5,Rect_28.y+5))
        screen.blit(Rect_29_txt_surface,(Rect_29.x+5,Rect_29.y+5))
        screen.blit(Rect_30_txt_surface,(Rect_30.x+5,Rect_30.y+5))
        screen.blit(Rect_31_txt_surface,(Rect_31.x+5,Rect_31.y+5))
        screen.blit(Rect_32_txt_surface,(Rect_32.x+5,Rect_32.y+5))
        screen.blit(Rect_33_txt_surface,(Rect_33.x+5,Rect_33.y+5))
        screen.blit(Rect_34_txt_surface,(Rect_34.x+5,Rect_34.y+5))
        screen.blit(Rect_35_txt_surface,(Rect_35.x+5,Rect_35.y+5))
        screen.blit(Rect_36_txt_surface,(Rect_36.x+5,Rect_36.y+5))




        #blit the buttons
        pg.draw.rect(screen,back_color,back_button,2)

        #blit the rectangles
        pg.draw.rect(screen,color_inactive,Rect_01,2)
        pg.draw.rect(screen,color_inactive,Rect_02,2)
        pg.draw.rect(screen,color_inactive,Rect_03,2)
        pg.draw.rect(screen,color_inactive,Rect_04,2)
        pg.draw.rect(screen,color_inactive,Rect_05,2)
        pg.draw.rect(screen,color_inactive,Rect_06,2)
        pg.draw.rect(screen,color_inactive,Rect_07,2)
        pg.draw.rect(screen,color_inactive,Rect_08,2)
        pg.draw.rect(screen,color_inactive,Rect_09,2)
        pg.draw.rect(screen,color_inactive,Rect_10,2)
        pg.draw.rect(screen,color_inactive,Rect_11,2)
        pg.draw.rect(screen,color_inactive,Rect_12,2)
        pg.draw.rect(screen,color_inactive,Rect_13,2)
        pg.draw.rect(screen,color_inactive,Rect_14,2)
        pg.draw.rect(screen,color_inactive,Rect_15,2)
        pg.draw.rect(screen,color_inactive,Rect_16,2)
        pg.draw.rect(screen,color_inactive,Rect_17,2)
        pg.draw.rect(screen,color_inactive,Rect_18,2)
        pg.draw.rect(screen,color_inactive,Rect_19,2)
        pg.draw.rect(screen,color_inactive,Rect_20,2)
        pg.draw.rect(screen,color_inactive,Rect_21,2)
        pg.draw.rect(screen,color_inactive,Rect_22,2)
        pg.draw.rect(screen,color_inactive,Rect_23,2)
        pg.draw.rect(screen,color_inactive,Rect_24,2)
        pg.draw.rect(screen,color_inactive,Rect_25,2)
        pg.draw.rect(screen,color_inactive,Rect_26,2)
        pg.draw.rect(screen,color_inactive,Rect_27,2)
        pg.draw.rect(screen,color_inactive,Rect_28,2)
        pg.draw.rect(screen,color_inactive,Rect_29,2)
        pg.draw.rect(screen,color_inactive,Rect_30,2)
        pg.draw.rect(screen,color_inactive,Rect_31,2)
        pg.draw.rect(screen,color_inactive,Rect_32,2)
        pg.draw.rect(screen,color_inactive,Rect_33,2)
        pg.draw.rect(screen,color_inactive,Rect_34,2)
        pg.draw.rect(screen,color_inactive,Rect_35,2)
        pg.draw.rect(screen,color_inactive,Rect_36,2)
        

        pg.display.flip()
        clock.tick(100)

def mainmenuScreen():
    #importing Main loop variable
    global mainmenuscreen, running, loginscreen, mainmenuscreen,leaderboardScreen, settingsScreen
    screen = pg.display.set_mode((640, 480))
    area = screen.get_rect()
    clock = pg.time.Clock()
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color_fps = pg.Color(0,255,0)
    font = pg.font.Font(None, 32)
    font_fps = pg.font.Font(None,12)

    #start game button
    Start_Game_Color = color_inactive
    Start_Game_Txt = "Start Game"
    Start_Game = pg.Rect ((area.width/2)-75,(area.height/6),150,32)

    #settings screen button
    Settings_Color = color_inactive
    Settings_Txt = "Settings"
    Settings = pg.Rect((area.width/2)-75,((area.height/6)*2),150,32)
    
    #store button   (TO BE ADDED)

    #leaderBoard button
    leaderBoard_button_Color = color_inactive
    leaderBoard_button_Txt = 'LeaderBoard'
    leaderBoard_button = pg.Rect((area.width/2)-75,((area.height/6)*3),150,32)

    #exit game button
    Quit_Game_Color = color_inactive
    Quit_Game_Txt = "Quit Game"
    Quit_Game = pg.Rect((area.width/2)-75,((area.height/6)*5),150,32)

    #logout game button
    Logout_Game_Color = color_inactive
    Logout_Game_Txt = "Logout"
    Logout_Game = pg.Rect((area.width/2)-75,(area.height*4/6),150,32)





    done = False

    #main mainmenu loop
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                
            #change color and do action when clicked
            elif event.type == pg.MOUSEBUTTONDOWN:
                if Start_Game.collidepoint(event.pos):
                    Start_Game_Color = color_active
                    difficultySelectScreen()
                elif Quit_Game.collidepoint(event.pos):
                    Quit_Game_Color = color_active
                    pg.quit()
                elif Settings.collidepoint(event.pos):
                    Settings_Color = color_active
                    settingsScreen()
                elif leaderBoard_button.collidepoint(event.pos):
                    leaderBoard_button_Color = color_active
                    leaderboardScreen()
                elif Logout_Game.collidepoint(event.pos):
                    Logout_Game_Color = color_active
                    loginscreen = True
                    done = True
                    mainmenuscreen = False
                    
            #makes sure the color of the button go back to original
            elif event.type != pg.MOUSEBUTTONDOWN:
                Start_Game_Color = color_inactive
                Quit_Game_Color = color_inactive
                Settings_Color = color_inactive
                leaderBoard_button_Color = color_inactive
                Logout_Game_Color - color_inactive


        screen.fill((30,30,30))

        #render text for buttons
        txt_startgame = font.render(Start_Game_Txt,True, Start_Game_Color)
        txt_quitgame = font.render(Quit_Game_Txt,True, Quit_Game_Color)
        txt_settings = font.render(Settings_Txt,True, Settings_Color)
        txt_leaderboard = font.render(leaderBoard_button_Txt,True,leaderBoard_button_Color)
        txt_logout = font.render(Logout_Game_Txt,True,Logout_Game_Color)
        FPS_counter_surface = font_fps.render(str(math.floor(FPS))+"FPS",True,color_fps)


        #Blit the text
        screen.blit(txt_startgame,(Start_Game.x + 5, Start_Game.y +5))
        screen.blit(txt_quitgame,(Quit_Game.x+5,Quit_Game.y+5))
        screen.blit(txt_settings,(Settings.x+5,Settings.y+5))
        screen.blit(txt_leaderboard,(leaderBoard_button.x+5,leaderBoard_button.y+5))
        screen.blit(txt_logout,(Logout_Game.x+5,Logout_Game.y+5))
        screen.blit(FPS_counter_surface,(area.width-FPS_counter_surface.get_width(),0))

        
        #Blit the buttons
        pg.draw.rect(screen,Start_Game_Color,Start_Game,2)
        pg.draw.rect(screen,Quit_Game_Color,Quit_Game,2)
        pg.draw.rect(screen,Settings_Color,Settings,2)
        pg.draw.rect(screen,leaderBoard_button_Color,leaderBoard_button,2)
        pg.draw.rect(screen,Logout_Game_Color,Logout_Game,2)

        count_fps()
        pg.display.flip()
        clock.tick(100)

def makeDifficulty():
    global Dictionary, easyDictionary, mediumDictionary, hardDictionary
    length = len(Dictionary)
    i = 0
    easyDictionary = []
    mediumDictionary = []
    hardDictionary = []
    while i < length:
        wordLength = len(Dictionary[i])

        if wordLength < 5:
            easyDictionary.append(Dictionary[i])
            i += 1
        elif wordLength < 7:
            mediumDictionary.append(Dictionary[i])
            i += 1
        elif wordLength <= 8:
            hardDictionary.append(Dictionary[i])
            i += 1
        else:
            pass
            i += 1

def Words(): #based on the difficulty selected it picks a random word from the three list difficulties, and returns the lower case of that word
    global globalDifficulty, Dictionary, easyDictionary, mediumDictionary, hardDictionary #allows all the other functions to use this global variables
    
    if globalDifficulty == "easyDictionary":
        itemNumber = randrange(0,len(easyDictionary)-1)
        word = easyDictionary[itemNumber]

    elif globalDifficulty == "normalDictionary":
        itemNumber = randrange(0,len(mediumDictionary)-1)
        word = mediumDictionary[itemNumber]

    elif globalDifficulty == "hardDictionary":
        itemNumber = randrange(0,len(hardDictionary)-1)
        word = hardDictionary[itemNumber]

    return word.lower()

def gameScreen():
    global mainmenuscreen, gamescreen, saveData, saving, saveValues,accuracy, typing_speed, FPS, deltatime
    screen = pg.display.set_mode((640,480),pg.HWSURFACE|pg.DOUBLEBUF)
    font = pg.font.Font(None,32)
    font_fps = pg.font.Font(None,12)
    area = screen.get_rect() #gets the size of the screen
    clock = pg.time.Clock()
    timer = Stopwatch()
    timer.restart()
    deltatime = 0
    FPS = 30

    #static text variables
    highScoreTxt = 'highscore:'
    
    #adding the words initially before loop does it
    word = Words()
    word_Loc = [randrange(0,area.width-100),0]

    word2 = Words()
    word2_Loc = [randrange(0,area.width-100),15]

    word3 = Words()
    word3_Loc = [randrange(0,area.width-100),45]

    #variables for the game loop 
    speed = 1 #speed for score calculation
    speed2 = 1 #how fast words fall down the screen
    score = 0 #current player score
    scoreTxt = 'score:' #static to display on the gamewindow screen
    
    #updates words to a random position on the screen, without it the words jump around constantly. State changes to True when a word is typed correctly and False when its updated on screen
    updateWord = False
    updateWord2 = False
    updateWord3 = False

    accuracy = [0,0,0] #right, wrong, %
    accTxt = accuracy[2]
    typing_speed = 0

    #Statics for the input box where the user writes the words
    input_box = pg.Rect(area.width/2-100, area.height-50, 30, 30)
    text = ''
    color_active = pg.Color('dodgerblue2')
    color_fps = pg.Color(0,255,0) #BRIGHT GREEN
    done = False

    #main game loop
    while not done:
        global word1_surface , word2_surface, word3_surface
        #checks if program is closed
        for event in pg.event.get():


            if event.type == pg.QUIT:
                done = True
                pg.quit()

        #checks if move keys are pressed
            if event.type == pg.KEYDOWN:
                
                #deletes a key if backspace pressed
                if event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                    accuracy[1] += 1

                #stops the game and goes into the mainmenu when escape is pressed
                elif event.key == pg.K_ESCAPE:
                    performance = score*speed*DifficultyMultiplier*480/area.height
                    performanceScore(performance)
                    saveValues()
                    done = True
                    saving = True
                
                #if either space or enter is pressed, the word will be compared with the words on the screen
                elif event.key == pg.K_SPACE or event.key == pg.K_RETURN:
                    #checks whether the typed word matches any of the words that are on the screen. This is repeated for word2 and word3
                    if text == word:
                        accuracy[0] += len(word)
                        accuracy[1] += len(word)
                        word = Words() #updates the word
                        while word == (word2 or word3):
                            word = Words()
                        updateWord = True
                        word_Loc[1] = 0
                        text = ''
                        score +=1

                    elif text == word2:
                        accuracy[0] += len(word2)
                        accuracy[1] += len(word2)
                        word2 = Words()
                        while word2 == (word or word3):
                            word2 = Words()
                        updateWord2 = True
                        word2_Loc[1] = 0
                        text = ''
                        score += 1
                    elif text == word3:
                        accuracy[0] += len(word3)
                        accuracy[1] += len(word3)
                        if score > 5:
                            word3 = Words()
                            while word3 == (word2 or word):
                                word3 = Words()
                            updateWord3 = True
                            word3_Loc[1] = 0
                            text = ''
                            score +=1
                    else:
                        text = ''
                        accuracy[1] += 1
                else:
                    text += event.unicode
        
        #statics
        currentPerformance = round(score*speed*DifficultyMultiplier,1) #updates the value of the performance and rounds it to 1 decimal point
        if accuracy[1] > 0:
            accuracy[2] = round(accuracy[0]/accuracy[1] *100,2)
        screen.fill((30,30,30))
        
        #render the current text
        score_surface = font.render(str(score),True,color_active) #return to score
        scoreTxt_surface = font.render(scoreTxt,True,color_active)
        currentPerformance_surface = font.render(str(currentPerformance)+"pp",True,color_active)
        accTxt_surface = font.render(str(accuracy[2])+"%",True,color_active)
        FPS_counter_surface = font_fps.render(str(math.floor(FPS))+"FPS",True,color_fps)
        
        #renders the highscore for the current game mode being played
        highScoreTxt_surface = font.render(highScoreTxt,True,color_active)
        if globalDifficulty == 'easyDictionary':
            highScore_surface = font.render(str(saveData[0]),True,color_active)
        elif globalDifficulty == 'normalDictionary':
            highScore_surface = font.render(str(saveData[1]),True,color_active)
        elif globalDifficulty == 'hardDictionary':
            highScore_surface = font.render(str(saveData[2]),True,color_active)

        #renders the input text, and the 3 words where 1 of the words only appears after the user has reached a score of 6
        txt_surface = font.render(text,True,color_active)
        word1_surface = font.render(word,True,color_active)
        word2_surface = font.render(word2,True,color_active)
        if score > 5:
            word3_surface = font.render(word3,True,color_active)
        

        #updates the word location and keeps them on screen
        if updateWord:
            word_Loc[0] = randrange(0,area.width - int(word1_surface.get_width()))
            updateWord = False

        if updateWord2:
            word2_Loc[0] = randrange(0,area.width - int(word2_surface.get_width()))
            updateWord2 = False
        if score > 5:
            if updateWord3:
                word3_Loc[0] = randrange(0,area.width - int(word3_surface.get_width()))
                updateWord3 = False

        #resize the box
        input_box.width = max(200,txt_surface.get_width()+10)
        input_box.x = area.width/2 - input_box.width/2

        #blit the text
        screen.blit(txt_surface,(input_box.x+5,input_box.y+5))
        screen.blit(accTxt_surface,(0,0))
        screen.blit(FPS_counter_surface,(area.width-FPS_counter_surface.get_width(),0))


        #blit the words 
        screen.blit(currentPerformance_surface,(0,input_box.y+25))
        screen.blit(score_surface,(100,input_box.y+5))
        screen.blit(scoreTxt_surface,(0,input_box.y+5))
        screen.blit(highScoreTxt_surface,(area.width-highScoreTxt_surface.get_width()-highScore_surface.get_width(),input_box.y+5))
        screen.blit(highScore_surface,(area.width-highScore_surface.get_width(),input_box.y+5))
        screen.blit(word1_surface,(word_Loc[0],word_Loc[1]))
        screen.blit(word2_surface,(word2_Loc[0],word2_Loc[1]))
        if score > 5:
            screen.blit(word3_surface,(word3_Loc[0],word3_Loc[1]))

        #blit the input box and floor
        pg.draw.rect(screen,color_active,input_box,2)


        #moving the words
        word_Loc[1] += speed2
        word2_Loc[1] += speed2
        if score > 5:
            word3_Loc[1] += speed2
        
        #checks to see if words are off screen
        if word_Loc[1] > area.height:
            print(accuracy[2])
            performance = score*speed*DifficultyMultiplier*480/area.height 
            performanceScore(performance)
            saveValues()
            done = True
            saving = True
            #endgameScreen(currentPerformance)

        elif word2_Loc[1] > area.height:
            print(accuracy[2])
            performance = score*speed*DifficultyMultiplier*480/area.height 
            performanceScore(performance)
            saveValues()
            done = True
            saving = True
            #endgameScreen(currentPerformance)

        elif word3_Loc[1] > area.height:
            print(accuracy[2])
            performance = score*speed*DifficultyMultiplier*480/area.height 
            performanceScore(performance)
            saveValues()
            done = True
            saving = True
            #endgameScreen(currentPerformance)

        #statics, and update speed of words
        speed = ((score**2)*(1/2400)+1)*area.height/480 #*(sum(saveData[7])/len(saveData[7])/20) #speed value for score calculation

        speed2 = ((score**2)*(1/2400)+1)*area.height/480 * deltatime *30 #*(sum(saveData[7])/len(saveData[7])/20)

        if accuracy[1] > 0:
            typing_speed = round(12*accuracy[1]/round(timer.duration,1),1)

        count_fps()
        pg.display.flip()
        clock.tick(100)

        
        

        #updates the highscore if the score is larger than the highscore
        if globalDifficulty == 'easyDictionary':
            if score > saveData[0]:
                saveData[0] = score
        elif globalDifficulty == 'normalDictionary':
            if score > saveData[1]:
                saveData[1] = score
        elif globalDifficulty == 'hardDictionary':
            if score > saveData[2]:
                saveData[2] = score

def endgameScreen(): #(TO BE ADDED)
    pass

def difficultySelectScreen():
    global globalDifficulty, saveData, DifficultyMultiplier,playerAccuracy
    playerPerformace = round((saveData[3][0])*1.00 + (saveData[3][1])*0.95 + (saveData[3][2])*0.90 + (saveData[3][3])*0.86 + (saveData[3][4])*0.81 + (saveData[3][5])*0.77 + (saveData[3][6])*0.74 + (saveData[3][7])*0.70 + (saveData[3][8])*0.66 + (saveData[3][9])*0.63,2)
    playerAccuracy = round(sum(saveData[6])/10,2)
    playerSpeed = round(sum(saveData[7])/len(saveData[7]),1)
    screen = pg.display.set_mode((640,480))
    font = pg.font.Font(None,32)
    font_fps = pg.font.Font(None,12)
    area = screen.get_rect() 
    clock = pg.time.Clock()
    
    #statics
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color_level = pg.Color('darkgoldenrod')
    color_LegendaryScore = pg.Color("DARKORANGE")
    color_EpicScore = pg.Color("DARKVIOLET")
    color_RareScore = pg.Color("ROYALBLUE")
    color_UncommonScore = pg.Color("LIMEGREEN")
    color_CommonScore = pg.Color("DARKGRAY")
    color_fps = pg.Color(0,255,0) #BRIGHT GREEN


    #buttons

    #easy button
    easy_Game = pg.Rect((area.width/2-150),(area.height*1/6),150,32)
    easy_Game_Color = color_inactive
    easy_Game_Txt = 'Easy Mode'
    easy_Highscore = str(saveData[0])
    easy_Highscore_Txt = 'Best:'

    #normal button
    normal_Game = pg.Rect((area.width/2-150),(area.height*2/6),150,32)
    normal_Game_Color = color_inactive
    normal_Game_Txt = 'Normal Mode'
    normal_Highscore = str(saveData[1])
    normal_Highscore_txt = 'Best: '

    #hard button
    hard_Game = pg.Rect((area.width/2-150),(area.height*3/6),150,32)
    hard_Game_Color = color_inactive
    hard_Game_Txt = 'Hard Mode'
    hard_Highscore = str(saveData[2])
    hard_Highscore_txt = 'Best: '

    #back button
    back_button = pg.Rect((area.width/2-150),(area.height*4/6),150,32)
    back_button_color = color_inactive
    back_button_txt = 'back'

    #user box <- this is the box that will contain the player level, player name player performance
    userbox = pg.Rect((area.width/2-150),0,300,70)
    userbox_color = color_active
    userbox_performance = str(playerPerformace)+ "pp"
    userbox_performance_color = color_UncommonScore
    userbox_name = username_txt
    userbox_level = ("Lvl: "+str(saveData[5][0]))
    userbox_accuracy = (str(playerAccuracy)+"%")
    userbox_playerSpeed = (str(playerSpeed)+"WPM")

    #experience bar
    experiencebox = pg.Rect((userbox.x+userbox.width-100),(userbox.y+userbox.height-11),100,10)
    experienceboxbar = pg.Rect((experiencebox.x+2),(experiencebox.y+1),(saveData[5][1]/saveData[5][2]*experiencebox.width),(8))
    experienceboxbar_color = color_UncommonScore
    experiencebox_color = color_inactive

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

            elif event.type == pg.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    done = True
                elif easy_Game.collidepoint(event.pos):
                    globalDifficulty = 'easyDictionary'
                    DifficultyMultiplier = 1.5
                    easy_Game_Color = color_active
                    gameScreen()
                    done = True

                elif normal_Game.collidepoint(event.pos):
                    normal_Game_Color = color_active
                    globalDifficulty = 'normalDictionary'
                    DifficultyMultiplier = 2.27
                    gameScreen()
                    done = True
                    pass

                elif hard_Game.collidepoint(event.pos):
                    hard_Game_Color = color_active
                    globalDifficulty = 'hardDictionary'
                    DifficultyMultiplier = 4
                    gameScreen()
                    done = True
                    pass

            elif event.type != pg.MOUSEBUTTONDOWN:
                easy_Game_Color = color_inactive
                normal_Game_Color = color_inactive
                hard_Game_Color = color_inactive
        
        screen.fill((30,30,30))

        #render the text for buttons

        easy_Game_Txt_Surface = font.render(easy_Game_Txt,True,easy_Game_Color)
        normal_Game_Txt_Surface = font.render(normal_Game_Txt,True,normal_Game_Color)
        hard_Game_Txt_Surface = font.render(hard_Game_Txt,True,hard_Game_Color)
        back_button_txt_Surface = font.render(back_button_txt,True,back_button_color)
        userbox_name_surface = font.render(userbox_name,True,userbox_color)
        userbox_level_surface = font.render(userbox_level,True,color_level)
        userbox_accuracy_surface = font.render(userbox_accuracy,True,color_inactive)
        userbox_playerSpeed_surface = font.render(userbox_playerSpeed,True,color_inactive)
        #making the color of the text be score dependant 
        if playerPerformace >= 10000:
            userbox_performance_color = color_LegendaryScore
        elif playerPerformace >= 8000:
            userbox_performance_color = color_EpicScore
        elif playerPerformace >= 6000:
            userbox_performance_color = color_RareScore
        elif playerPerformace >= 4000:
            userbox_performance_color = color_UncommonScore
        else:
            userbox_performance_color = color_CommonScore
        userbox_performance_txt = font.render(userbox_performance,True,userbox_performance_color)

        #FPS COUNTER
        FPS_counter_surface = font_fps.render(str(math.floor(FPS))+"FPS",True,color_fps)
        screen.blit(FPS_counter_surface,(area.width-FPS_counter_surface.get_width(),0))
        count_fps()

        #render highscore text
        if int(easy_Highscore) >= 120:    
            easy_Highscore_Surface = font.render(easy_Highscore_Txt + easy_Highscore,True,color_LegendaryScore)
        elif int(easy_Highscore) >= 100:
            easy_Highscore_Surface = font.render(easy_Highscore_Txt + easy_Highscore,True,color_EpicScore)
        elif int(easy_Highscore) >= 85:
            easy_Highscore_Surface = font.render(easy_Highscore_Txt + easy_Highscore,True,color_RareScore)
        elif int(easy_Highscore) >= 60:
            easy_Highscore_Surface = font.render(easy_Highscore_Txt + easy_Highscore,True,color_UncommonScore)
        else:
            easy_Highscore_Surface = font.render(easy_Highscore_Txt + easy_Highscore,True,color_CommonScore)

        if int(normal_Highscore) >= 100:
            normal_Highscore_Surface = font.render(normal_Highscore_txt +normal_Highscore,True,color_LegendaryScore)
        elif int(normal_Highscore) >= 85:
            normal_Highscore_Surface = font.render(normal_Highscore_txt +normal_Highscore,True,color_EpicScore)
        elif int(normal_Highscore) >= 70:
            normal_Highscore_Surface = font.render(normal_Highscore_txt +normal_Highscore,True,color_RareScore)
        elif int(normal_Highscore) >= 50:
            normal_Highscore_Surface = font.render(normal_Highscore_txt +normal_Highscore,True,color_UncommonScore)
        else:
            normal_Highscore_Surface = font.render(normal_Highscore_txt +normal_Highscore,True,color_CommonScore)    

        if int(hard_Highscore) >= 90:
            hard_Highscore_Surface = font.render(hard_Highscore_txt+hard_Highscore,True,color_LegendaryScore)
        elif int(hard_Highscore) >= 80:
            hard_Highscore_Surface = font.render(hard_Highscore_txt+hard_Highscore,True,color_EpicScore)
        elif int(hard_Highscore) >= 65:
            hard_Highscore_Surface = font.render(hard_Highscore_txt+hard_Highscore,True,color_RareScore)
        elif int(hard_Highscore) >= 45:
            hard_Highscore_Surface = font.render(hard_Highscore_txt+hard_Highscore,True,color_UncommonScore)
        else:
            hard_Highscore_Surface = font.render(hard_Highscore_txt+hard_Highscore,True,color_CommonScore)

        #blit everything for the user box
        screen.blit(userbox_performance_txt,(userbox.x+2,userbox.y+2))
        screen.blit(userbox_name_surface,(userbox.x+2,userbox.y+userbox.height-25))
        screen.blit(userbox_level_surface,(userbox.x+userbox.width-int(userbox_level_surface.get_width())-2,userbox.y+userbox.height-35))
        screen.blit(userbox_accuracy_surface,(userbox.x+userbox.width-int(userbox_accuracy_surface.get_width())-2,userbox.y+2))
        screen.blit(userbox_playerSpeed_surface,(userbox.x+userbox.width/2-userbox_playerSpeed_surface.get_width()/2,userbox.y+userbox.height-25))

            #experience box
        pg.draw.rect(screen,experiencebox_color,experiencebox,2)
        pg.draw.rect(screen,experienceboxbar_color,experienceboxbar,0)

        #blit the text
        screen.blit(easy_Highscore_Surface,(easy_Game.x+easy_Game.width+5,easy_Game.y+5))
        screen.blit(normal_Highscore_Surface,(normal_Game.x+normal_Game.width+5,normal_Game.y+5))
        screen.blit(hard_Highscore_Surface,(hard_Game.x+hard_Game.width+5,hard_Game.y+5))
        screen.blit(easy_Game_Txt_Surface,(easy_Game.x+5,easy_Game.y+5))
        screen.blit(normal_Game_Txt_Surface,(normal_Game.x+5,normal_Game.y+5))
        screen.blit(hard_Game_Txt_Surface,(hard_Game.x+5,hard_Game.y+5))
        screen.blit(back_button_txt_Surface,(back_button.x+5,back_button.y+5))


        #blit the buttons
        pg.draw.rect(screen,easy_Game_Color,easy_Game,2)
        pg.draw.rect(screen,normal_Game_Color,normal_Game,2)
        pg.draw.rect(screen,hard_Game_Color,hard_Game,2)
        pg.draw.rect(screen,back_button_color,back_button,2)
        pg.draw.rect(screen,userbox_color,userbox,2)


        pg.display.flip()
        clock.tick(100)

def loginScreen():
    global loginscreen
    global mainmenuscreen
    global username_txt
    global global_highscores, global_performance
    try:
        usernames = pickle.load(open("SAVE_DATA/Game_Data/usernames.txt","rb"))
    except FileNotFoundError:
        usernames = []
        pickle.dump(usernames,open("SAVE_DATA/Game_Data/usernames.txt","wb"))
    try:
        passwords = pickle.load(open("SAVE_DATA/Game_Data/passwords.txt","rb"))
    except FileNotFoundError:
        passwords = []
        pickle.dump(passwords,open("SAVE_DATA/Game_Data/passwords.txt","wb"))
    try:
        global_highscores = pickle.load(open("SAVE_DATA/Game_Data/highscores.txt","rb"))
    except FileNotFoundError:
        global_highscores = [["","","","","","","","","",""],[0,0,0,0,0,0,0,0,0,0],["","","","","","","","","",""]] #[[usernames(10)][scores(top 10 pp)][difficulty(10)]]
        pickle.dump(global_highscores,open("SAVE_DATA/Game_Data/highscores.txt","wb"))
    try:
        global_performance = pickle.load(open("SAVE_DATA/Game_Data/performance.txt","rb"))
    except FileNotFoundError:
        global_performance = [["","","","","","","","","",""],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]] #names, score, level
        pickle.dump(global_performance,open("SAVE_DATA/Game_Data/performance.txt","wb"))

    print(global_performance)
    userDefaults = [0,0,0,[0,0,0,0,0,0,0,0,0,0],["","","","","","","","","",""],[0,0,10],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]] #[Highscore Easy,normal,Hard,performance[total,top 10],[diff for the highscores also top 10],[LEVEL,XP,NeedXP],[top 10 accuracy],[10 wpm for avg]]
    screen = pg.display.set_mode ((640,480))
    font = pg.font.Font(None,32)
    font_fps = pg.font.Font(None,12)
    area = screen.get_rect()
    clock = pg.time.Clock()

    #static text variables
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color_fps = pg.Color(0,255,0)

    #login box
    username_box = pg.Rect(100,100,140,32)
    username_box_color = color_inactive
    username_txt = ''

    #password box
    password_box = pg.Rect(100,164,140,32)
    password_box_color = color_inactive
    password_txt = ''
    password_txtStar = ''

    #login button
    Login_Button = pg.Rect(340,164,90,32)
    Login_Button_color = color_inactive
    Login_Button_txt = 'login'
    #sign up button
    SignUp_Button = pg.Rect(340,100,90,32)
    SignUp_Button_color = color_inactive
    SignUp_Button_txt = 'signup'

    #fps counter
    fps_counter = clock.get_fps()

    done = False
    active = False
    state = ''
    
    while not done:
        if not active:
            #resets the color of the texts and buttons
            username_box_color = color_inactive
            password_box_color = color_inactive
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONUP:
                SignUp_Button_color = color_inactive
                Login_Button_color = color_inactive

            elif event.type == pg.MOUSEBUTTONDOWN:
            
                if SignUp_Button.collidepoint(event.pos):
                    SignUp_Button_color = color_active
                    if len(username_txt) > 0: 
                        try:
                            pickle.load(open("SAVE_DATA/Users/"+str(username_txt)+".txt","rb"))
                        except FileNotFoundError:
                            pickle.dump(userDefaults,open("SAVE_DATA/Users/"+str(username_txt)+".txt","wb"))
                            usernames.append(username_txt)
                            passwords.append(password_txt)
                            pickle.dump(usernames,open("SAVE_DATA/Game_Data/usernames.txt","wb"))
                            pickle.dump(passwords,open("SAVE_DATA/Game_Data/passwords.txt","wb"))
                        else:
                            print("username already exists")
                    else:
                        print("Please make username longer")

                elif Login_Button.collidepoint(event.pos):
                    Login_Button_color = color_active
                    if username_txt in usernames:
                        if password_txt == passwords[int(usernames.index(username_txt))]:
                            try:
                                userData = pickle.load(open("SAVE_DATA/Users/"+str(username_txt)+".txt","rb"))
                                print(userData)
                            except FileNotFoundError:
                                print("please sign up")
                            else:
                                updateValues(userData)
                                mainmenuscreen = True
                                done = True
                                loginscreen = False
                        else:
                            print("wrong password")
                    else:
                        print('wrong username')
                    

                elif username_box.collidepoint(event.pos):
                    username_box_color = color_active
                    state = 'login'
                    active = not active
                
                elif password_box.collidepoint(event.pos):
                    password_box_color = color_active
                    state = 'password'
                    active = not active
                else:
                    active = False


            elif event.type == pg.KEYDOWN:
                if active:
                    if state == "login":
                        if event.key == pg.K_TAB:
                            state = 'password'
                            username_box_color = color_inactive
                            password_box_color = color_active
                        elif event.key == pg.K_RETURN:
                            username_box_color = color_inactive
                            if username_txt in usernames:
                                if password_txt == passwords[int(usernames.index(username_txt))]:
                                    try:
                                        userData = pickle.load(open("SAVE_DATA/Users/"+str(username_txt)+".txt","rb"))
                                        print(userData)
                                    except FileNotFoundError:
                                        print("please sign up")
                                    else:
                                        updateValues(userData)
                                        mainmenuscreen = True
                                        done = True
                                        loginscreen = False
                                else:
                                    print("wrong password")
                            else:
                                print('wrong username')

                        elif event.key == pg.K_BACKSPACE:
                            username_txt = username_txt[:-1]
                        else:
                            username_txt += event.unicode

                    elif state == "password":
                        if event.key == pg.K_RETURN:
                            password_box_color = color_inactive
                            if username_txt in usernames:
                                if password_txt == passwords[int(usernames.index(username_txt))]:
                                    try:
                                        userData = pickle.load(open("SAVE_DATA/Users/"+str(username_txt)+".txt","rb"))
                                        print(userData)
                                    except FileNotFoundError:
                                        print("please sign up")
                                    else:
                                        updateValues(userData)
                                        mainmenuscreen = True
                                        done = True
                                        loginscreen = False
                                else:
                                    print("wrong password")
                            else:
                                print('wrong username')

                        elif event.key == pg.K_BACKSPACE:
                            password_txt = password_txt[:-1]
                            password_txtStar = password_txtStar[:-1]
                        else:
                            password_txt +=event.unicode
                            password_txtStar += "*"

        screen.fill((30,30,30))

        #render the current text
        username_txt_surface =  font.render(username_txt,True,username_box_color)
        Login_Button_txt_surface = font.render(Login_Button_txt,True,Login_Button_color) 
        password_txtStar_surface = font.render(password_txtStar,True,password_box_color)
        SignUp_Button_txt_surface = font.render(SignUp_Button_txt,True,SignUp_Button_color)

        #blit the text
        screen.blit(username_txt_surface,(username_box.x+5,username_box.y+5))
        screen.blit(Login_Button_txt_surface,(Login_Button.x+5,Login_Button.y+5))
        screen.blit(password_txtStar_surface,(password_box.x+5,password_box.y+5))
        screen.blit(SignUp_Button_txt_surface,(SignUp_Button.x+5,SignUp_Button.y+5))


        #blit the buttons
        pg.draw.rect(screen,Login_Button_color,Login_Button,2)
        pg.draw.rect(screen,username_box_color,username_box,2)
        pg.draw.rect(screen,password_box_color,password_box,2)
        pg.draw.rect(screen,SignUp_Button_color,SignUp_Button,2)

        #FPS COUNTER
        FPS_counter_surface = font_fps.render(str(math.floor(FPS))+"FPS",True,color_fps)
        screen.blit(FPS_counter_surface,(area.width-FPS_counter_surface.get_width(),0))
        count_fps()

        #statics
        pg.display.flip()
        clock.tick(100)
        

def saveValues():
    #saves the values when user is done playing. Happens when user exits the game screen
    global saveData
    print(saveData)
    pickle.dump(saveData,open("SAVE_DATA/Users/"+str(username_txt)+".txt","wb"))

def performanceScore(performancePoints):
    #checks if the new performance is bigger than any performance in the list saveData[3] which is a list of best 10
    performancePoints = round(performancePoints,2)
    global saveData, playerPerformace,accuracy,playerAccuracy
    playerPerformace = (saveData[3][0])*1.00 + (saveData[3][1])*0.95 + (saveData[3][2])*0.90 + (saveData[3][3])*0.86 + (saveData[3][4])*0.81 + (saveData[3][5])*0.77 + (saveData[3][6])*0.74 + (saveData[3][7])*0.70 + (saveData[3][8])*0.66 + (saveData[3][9])*0.63
    temporaryList = saveData[3] #list for the values
    temporaryList2 = saveData[4] #list for the difficulties
    temporaryList3 = saveData[6] #list for the accuracy
    del saveData[3]
    del saveData[3]
    del saveData[4]
    i = 0
    checking = True
    while i < len(temporaryList) and checking:
        if performancePoints > temporaryList[i]:
            print(performancePoints)
            temporaryList.insert(i,performancePoints)
            temporaryList3.insert(i,accuracy[2])
            if globalDifficulty == 'easyDictionary':
                temporaryList2.insert(i,"easy")
            elif globalDifficulty == "normalDictionary":
                temporaryList2.insert(i,"normal")
            elif globalDifficulty == "hardDictionary":
                temporaryList2.insert(i,"hard")
            del temporaryList[10] #if a new score has been added, the lowest score is removed
            del temporaryList2[10] #same thing with the difficulty fo that score
            del temporaryList3[10] #same thing with the previus 2 lists
            checking = False
        else:
            i+= 1
    print(performancePoints) #prints the updated list for testing
    saveData.insert(3,temporaryList)
    saveData.insert(4,temporaryList2)
    saveData.insert(6,temporaryList3)
    #adding the weights to the performance where best score is worth 100% and lowest is worth 63%
    playerAccuracy = round(sum(saveData[6])/10,2)
    playerPerformace = (saveData[3][0])*1.00 + (saveData[3][1])*0.95 + (saveData[3][2])*0.90 + (saveData[3][3])*0.86 + (saveData[3][4])*0.81 + (saveData[3][5])*0.77 + (saveData[3][6])*0.74 + (saveData[3][7])*0.70 + (saveData[3][8])*0.66 + (saveData[3][9])*0.63
    playerPerformace = round(playerPerformace,2)
    #this increases the xp based on the score achieved and checks to see if the player leveled up
    saveData[5][2] = round(((saveData[5][0] * saveData[5][0] * saveData[5][0])/15 + 500),1)
    saveData[5][1] = round(saveData[5][1] + performancePoints,1)
    round(saveData[5][1],1)

    while saveData[5][1] >= saveData[5][2]:
        saveData[5][1] -= saveData[5][2]
        round(saveData[5][1],1)
        saveData[5][0] += 1
    
    #adding the typing speed for the previous race to the players average
    temporaryList = saveData[7]
    temporaryList.insert(0,typing_speed)
    if len(temporaryList) >= 21:
        del temporaryList[20]
    try:
        temporaryList.remove(0)
    except ValueError:
        pass
    saveData[7] = temporaryList

    #this checks if its the best score across all accounts
    i = 0
    checking = True
    temporaryList = global_highscores[1] #this is the score
    temporaryList2 = global_highscores[2] #this is the difficulty
    temporaryList3 = global_highscores[0] #this is the username
    print(global_highscores)
    while i < len(temporaryList) and checking:
        if performancePoints > temporaryList[i]:
            temporaryList.insert(i,performancePoints)
            if globalDifficulty == 'easyDictionary':
                temporaryList2.insert(i,"easy")
            elif globalDifficulty == "normalDictionary":
                temporaryList2.insert(i,"normal")
            elif globalDifficulty == "hardDictionary":
                temporaryList2.insert(i,"hard")
            temporaryList3.insert(i,username_txt)
            del temporaryList[10]
            del temporaryList2[10]
            del temporaryList3[10]
            checking = False
        else:
            i += 1
    global_highscores[1] = temporaryList
    global_highscores[2] = temporaryList2
    global_highscores[0] = temporaryList3
    print(global_highscores)
    pickle.dump(global_highscores,open("SAVE_DATA/Game_Data/highscores.txt","wb"))

    temporaryList = global_performance[0] #names
    temporaryList2 = global_performance[1] #performance
    temporaryList3 = global_performance[2] #level
    print(temporaryList3)

    if username_txt in temporaryList:
        Loc = temporaryList.index(username_txt)
        if playerPerformace >= temporaryList2[Loc]:
            del temporaryList[Loc]
            del temporaryList2[Loc]
            del temporaryList3[Loc]
            for i in range(0,len(temporaryList2)):
                if playerPerformace >= temporaryList2[i]:
                    temporaryList2.insert(i,playerPerformace)
                    temporaryList.insert(i,username_txt)
                    temporaryList3.insert(i,saveData[5][0])
                    break
                else:
                    i += 1
    else:
        for i in range(0,len(temporaryList2)):
            if playerPerformace >= temporaryList2[i]:
                temporaryList2.insert(i,playerPerformace)
                temporaryList.insert(i,username_txt)
                temporaryList3.insert(i,saveData[5][0])
                del temporaryList2[10]
                del temporaryList[10]
                print(temporaryList3)
                del temporaryList3[10]
                break
            else:
                i += 1
    global_performance[0] = temporaryList
    global_performance[1] = temporaryList2
    global_performance[2] = temporaryList3


    pickle.dump(global_performance,open("SAVE_DATA/Game_Data/performance.txt","wb"))
    print(global_performance)

        


#variables for the main program loop
loginscreen = True
mainmenuscreen = False
gamescreen = False
difficultyselectscreen = False
globalDifficulty = " "
endgamescreen = False
makeDifficulty()
running = True

#main program loop
while running:
    if loginscreen:
        loginScreen()
    elif mainmenuscreen:
        mainmenuScreen()
    elif gamescreen:
        gameScreen()
    elif endgamescreen:
        endgameScreen()
    elif difficultyselectscreen:
        difficultySelectScreen()
    


