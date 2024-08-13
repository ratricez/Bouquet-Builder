##########################################################
# Title: Bouquet Builder                                 #
# Author: Elaine Zhu                                     #
# Purpose: A game that allows you to pick the            #
#          prettiest flowers and make a custom bouquet   #
##########################################################

from tkinter import *                                    
from math import *  #only if you need sqrt, pi, sin, cos or tan
from time import *
from random import *
from DecimalToHex import *


root = Tk()
screen = Canvas(root, width=800, height=600, background="#D9EEFF")
screen.pack()

def setInitialValues():
    #global variables...
    global BlueTulipDisplay1, BlueTulipDisplay2, PinkTulipDisplay1, PinkTulipDisplay2, SunflowerDisplay1, SunflowerDisplay2, LilyDisplay1, LilyDisplay2, LilyoftheValleyDisplay1, LilyoftheValleyDisplay2, LavendarDisplay1, LavendarDisplay2, BBDisplay1, BBDisplay2, displayScreen, SBlueTulipDisplay, SPinkTulipDisplay, SLilyoftheValleyDisplay, SLavendarDisplay, SLilyDisplay, SSunflowerDisplay, SBBDisplay, BBDisplay, SunflowerDisplay, LilyDisplay, LavendarDisplay, LilyoftheValleyDisplay, BlueTulipDisplay, PinkTulipDisplay
  
    global BouquetBuilderDisplay, introScreen
    
    global fieldScreen, flowerXmove, flowers, flowertypecount, hearts
    
    global ruleScreen, inventoryScreen, xsparkle, ysparkle, sizesparkle
    
    global colours, popups, Bow1, Bow2, Bow3, Bow1L, Bow2L, Bow3L, bows, cancel, accessories
    
    global squarex, GrassDisplay, inframel, inframer, flowersstat, flowercount
    
    global xgrass, ygrass, grassflower, grassheight, grasscolour, flowercolour

    
    #Flower Displays (3 versions of each)    
    BBDisplay = PhotoImage(file = 'BabyBreaths.png')
    SunflowerDisplay = PhotoImage(file = 'Sunflower.png')
    LilyDisplay = PhotoImage(file = 'Lily.png')
    LavendarDisplay = PhotoImage(file = 'Lavendar.png')
    LilyoftheValleyDisplay = PhotoImage(file = 'LilyoftheValley.png')
    BlueTulipDisplay = PhotoImage(file = 'BlueTulip.png')
    PinkTulipDisplay = PhotoImage(file = 'PinkTulip.png')
    BouquetBuilderDisplay = PhotoImage(file = 'bouquetbuilder.png')
    GrassDisplay = PhotoImage(file = 'grass.png')

    BBDisplay1 = PhotoImage(file = 'BabyBreaths1.png')
    LavendarDisplay1 = PhotoImage(file = 'Lavendar1.png')
    LilyoftheValleyDisplay1 = PhotoImage(file = 'LilyoftheValley1.png')
    LilyDisplay1 = PhotoImage(file = 'Lily1.png')
    SunflowerDisplay1 = PhotoImage(file = 'Sunflower1.png')
    PinkTulipDisplay1 = PhotoImage(file = 'PinkTulip1.png')
    BlueTulipDisplay1 = PhotoImage(file = 'BlueTulip1.png')
    
    BBDisplay2 = PhotoImage(file = 'BabyBreaths2.png')
    LavendarDisplay2 = PhotoImage(file = 'Lavendar2.png')
    LilyoftheValleyDisplay2 = PhotoImage(file = 'LilyoftheValley2.png')
    LilyDisplay2 = PhotoImage(file = 'Lily2.png')
    SunflowerDisplay2 = PhotoImage(file = 'Sunflower2.png')
    PinkTulipDisplay2 = PhotoImage(file = 'PinkTulip2.png')
    BlueTulipDisplay2 = PhotoImage(file = 'BlueTulip2.png')

    #Small Display of Flowers for Field Screen + Inventory
    SBBDisplay = PhotoImage(file = 'BabyBreathSmall.png')
    SSunflowerDisplay = PhotoImage(file = 'SunflowerSmall.png')
    SLilyDisplay = PhotoImage(file = 'LilySmall.png')
    SLavendarDisplay = PhotoImage(file = 'LavendarSmall.png')
    SLilyoftheValleyDisplay = PhotoImage(file = 'LilyoftheValleySmall.png')
    SBlueTulipDisplay = PhotoImage(file = 'BlueTulipSmall.png')
    SPinkTulipDisplay = PhotoImage(file = 'PinkTulipSmall.png')

    #Accessories
    Bow1 = PhotoImage(file = "Bow1.png")
    Bow2 = PhotoImage(file = "Bow2.png")
    Bow3 = PhotoImage(file = "Bow3.png")
    Bow1L = PhotoImage(file = "Bow1L.png")
    Bow2L = PhotoImage(file = "Bow2L.png")
    Bow3L = PhotoImage(file = "Bow3L.png")
    cancel = PhotoImage(file = "cancel.png")
    hearts = PhotoImage(file = "Hearts.png")

    #Variables to help move field and keep track of how many flowers + which ones are picked
    flowerXmove = 0
    flowercount = 0
    flowertypecount = [0, 0, 0, 0, 0, 0, 0]
    flowers = {}
    flowersstat = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,]

    #Variables to keep track of which screen should be shown
    introScreen = True
    displayScreen = False
    ruleScreen = False
    fieldScreen = False
    inventoryScreen = False
    
    #Variables to keep track of which accessories/background colours are chosen
    colours = [False, False, False, False, False, False]
    bows = [False, False, False]
    accessories = [False, False]
    
    #Moving left and right, parameters, popups
    squarex = 0
    inframel = True
    inframer = True
    squaretest = 0
    popups = True
    
    #Gets random x and y values + size for sparkle accessory
    xsparkle = []
    ysparkle = []
    sizesparkle = []
    
    for i in range(100):
        xsparkle.append(uniform(50, 420))
        ysparkle.append(uniform(50, 550))
        sizesparkle.append(uniform(2, 5))
        
    #Opinions for intro screen grass + flower colour
    grasscolours = ["#42941c", "#5fa140", "#396e21", "#2e730f", "#57b82c", "#3cb53a"]
    flowercolours = ["#d485cd", "#eab9f0", "#f57faa", "#f7bb65", "#e9ed6f"]

    #Lists that will store the random values for intro screen
    xgrass = []
    ygrass = []
    grassflower = []
    grassheight = []
    grasscolour = []
    flowercolour = []
    
    #Random values for grass x + y, colours and heights
    for i in range(100):
        grassflower.append(randint(0, 1))
        xgrass.append(uniform(0, 800))
        ygrass.append(uniform(510, 598))
        grassheight.append(uniform(18, 25))
        grasscolour.append(grasscolours[randint(0, 5)])
        flowercolour.append(flowercolours[randint(0, 4)])

        


#Intro Screen
def drawIntroScreen():
    title = screen.create_image(400, 250, image = BouquetBuilderDisplay, anchor = CENTER)
    slogan = screen.create_text(400, 315, text = "~make the prettiest bouquets~", fill = "#FF9195", font = ("Arial", 17))
    
    #Buttons
    screen.create_rectangle(220, 350, 380, 390, fill = "#FAF3E3")
    screen.create_text(300, 370, text = "PLAY", fill = "#FF9195", font = ("Arial", 17))
    
    screen.create_rectangle(420, 350, 580, 390, fill = "#FAF3E3")
    screen.create_text(500, 370, text = "RULES", fill = "#FF9195", font = ("Arial", 17))

    #Grass
    screen.create_rectangle(0,500, 800, 600, fill = "#2d8504", outline = "")

    for i in range(100):
        screen.create_line(xgrass[i], ygrass[i], xgrass[i], ygrass[i]-grassheight[i], fill = grasscolour[i])
        #If the random value is 0, add a flower!
        if grassflower[i] == 0:
            screen.create_oval(xgrass[i]-5, ygrass[i]-grassheight[i]-10, xgrass[i]+5, ygrass[i]-grassheight[i], fill = flowercolour[i], outline = "")
            
#Rule Screen
def drawRuleScreen():
    #The boxes
    screen.create_rectangle(100, 100, 700, 500, fill = "#8dbce3", outline = "")
    screen.create_rectangle(110, 110, 690, 490, fill = "#bedefa", outline = "")

    screen.create_text(400, 170, text = "Instructions", fill = "White", font = ("FreeMono Bold", 25))
    screen.create_text(400, 220, text = "Explore the fields and pick your favourite 6 flowers \n Then decorate your unique bouquet!", fill = "White", justify = CENTER,font = ("FreeMono Bold", 12))
    
    screen.create_text(400, 280, text = "Controls", fill = "White", font = ("FreeMono Bold", 25))
    screen.create_text(135, 140, text = "X", fill = "#8dbce3", font = ("FreeMono Bold", 25))
    
    #The keyboard visual
    i = 40
    screen.create_rectangle(150+i, 380, 200+i, 430, fill = "Pink", outline = "#8dbce3", width = 3)
    screen.create_rectangle(210+i, 380, 260+i, 430, fill = "White", outline = "#8dbce3", width = 3)
    screen.create_rectangle(270+i, 380, 320+i, 430, fill = "Pink", outline = "#8dbce3", width = 3)
    screen.create_rectangle(210+i, 320, 260+i, 370, fill = "White", outline = "#8dbce3", width = 3)
    screen.create_text(275, 460, text = "A & D or <-- & -->\nto move left and right", fill = "White", justify = CENTER,font = ("FreeMono Bold", 10))

    #Key Labels
    screen.create_text(215, 407, text = "A\n<--", fill = "White", font = ("FreeMono Bold", 12), justify = CENTER)
    screen.create_text(335, 407, text = "D\n-->", fill = "White", font = ("FreeMono Bold", 12), justify = CENTER)

    #Mouse visual
    screen.create_oval(490, 320, 575, 430, fill = "White", outline = "#8dbce3", width = 3)
    screen.create_arc(490, 320, 571, 422, start = 90, extent = 90, fill = "Pink", outline = "")
    screen.create_oval(490, 320, 575, 430, fill = "", outline = "#8dbce3", width = 3)

    screen.create_line(532.5, 320, 532.5, 371, fill = "#8dbce3", width = 4)
    screen.create_text(532.5, 460, text = "Left click to pick up flowers", fill = "White", justify = CENTER,font = ("FreeMono Bold", 10))

#Flower Field Screen
def drawFieldScreen():
    global squarex, squaretest, flowers, flowersstat
    
    #Background gradient
    if True:
        #Blue Shade
        R1 = 188
        G1 = 224
        B1 = 253
        #Yellow Shade
        R2 = 235
        G2 = 226
        B2 = 179
        for i in range(0, 200, 2):
            colour = str(getPythonColor(R1,G1,B1))
            screen.create_rectangle(0, i, 800, i+3, fill = colour, outline = colour)
            
            R1 += 47/100
            G1 += 2/100
            B1 -= 74/100
    
        #Yellow Shade
        R1 = 235
        G1 = 226
        B1 = 179
        #Pink Shade
        R2 = 239
        G2 = 188
        B2 = 177
        for i in range(200, 600, 4):
            colour = str(getPythonColor(R1,G1,B1))
            screen.create_rectangle(0, i, 800, i+3, fill = colour, outline = colour)
            R1 += 4/100
            G1 -= 38/100
            B1 -= 2/100

    #Grass
    grass = screen.create_image(400+squarex, 450, image = GrassDisplay)

    #Arrows
    screen.create_text(50, 300, text = "<", fill ="#FF9195", font = ("Arial", 35))
    screen.create_text(750, 300, text = ">", fill ="#FF9195", font = ("Arial", 35))

    #Check if each flower still exists (True), if it does, display it
    if flowersstat[0] == True: 
        BB1 = screen.create_image(270+squarex, 500, image = SBBDisplay, anchor = W)
    if flowersstat[1] == True:
        BB2 = screen.create_image(-330+squarex, 500, image = SBBDisplay, anchor = W)
    if flowersstat[2] == True:
        BB3 = screen.create_image(1500+squarex, 500, image = SBBDisplay, anchor = W)
    if flowersstat[3] == True:
        S1 = screen.create_image(950+squarex, 510, image = SSunflowerDisplay, anchor = W)
    if flowersstat[4] == True:
        S2 = screen.create_image(-190+squarex, 510, image = SSunflowerDisplay, anchor = W)
    if flowersstat[5] == True:
        S3 = screen.create_image(-620+squarex, 510, image = SSunflowerDisplay, anchor = W)
    if flowersstat[6] == True:
        L1 = screen.create_image(570+squarex, 540, image = SLilyDisplay, anchor = W)
    if flowersstat[7] == True:
        L2 = screen.create_image(1355+squarex, 540, image = SLilyDisplay, anchor = W)
    if flowersstat[8] == True:
        L3 = screen.create_image(-915+squarex, 540, image = SLilyDisplay, anchor = W)
    if flowersstat[9] == True:
        La1 = screen.create_image(-790+squarex, 500, image = SLavendarDisplay, anchor = W)
    if flowersstat[10] == True:
        La2 = screen.create_image(860+squarex, 500, image = SLavendarDisplay, anchor = W)
    if flowersstat[11] == True:
        La3 = screen.create_image(squarex, 500, image = SLavendarDisplay, anchor = W)
    if flowersstat[12] == True:
        Lotv1 = screen.create_image(1120+squarex, 530, image = SLilyoftheValleyDisplay, anchor = W)
    if flowersstat[13] == True:
        Lotv2 = screen.create_image(-460+squarex, 530, image = SLilyoftheValleyDisplay, anchor = W)
    if flowersstat[14] == True:
        Lotv3 = screen.create_image(710+squarex, 530, image = SLilyoftheValleyDisplay, anchor = W)
    if flowersstat[15] == True:
        BT1 = screen.create_image(100+squarex, 530, image = SBlueTulipDisplay, anchor = W)
    if flowersstat[16] == True:
        BT2 = screen.create_image(-1040+squarex, 530, image = SBlueTulipDisplay, anchor = W)
    if flowersstat[17] == True:
        BT3 = screen.create_image(1250+squarex, 530, image = SBlueTulipDisplay, anchor = W)
    if flowersstat[18] == True:
        PT1 = screen.create_image(1640+squarex, 530, image = SPinkTulipDisplay, anchor = W)
    if flowersstat[19] == True:
        PT2 = screen.create_image(420+squarex, 530, image = SPinkTulipDisplay, anchor = W)
    if flowersstat[20] == True:
        PT2 = screen.create_image(-720+squarex, 530, image = SPinkTulipDisplay, anchor = W)

    #Key Value Dictionary for all coordinates of flowers
    flowers = {"BB1": 270+squarex, "BB2": -330+squarex, "BB3": 1500+squarex,
            "S1": 950+squarex, "S2": -190+squarex, "S3": -620+squarex,
            "L1": 570+squarex, "L2": 1355+squarex, "L3": -915+squarex,
            "La1": -830+squarex, "La2": 820+squarex, "La3": -40+squarex,
            "Lotv1": 1120+squarex, "Lotv2": -460+squarex, "Lotv3": 710+squarex,
            "BT1": 100+squarex, "BT2": -1040+squarex, "BT3": 1250+squarex,
            "PT1": 1640+squarex, "PT2": 420+squarex, "PT3": -720+squarex,
    }
    
    #Total display
    screen.create_text(700, 70, text = "Total:", fill ="#FF9195", font = ("Arial", 20))
    screen.create_text(750, 70, text = str(flowercount), fill ="#FF9195", font = ("Arial", 20))
    
    #Next Screen Button
    screen.create_rectangle(630, 540, 760, 570, fill = "#FAF3E3")
    screen.create_text(695, 555, text = "NEXT", fill ="#FF9195", font = ("Arial", 13))

    #Inventory Button
    screen.create_rectangle(50, 50, 100, 100, fill = "#FAF3E3")

    #Inventory Icon
    screen.create_rectangle(60, 70, 90, 90, fill = "", width = 2)
    screen.create_rectangle(70, 60 ,80, 70, fill = "", width = 2)

#Inventory Screen
def drawInventoryScreen():
    global flowertypecount
    
    #Background Gradient
    if True:
        #Blue Shade
        R1 = 188
        G1 = 224
        B1 = 253
        #Yellow Shade
        R2 = 235
        G2 = 226
        B2 = 179
        for i in range(0, 200, 2):
            colour = str(getPythonColor(R1,G1,B1))
            screen.create_rectangle(0, i, 800, i+3, fill = colour, outline = colour)
            
            R1 += 47/100
            G1 += 2/100
            B1 -= 74/100
    
        #Yellow Shade
        R1 = 235
        G1 = 226
        B1 = 179
        #Pink Shade
        R2 = 239
        G2 = 188
        B2 = 177
        for i in range(200, 600, 4):
            colour = str(getPythonColor(R1,G1,B1))
            screen.create_rectangle(0, i, 800, i+3, fill = colour, outline = colour)
            R1 += 4/100
            G1 -= 38/100
            B1 -= 2/100

    grass = screen.create_image(400, 450, image = GrassDisplay)

    #Back panel
    screen.create_rectangle(30, 30, 770, 500, fill = "#FAF3E3")

    #Exit button
    screen.create_rectangle(50, 50, 100, 100, fill = "#FAF3E3")
    
    #X
    screen.create_text(75, 75, text = "X", fill = "Black", font = ("Arial", 30))


    #Flowers + how many have been picked up
    screen.create_image(230, 150, image = SBBDisplay, anchor = CENTER)
    screen.create_text(270, 240, text = str(flowertypecount[0])+"x", fill = "Black", font = ("Arial", 20))
    
    screen.create_image(410, 150, image = SSunflowerDisplay, anchor = CENTER)
    screen.create_text(450, 240, text = str(flowertypecount[1])+"x", fill = "Black", font = ("Arial", 20))

    screen.create_image(600, 175, image = SLilyDisplay, anchor = CENTER)
    screen.create_text(640, 240, text = str(flowertypecount[2])+"x", fill = "Black", font = ("Arial", 20))
    
    screen.create_image(130, 370, image = SLavendarDisplay, anchor = CENTER)
    screen.create_text(160, 460, text = str(flowertypecount[3])+"x", fill = "Black", font = ("Arial", 20))
    
    screen.create_image(325, 395, image = SLilyoftheValleyDisplay, anchor = CENTER)
    screen.create_text(375, 460, text = str(flowertypecount[4])+"x", fill = "Black", font = ("Arial", 20))

    screen.create_image(505, 410, image = SBlueTulipDisplay, anchor = CENTER)
    screen.create_text(535, 460, text = str(flowertypecount[5])+"x", fill = "Black", font = ("Arial", 20))
    
    screen.create_image(660, 405, image = SPinkTulipDisplay, anchor = CENTER)
    screen.create_text(710, 460, text = str(flowertypecount[6])+"x", fill = "Black", font = ("Arial", 20))


#Drawing the Bouquet
def drawDisplayBouquet():
    global flowertypecount
    #The selection pallets
    i = 20
    screen.create_polygon(500, 100-i, 520, 100-i, 730, 100-i, 750, 100-i, 750, 120-i, 750, 260-i, 750, 280-i, 730, 280-i, 520, 280-i, 500, 280-i, 500, 260-i, 500, 120-i, fill = "#80664B", smooth = True, outline = "")
    screen.create_polygon(500, 300+i, 520, 300+i, 730, 300+i, 750, 300+i, 750, 320+i, 750, 460+i, 750, 480+i, 730, 480+i, 520, 480+i, 500, 480+i, 500, 460+i, 500, 320+i, fill = "#80664B", smooth = True, outline = "")

    #Colour selector
    screen.create_polygon(512, 100, 522, 100, 567, 100, 577, 100, 577, 110, 577, 150, 577, 160, 567, 160, 522, 160, 512, 160, 512, 150, 512, 110, fill = "#DCDEDD", outline = "", smooth = True)
    screen.create_polygon(512+80, 100, 522+80, 100, 567+80, 100, 577+80, 100, 577+80, 110, 577+80, 150, 577+80, 160, 567+80, 160, 522+80, 160, 512+80, 160, 512+80, 150, 512+80, 110, fill = "#FAF3E3", outline = "", smooth = True)
    screen.create_polygon(512+160, 100, 522+160, 100, 567+160, 100, 577+160, 100, 577+160, 110, 577+160, 150, 577+160, 160, 567+160, 160, 522+160, 160, 512+160, 160, 512+160, 150, 512+160, 110, fill = "#D9EEFF", outline = "", smooth = True)

    screen.create_polygon(512, 180, 522, 180, 567, 180, 577, 180, 577, 190, 577, 230, 577, 240, 567, 240, 522, 240, 512, 240, 512, 230, 512, 190, fill = "#FFEEF9", outline = "", smooth = True)
    screen.create_polygon(512+80, 180, 522+80, 180, 567+80, 180, 577+80, 180, 577+80, 190, 577+80, 230, 577+80, 240, 567+80, 240, 522+80, 240, 512+80, 240, 512+80, 230, 512+80, 190, fill = "#f5eba2", outline = "", smooth = True)
    screen.create_polygon(512+160, 180, 522+160, 180, 567+160, 180, 577+160, 180, 577+160, 190, 577+160, 230, 577+160, 240, 567+160, 240, 522+160, 240, 512+160, 240, 512+160, 230, 512+160, 190, fill = "#DCF6D0", outline = "", smooth = True)

    
    #Accessories
    j = 240
    screen.create_polygon(512, 100+j, 522, 100+j, 567, 100+j, 577, 100+j, 577, 110+j, 577, 150+j, 577, 160+j, 567, 160+j, 522, 160+j, 512, 160+j, 512, 150+j, 512, 110+j, fill = "#FAF3E3", outline = "", smooth = True)
    screen.create_polygon(512+80, 100+j, 522+80, 100+j, 567+80, 100+j, 577+80, 100+j, 577+80, 110+j, 577+80, 150+j, 577+80, 160+j, 567+80, 160+j, 522+80, 160+j, 512+80, 160+j, 512+80, 150+j, 512+80, 110+j, fill = "#FAF3E3", outline = "", smooth = True)
    screen.create_polygon(512+160, 100+j, 522+160, 100+j, 567+160, 100+j, 577+160, 100+j, 577+160, 110+j, 577+160, 150+j, 577+160, 160+j, 567+160, 160+j, 522+160, 160+j, 512+160, 160+j, 512+160, 150+j, 512+160, 110+j, fill = "#FAF3E3", outline = "", smooth = True)

    screen.create_polygon(512, 180+j, 522, 180+j, 567, 180+j, 577, 180+j, 577, 190+j, 577, 230+j, 577, 240+j, 567, 240+j, 522, 240+j, 512, 240+j, 512, 230+j, 512, 190+j, fill = "#FAF3E3", outline = "", smooth = True)
    screen.create_polygon(512+80, 180+j, 522+80, 180+j, 567+80, 180+j, 577+80, 180+j, 577+80, 190+j, 577+80, 230+j, 577+80, 240+j, 567+80, 240+j, 522+80, 240+j, 512+80, 240+j, 512+80, 230+j, 512+80, 190+j, fill = "#FAF3E3", outline = "", smooth = True)
    screen.create_polygon(512+160, 180+j, 522+160, 180+j, 567+160, 180+j, 577+160, 180+j, 577+160, 190+j, 577+160, 230+j, 577+160, 240+j, 567+160, 240+j, 522+160, 240+j, 512+160, 240+j, 512+160, 230+j, 512+160, 190+j, fill = "#FAF3E3", outline = "", smooth = True)
    
    #Accessory Icons
    bow1 = screen.create_image(520, 370, image = Bow1, anchor = W )
    bow2 = screen.create_image(600, 370, image = Bow2, anchor = W )
    bow3 = screen.create_image(680, 370, image = Bow3, anchor = W )
    cancelicon = screen.create_image(680, 450, image = cancel, anchor = W)
    sparkle = screen.create_polygon(524, 450, 538, 443, 544, 430, 550, 443, 564, 450, 550, 457, 544, 470, 538, 457, fill = "#f5c242")
    heart = screen.create_polygon(621, 438, 624, 442, 627, 438, 634, 435, 644, 440, 639, 457, 624, 470, 609, 457, 604, 440, 614, 435, smooth = True, fill = "Pink")

    #Check how many of each flower is picked, display which ones are
        #If more than one, use a different image so it doesn't overlap
    if flowertypecount[0] >= 1:
        BB = screen.create_image(216, 300, image = BBDisplay, anchor = CENTER )
    if flowertypecount[0] >= 2:
        BB1 = screen.create_image(205, 300, image = BBDisplay1, anchor = CENTER )
    if flowertypecount[0] >= 3:
        BB2 = screen.create_image(228, 290, image = BBDisplay2, anchor = CENTER )
    if flowertypecount[3] >= 1:
        La = screen.create_image(220, 320, image = LavendarDisplay, anchor = CENTER)
    if flowertypecount[3] >= 2:
        La1 = screen.create_image(210, 335, image = LavendarDisplay1, anchor = CENTER)
    if flowertypecount[3] >= 3:
        La2 = screen.create_image(210, 335, image = LavendarDisplay2, anchor = CENTER)
    if flowertypecount[4] >= 1:
        Lotv = screen.create_image(225, 316, image = LilyoftheValleyDisplay, anchor = CENTER )
    if flowertypecount[4] >= 2:
        Lotv1 = screen.create_image(240, 320, image = LilyoftheValleyDisplay1, anchor = CENTER )
    if flowertypecount[4] >= 3:
        Lotv2 = screen.create_image(228, 320, image = LilyoftheValleyDisplay2, anchor = CENTER )
    if flowertypecount[2] >= 1:
        L = screen.create_image(222, 327, image = LilyDisplay, anchor = CENTER )
    if flowertypecount[2] >= 2:
        L1 = screen.create_image(202, 336, image = LilyDisplay1, anchor = CENTER )
    if flowertypecount[2] >= 3:
        L2 = screen.create_image(212, 346, image = LilyDisplay2, anchor = CENTER )
    if flowertypecount[1] >= 1:
        S = screen.create_image(220, 330, image = SunflowerDisplay, anchor = CENTER )
    if flowertypecount[1] >= 2:
        S1 = screen.create_image(238, 334, image = SunflowerDisplay2, anchor = CENTER )
    if flowertypecount[1] >= 3:
        S2 = screen.create_image(228, 340, image = SunflowerDisplay1, anchor = CENTER )
    if flowertypecount[5] >= 1:
        BT1 = screen.create_image(215, 350, image = BlueTulipDisplay1, anchor = CENTER )
    if flowertypecount[5] >= 2:
        BT = screen.create_image(233, 370, image = BlueTulipDisplay, anchor = CENTER )
    if flowertypecount[5] >= 3:
        BT2 = screen.create_image(200, 370, image = BlueTulipDisplay2, anchor = CENTER )
    if flowertypecount[6] >= 1:
        PT2 = screen.create_image(243, 375, image = PinkTulipDisplay2, anchor = CENTER )
    if flowertypecount[6] >= 2:
        PT1 = screen.create_image(223, 370, image = PinkTulipDisplay1, anchor = CENTER )
    if flowertypecount[6] >= 3:
        PT = screen.create_image(207, 370, image = PinkTulipDisplay, anchor = CENTER )

    #Restart button
    screen.create_rectangle(630, 540, 760, 570, fill = "#FAF3E3")
    screen.create_text(695, 555, text = "RESTART", fill ="#FF9195", font = ("Arial", 13))

#Updating objects (left + right on Field Screen)
def updateObjects():
    global squarex, squarey, inframel, inframer
    
    #While you are anywhere that isn't the end of screen, move
    if squarex < 1000 and squarex > -1000:
        squarex += flowerXmove
        inframel = True
        inframer = True
    #If you are at the right most, don't let user continue right
    elif squarex >= 1000:
        inframel = False
        if flowerXmove > 0:
            squarex = squarex
        else:
            squarex += flowerXmove
    #If you are left most, don't let user continue left
    elif squarex <= -1000:
        inframer = False
        if flowerXmove < 0:
            squarex = squarex
        else:
            squarex += flowerXmove
        
#Update the background colours for display screen (based on selection by user)
def updateColours():
    if colours[0] == True:
        screen.create_rectangle(0, 0 ,800, 600, fill = "#DCDEDD", outline = "" )
    elif colours[1] == True:
        screen.create_rectangle(0, 0 ,800, 600, fill = "#FAF3E3", outline = "" )
    elif colours[2] == True:
        screen.create_rectangle(0, 0 ,800, 600, fill = "#D9EEFF", outline = "" )
    elif colours[3] == True:
        screen.create_rectangle(0, 0 ,800, 600, fill = "#FFEEF9", outline = "" )
    elif colours[4] == True:
        screen.create_rectangle(0, 0 ,800, 600, fill = "#f5eba2", outline = "" )
    elif colours[5] == True:
        screen.create_rectangle(0, 0 ,800, 600, fill = "#DCF6D0", outline = "" )
    
#Update the general accessories like bows, sparkles and heart
def updateBows():
    #If the icon is clicked, the variable will be True, thus display it
    if bows[0] == True:
        screen.create_image(223, 460, image = Bow1L, anchor = CENTER)
    elif bows[1] == True:
        screen.create_image(223, 460, image = Bow2L, anchor = CENTER)
    elif bows[2] == True:
        screen.create_image(223, 465, image = Bow3L, anchor = CENTER)

    if accessories[0] == True:
        for i in range(100):
            screen.create_oval(xsparkle[i], ysparkle[i], xsparkle[i]+sizesparkle[i], ysparkle[i]+sizesparkle[i], fill = "#fffd21", outline = "White", width = 1)
    if accessories[1] == True:
        screen.create_image(340, 150, image = hearts, anchor = CENTER)
        
#Whenever user clicks...
def mouseClickHandler( event ):
    global bows, accessories, popups, introScreen, inventoryScreen, displayScreen, ruleScreen, xMouse, yMouse, fieldScreen, colours
    
    global flowers, flowersstat, flowercount, flowertypecount
    xMouse = event.x
    yMouse = event.y
    
    #If it is the intro screen and they click on the play button, go to field
    if introScreen == True and 220 <= xMouse and 380 >= xMouse and 350 <= yMouse and 390 >= yMouse:
        introScreen = False
        fieldScreen = True
    
    #If intro screen and they click on rule button, go to rule page
    elif introScreen == True and 420 <= xMouse and 580 >= xMouse and 350 <= yMouse and 390 >= yMouse:
        introScreen = False
        ruleScreen = True
        
    #If on rule screen and click the X, go back to intro screen
    elif ruleScreen == True and 122 <= xMouse and 148 >= xMouse and 120 <= yMouse and 154 >= yMouse:
        ruleScreen = False
        introScreen = True
    
    #If on field screen and click next, go to display
    elif fieldScreen == True and 630 <= xMouse and 760 >= xMouse and 540 <= yMouse and 570 >= yMouse:
        fieldScreen = False
        displayScreen = True
        
    #If on field screen and they click on the inventory button, open inventory
    elif fieldScreen == True and 50 <= xMouse and 100 >= xMouse and 50 <= yMouse and 100 >= yMouse:
        inventoryScreen = True
        fieldScreen = False
    
    #If on inventory screen and click on X, go back to field
    elif inventoryScreen == True and 50 <= xMouse and 100 >= xMouse and 50 <= yMouse and 100 >= yMouse:
        inventoryScreen = False
        fieldScreen = True

    #For the display screen...
    elif displayScreen == True:
        #For the first row for 2nd brown box (bows), set value to True if they click it
        if 340 <= yMouse and 400 >= yMouse:
            if 512 <= xMouse and 577 >= xMouse:
                bows = [True, False, False]
            elif 592 <= xMouse and 657 >= xMouse:
                bows = [False, True, False]
            elif 672 <= xMouse and 737 >= xMouse:
                bows = [False, False, True]
        #For the second row for 2nd brown box (sparkles, hearts, cancel), set value = True if they click it
        elif 420 <= yMouse and 480 >= yMouse:
            if 512 <= xMouse and 577 >= xMouse:
                accessories[0] = True
            elif 592 <= xMouse and 657 >= xMouse:
                accessories[1] = True
            elif 672 <= xMouse and 737 >= xMouse:
                bows = [False, False, False]
                accessories = [False, False]

        #For colour selection, set colour to True and other colours to False if they choose one
        if 100 <= yMouse and 160 >= yMouse:
            if 512 <= xMouse and 577 >= xMouse:
                colours = [True, False, False, False, False, False]
            elif 592 <= xMouse and 657 >= xMouse:
                colours = [False, True, False, False, False, False]
            elif 672 <= xMouse and 737 >= xMouse:
                colours = [False, False, True, False, False, False]
        elif 180 <= yMouse and 240 >= yMouse:
            if 512 <= xMouse and 577 >= xMouse:
                colours = [False, False, False, True, False, False]
            elif 592 <= xMouse and 657 >= xMouse:
                colours = [False, False, False, False, True, False]
            elif 672 <= xMouse and 737 >= xMouse:
                colours = [False, False, False, False, False, True]
        elif 630 <= xMouse and 760 >= xMouse and 540 <= yMouse and 570 >= yMouse:
            runGame()
    
    #Change parameter depending on which group of 3 (some flowers are less wide)
    if fieldScreen == True:
        #Get the key and value pairs of flower coordinates
        flowervalues = list(flowers.values())
        flowerkeys = list(flowers.keys())
        if flowercount < 6:
            for i in range(len(flowervalues)):
                #i = leftmost point of 
                #i+160 = rightmost
                
                #If they click on the flower with bigger widths, add to count + make that flower False so it won't display on the field    
                if i in [0, 1, 2]:
                    if flowersstat[i] == True and flowervalues[i] <= xMouse and flowervalues[i]+160 >= xMouse and yMouse >= 400:
                        flowersstat[i] = False
                        flowercount += 1
                        
                        #Check current flower but remove the last letter (which is the number)
                        cf = flowerkeys[i][:-1]
                        
                        if cf == "BB":
                            flowertypecount[0] += 1
                        elif cf == "S":
                            flowertypecount[1] += 1
                        elif cf == "L":
                            flowertypecount[2] += 1
                        elif cf == "La":
                            flowertypecount[3] += 1
                        elif cf == "Lotv":
                            flowertypecount[4] += 1
                        elif cf == "BT":
                            flowertypecount[5] += 1
                        elif cf == "PT":
                            flowertypecount[6] += 1
                else:
                    #For smaller flowers...
                    if flowersstat[i] == True and flowervalues[i]+50 <= xMouse and flowervalues[i]+110 >= xMouse and yMouse >= 400:
                        flowersstat[i] = False
                        flowercount += 1
                        
                        cf = flowerkeys[i][:-1]
                        if cf == "BB":
                            flowertypecount[0] += 1
                        elif cf == "S":
                            flowertypecount[1] += 1
                        elif cf == "L":
                            flowertypecount[2] += 1
                        elif cf == "La":
                            flowertypecount[3] += 1
                        elif cf == "Lotv":
                            flowertypecount[4] += 1
                        elif cf == "BT":
                            flowertypecount[5] += 1
                        elif cf == "PT":
                            flowertypecount[6] += 1
        #If they are at 6 flowers and picking up more, the popup will be true...
        elif popups == True and yMouse > 400:
            popups = False

            #Print the message
            popup = screen.create_rectangle(200, 250, 600, 350, fill = "White")
            popuptext = screen.create_text(400, 300, text = "Bouquet is too full \nPlease go to next screen", fill = "#FF9195", font = ("Arial", 16))

            #Sleep the screen so they can't press anything momentarily
            screen.update()
            sleep(3)
            screen.delete(popup, popuptext)
            screen.update()
            popups = True


def keyDownHandler( event ):
    #code to run on key press...
    global flowerXmove, squarex, inframel, inframer
    
    #Set the keys to move left and right
    if event.keysym in ["a", "A", "Left"] and inframel == True :
        flowerXmove = 10
    elif event.keysym in ["d", "D", "Right"] and inframer == True:
        flowerXmove = -10

#Stop moving when they let go
def keyReleaseHandler( event ):
    global flowerXmove
    
    flowerXmove = 0

def runGame():
    #Evertime runGame is called, set the intial values
    setInitialValues() 
    
    #While true, aka forever, update the screen
    while True:
        if introScreen == True:
            drawIntroScreen()
            screen.update()
            sleep(0.03)
            screen.delete("all")
        elif displayScreen == True:
            drawDisplayBouquet()
            updateBows()
            
            screen.update()
            sleep(0.03)
            screen.delete("all")
            updateColours()  
            

        elif fieldScreen == True:
            drawFieldScreen()
        
            screen.update()
            sleep(0.03)
            screen.delete("all")
            updateObjects()  
        
        elif inventoryScreen == True:
            drawInventoryScreen()
            
            screen.update()
            sleep(0.03)
            screen.delete("all")
        elif ruleScreen == True:
            drawRuleScreen()
        
            screen.update()
            sleep(0.03)
            screen.delete("all")

#Call the runGame function
root.after( 0, runGame )

#Connecting user inputs to functions
screen.bind( "<Button-1>", mouseClickHandler )
screen.bind( "<Key>", keyDownHandler )
screen.bind( "<KeyRelease>", keyReleaseHandler )

screen.pack()
screen.focus_set()
root.mainloop()