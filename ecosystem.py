#ecosystem
import time
import math
import winsound
from graphics import *
import random

vegx = []
vegy = []
vegno = 0
timer = -1
showage = False
showveg = True
showflies = True
showsenses = False
showfood = False
showmate = False

hungeraffect = 12
maxenergy = 600
sympathy = 2 # lets flies under the age of fifteen need less food
foodweight = []
mateweight = []
x = []
y = []
energy = []
senses = []
age = []
species = []

rot = 2000
vegetables = 0
lastvegetables = vegetables
flies = 60
bats = 0
lastbats = bats
lastflies = flies
width = 50
height = 50
zoom = 10
pause = 0
border = 50
for i in range (0, flies):
    species.append ("f")
    x.append (random.randint(0, (width)))
    y.append (random.randint(0, (height)))
    foodweight.append (random.uniform(0.5, 1))
    mateweight.append (random.uniform(0.5, 1))
    energy.append(300)
    senses.append (random.randint(1, 5))
    age.append (random.randint (0, 30))

for i in range (0, bats):
    species.append ("b")
    batx.append (random.randint(1, (width-1)))
    baty.append (random.randint(1, (height-1)))
    batfoodweight.append (random.uniform(0.5, 1))
    batmateweight.append (random.uniform(0.5, 1))
    batenergy.append (5000)
    batsenses.append (random.randint(2, 6))
    batage.append (random.randint(0, 50))

lastavgage = sum(age) / flies
lastmate = (sum(mateweight) / flies) *100
lastfood = (sum(foodweight) / flies) *100
lastsenses = (sum(senses) / flies) *20

canvas = GraphWin("ecosystem", (width*zoom)+(border*2), (height*zoom)+(border*2), autoflush = False)
canvas.setBackground (color_rgb(255, 255, 255))
graph = GraphWin("data", (800+border), (400+border))
graph.setBackground (color_rgb(0, 0, 0))


while flies > 0:
    timer = timer + 1
    time.sleep(pause)

# KILLS FLIES

    deaths = 0
    for i in range (0, flies):
        if energy[flies-i-1] < 1 or age[flies-i-1] > 100: # if the fly has no energy or is old
            deaths = deaths +1
            rot = rot + energy[flies-i-1]
            energy.pop(flies-i-1)
            x.pop(flies-i-1)
            y.pop(flies-i-1)
            senses.pop(flies-i-1)
            foodweight.pop(flies-i-1)
            mateweight.pop(flies-i-1)
            age.pop(flies-i-1)
    flies = flies - deaths

# GROWS NEW VEG FROM ROT

    for i in range (0, round((rot / 100) + 1)):
        if rot >= 100:
            rot = rot - 100
            vegetables = vegetables + 1
            vegx.append(random.randint(0, (width)))
            vegy.append(random.randint(0, (height)))

# CLEARS DRAWING

    for item in canvas.items[:]:
        item.undraw()

# DRAWS VEG
    
    for i in range (0, vegetables):
        veg = Rectangle(Point ((((vegx[i]-1)*zoom)+border),(((vegy[i]-1)*zoom)+border)), Point(((vegx[i]*zoom)+border),((vegy[i]*zoom)+border)))
        veg.setOutline (color_rgb (0,200,0))
        veg.setWidth (1)
        veg.draw (canvas)

# DRAWS FLIES

    for i in range (0, flies):
        if age[i] > 15:
            fly = Rectangle(Point ((((x[i]-1)*zoom)+border),(((y[i]-1)*zoom)+border)), Point(((x[i]*zoom)+border),((y[i]*zoom)+border)))
        else:
            fly = Rectangle(Point ((((x[i]-1)*zoom)+border+(zoom/12)),(((y[i]-1)*zoom)+border+(zoom / 12))), Point(((x[i]*zoom)+border-(zoom / 8)),((y[i]*zoom)+border-(zoom / 8))))
        fly.setOutline (color_rgb (0,0,0))
        fly.setWidth ((round(energy[i] / (30 * zoom))) + 1)
        fly.draw (canvas)

# DRAWS BATS

    for i in range (0, bats):
        bat = Rectangle (Point ((((batx[i]-2)*zoom)+border),(((baty[i]-2)*zoom)+border)), Point((((batx[i]+1)*zoom)+border),(((baty[i]+1)*zoom)+border)))
        bat.setOutline (color_rgb (120,0,0))
        bat.setWidth ((round(batenergy[i] / (100 * zoom))) + 1)
        bat.draw (canvas)
        
# DRAWS GRAPH

    if timer % 750 == 0:
        timer = 0
        for item in graph.items[:]:
            item.undraw()
        graph.update()
        axis = Line(Point((border),(400)), Point((800),(400)))
        axis.setOutline (color_rgb (255,255,255))
        axis.setWidth (2)
        axis.draw (graph)
        
        axis = Line(Point((border),(border)), Point((border),(400)))
        axis.setOutline (color_rgb (255,255,255))
        axis.setWidth (2)
        axis.draw (graph)

    if showage == True:
        graphage = Line(Point((timer+border-1), (400 - (lastavgage*4)-border)), Point ((timer+border), (400 - (sum(age) / flies*4) -border)))
        graphage.setOutline (color_rgb (160,0,0))
        graphage.setWidth (5)
        graphage.draw (graph)
        lastavgage = (sum(age) / flies)

    if showveg == True:
        graphveg = Line(Point((timer+border-1), (400 - (lastvegetables*2)-border)), Point ((timer+border), (400 - (vegetables*2) -border)))
        graphveg.setOutline (color_rgb (0,160,0))
        graphveg.setWidth (5)
        graphveg.draw (graph)
        lastvegetables = vegetables

    if showflies == True:
        graphflies = Line(Point((timer+border-1), (400 - (lastflies*2)-border)), Point ((timer+border), (400 - (flies*2) -border)))
        graphflies.setOutline (color_rgb (100,100,100))
        graphflies.setWidth (5)
        graphflies.draw (graph)
        lastflies = flies

    if showmate == True:
        graphmate = Line(Point((timer+border-1), (400 - (lastmate)-border)), Point ((timer+border), (400 - ((sum(mateweight) / flies)*100)) -border))
        graphmate.setOutline (color_rgb (160,0,160))
        graphmate.setWidth (5)
        graphmate.draw (graph)
        lastmate = (sum(mateweight) / flies)*100

    if showfood == True:
        graphfood = Line(Point((timer+border-1), (400 - (lastfood)-border)), Point ((timer+border), (400 - ((sum(foodweight) / flies)*100)) -border))
        graphfood.setOutline (color_rgb (160,160,0))
        graphfood.setWidth (5)
        graphfood.draw (graph)
        lastfood = (sum(foodweight) / flies)*100

    if showsenses == True:
        graphsenses = Line(Point((timer+border-1), (400 - (lastsenses)-border)), Point ((timer+border), (400 - ((sum(senses) / flies)*20)) -border))
        graphsenses.setOutline (color_rgb (250,160,0))
        graphsenses.setWidth (5)
        graphsenses.draw (graph)
        lastsenses = (sum(senses) / flies)*20

# GATHERS FLY DATA
    
    for i in range (0, flies):

        # finds nearby veg
        gotox = 0
        gotoy = 0
        vegdis = 9999
        for e in range (0, vegetables):
            vegdisx = (((x[i]-vegx[e])**2)**0.5)
            vegdisy = (((y[i]-vegy[e])**2)**0.5)
            
            if vegdisx >= vegdisy and vegdisx <= vegdis:
                fly_on_food = False
                for o in range (0, flies):
                    if (((x[o]-vegx[e])**2)**0.5) == 0 and (((y[o]-vegy[e])**2)**0.5) == 0 and o != i:
                        fly_on_food = True
                    if fly_on_food == False:
                        vegdis = vegdisx
                        vegno = e
                        
            elif vegdisx <= vegdisy and vegdisy <= vegdis:
                fly_on_food = False
                for o in range (0, flies):
                    if (((x[o]-vegx[e])**2)**0.5) == 0 and (((y[o]-vegy[e])**2)**0.5) == 0 and o != i:
                        fly_on_food = True
                    if fly_on_food == False:
                        vegdis = vegdisy
                        vegno = e


        # finds nearby flies
        adjacent = 0
        flydis = 9999
        seeflyno = []
        for o in range (0, flies):
            if o != i:
                flydisx = (((x[o]-x[i])**2)**0.5)
                flydisy = (((y[o]-y[i])**2)**0.5)
                if flydisx >= flydisy and flydisx <= senses[i]:
                    if flydisx == 1 or flydisy == 1:
                        adjacent = adjacent + 1 
                    seeflyno.append(o)
                    if flydisx <= flydis:
                        flydis = flydisx
                        flyno = o
                elif flydisx <= flydisy and flydisy <= senses[i]:
                    if flydisx == 1 or flydisy == 1:
                        adjacent = adjacent + 1 
                    seeflyno.append(o)
                    if flydisy <= flydis:
                        flydis = flydisy
                        flyno = o


# FLIES CHOOSE THEIR MOOD
                    
        mood = "idle"
        chooseeat = 0
        choosefood = 0
        choosemate = 0
        choosefollow = 0

        # eating
        if vegdis == 0 and energy[i] < (maxenergy + 1):
            chooseeat = (1 / (((((energy[i] / 10) + 1) ** 1.1) / 75) + 1)) * foodweight[i]
            

            
        # search food
        elif vegdis <= senses[i] and energy[i] < (maxenergy + 1): # If they are hungry and near food
            choosefood = (1 / (((( ((vegdis / 5) + 1) * ((energy[i] / 10) + 1)) ** 1.1) / 50) + 1)) * foodweight[i]
            gotox = vegx[vegno]
            gotoy = vegy[vegno]
            newx = x[i]
            newy = y[i]
            if gotox < x[i]:
                newx = x[i] - 1
            elif gotox > x[i]:
                newx = x[i] +1
            if gotoy < y[i]:
                newy = y[i] - 1
            elif gotoy > y[i]:
                newy = y[i] + 1
            for o in range (0, len(seeflyno)): # if they are trying to move where another fly is they stop getting food
                if x[seeflyno[o]] == newx and y[seeflyno[o]] == newy:
                    choosefood = 0
                    newx = x[i]
                    newy = y[i]


        # mating
        if flydis == 0 and energy[i] > 10 and age[i] > 15 and age[flyno] > 15: # if they are on another fly
            choosemate = (1 / (((1 / (energy[i] / 5)) + 1) ** 1.4)) * mateweight[i]
            if choosemate < 0.35 or adjacent > 4:
                choosemate = 0
            
            
        # following
        elif flydis <= senses[i] and age[i] > 15 and age[flyno] > 15 and flydis > 0: # if they are near a fly
            choosefollow = (1 / ((((1 / (energy[i] / 5)) + 1) ** 1.4) * ((flydis / 8) + 1))) * mateweight[i]
            followx = x[flyno]
            followy = y[flyno]
            newx2 = x[i]
            newy2 = y[i]
            if followx < x[i]:
                 newx2 = x[i] - 1
            elif followx > x[i]:
                 newx2 = x[i] +1
            if followy < y[i]:
                 newy2 = y[i] - 1
            elif followy > y[i]:
                 newy2 = y[i] + 1

        # finalises their priorities
        if chooseeat >= choosefood and chooseeat >= choosefollow and chooseeat >= choosemate and chooseeat > 0:
            mood = "eating"
        elif  choosefood >= chooseeat and choosefood >= choosefollow and choosefood >= choosemate and choosefood > 0:
            mood = "search food"
        elif  choosemate >= choosefood and choosemate >= choosefollow and choosemate >= chooseeat and choosemate > 0:
            mood = "mating"
        elif  choosefollow >= choosefood and choosefollow >= chooseeat and choosefollow >= choosemate and choosefollow > 0:
            mood = "follow"
        else:
            mood = "idle"
        #print ("chooseeat", chooseeat)
       # print ("choosefood", choosefood)
        #print ("choosemate", choosemate)
        #print ("choosefollow", choosefollow)
        #print (i, mood)
        #print ()
        #time.sleep(0.3)
            


# THE FLIES ACT

        if mood == "eating": # if they are hungry and on food
            vegx.pop(vegno)
            vegy.pop(vegno)
            newenergy = energy[i] + 100
            energy.pop(i)
            energy.insert(i, newenergy)
            vegetables = vegetables - 1
            newage = age[i] + 1
            age.pop(i)
            age.insert(i, newage)
                    

        if mood == "search food":
            x.pop(i)
            x.insert(i, newx)
            y.pop(i)
            y.insert(i, newy)
            if age[i] > 15:
                newenergy = energy[i] - hungeraffect
                rot = rot + hungeraffect
                energy.pop(i)
                energy.insert(i, newenergy)
            else:
                newenergy = energy[i] - round(hungeraffect / sympathy)
                rot = rot + round(hungeraffect / sympathy)
                energy.pop(i)
                energy.insert(i, newenergy)
            newage = age[i] + 1
            age.pop(i)
            age.insert(i, newage)


        if mood == "mating":
            newenergy = energy[i] - hungeraffect
            rot = rot + hungeraffect
            energy.pop(i)
            energy.insert(i, newenergy)
            newx = x[i] + (random.randint(-1, 1))
            newy = y[i] + (random.randint(-1, 1))
            for o in range (0, len(seeflyno)): # if they are trying to reproduce where another fly is they do not mate
                if x[seeflyno[o]] == newx and y[seeflyno[o]] == newy:
                    choosemate = 0
                    mood = "idle"
            if choosemate > 0:
                newenergy = round((energy[i] + energy[flyno]) / 3)
                rot = rot + ((energy[i] + energy[flyno]) - (newenergy*3))
                energy.pop(i)
                energy.insert(i, newenergy)
                energy.pop(flyno)
                energy.insert(flyno, newenergy)
                newage = age[i] + 1
                age.pop(i)
                age.insert(i, newage)

                flies = flies + 1
                energy.append (newenergy)
                x.append (newx)
                y.append (newy)
                age.append (0)
                parent = random.randint (1, 2) # senses
                if parent == 1:
                    senses.append (senses[i] + random.randint (-1, 1))
                elif parent == 2:
                    senses.append (senses[flyno] + random.randint (-1, 1))
                parent = random.randint (1, 2) # foodweight
                if parent == 1:
                    foodweight.append (foodweight[i] + random.uniform (-1, 1))
                elif parent == 2:
                    foodweight.append (foodweight[flyno] + random.uniform (-1, 1))
                parent = random.randint (1, 2) # mateweight
                if parent == 1:
                    mateweight.append (mateweight[i] + random.uniform (-1, 1))
                elif parent == 2:
                    mateweight.append (mateweight[flyno] + random.uniform (-1, 1))

             

        if mood == "follow": 
            x.pop(i)
            x.insert(i, newx2)
            y.pop(i)
            y.insert(i, newy2)
            if age[i] > 15:
                newenergy = energy[i] - hungeraffect
                rot = rot + hungeraffect
                energy.pop(i)
                energy.insert(i, newenergy)
            else:
                newenergy = energy[i] - round(hungeraffect / sympathy)
                rot = rot + round(hungeraffect / sympathy)
                energy.pop(i)
                energy.insert(i, newenergy)
            newage = age[i] + 1
            age.pop(i)
            age.insert(i, newage)
            
            
        if mood == "idle": # if the fly is idle
            if age[i] > 15:
                newenergy = energy[i] - hungeraffect
                rot = rot + hungeraffect
                energy.pop(i)
                energy.insert(i, newenergy)
            else:
                newenergy = energy[i] - round(hungeraffect / sympathy)
                rot = rot + round(hungeraffect / sympathy)
                energy.pop(i)
                energy.insert(i, newenergy)
            newx = x[i]
            newy = y[i]
            
            if x[i] == width: # Adjusts fly x
                newx = x[i] - (random.randint (0,1))
            elif x[i] == 0:
                newx = x[i] - (random.randint (-1,0))
            else:
                newx = x[i] - (random.randint (-1,1))
            for o in range (0, len(seeflyno)): # if they are trying to move where another fly is they dont move
                if x[seeflyno[o]] == newx:
                    newx = x[i]
            x.pop(i)
            x.insert(i, newx)
            
            if y[i] == height: # Adjusts fly y
                newy = y[i] - (random.randint (0,1))
            elif y[i] == 0:
                newy = y[i] - (random.randint (-1,0))
            else:
                newy = y[i] - (random.randint (-1,1))
            for o in range (0, len(seeflyno)): # if they are trying to move where another fly is they dont move
                if y[seeflyno[o]] == newy:
                    newy = y[i]
            y.pop(i)
            y.insert(i, newy)
            newage = age[i] + 1
            age.pop(i)
            age.insert(i, newage)





        #print (age[i])

