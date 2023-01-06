#Snake in PyGame
#Initialization
import pygame
import random
pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake in PyGame")
screenWidth = 800
screenHeight = 600
clock = pygame.time.Clock()

#Colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

#Dimensions
size = 10
x = int(screenWidth/2)
y = int(screenHeight/2)
dx = 0 #Change in dimensions
dy = 0
speed = 10

#The Food
foodx = round(random.randint(0,screenWidth - size)/10)*10 #This is because coordinates are at the top left
foody = round(random.randint(0,screenHeight - size)/10)*10 

#Main Loop
snakelist = [[x,y]]
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False #If quit stop running
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -speed #Keep going in -10 which is the size of snake change in x and do not change in y, therefore you can't move horizontally and veritcally at the same time 
                dy = 0 
            if event.key == pygame.K_RIGHT:
                dx = speed
                dy = 0
            if event.key == pygame.K_UP:
                dy = -speed
                dx = 0
            if event.key == pygame.K_DOWN:
                dy = speed
                dx = 0
    
    #Borders
    if x <= 0 or x >= screenWidth:
        run = False
    elif y <= 0 or y >= screenHeight:
        run = False
    
    #The Coordinate Lists and Extention
    snakelistp = snakelist #To remember past snake
    x += dx
    y += dy
    snakelist.reverse()
    for i in range(len(snakelist) - 2):
        snakelist[i] = snakelist[i+1]
    snakelist[len(snakelist) - 1] = [x,y]
    snakelist.reverse()

    #Food Randomizer and Points
    if foodx == x and foody == y:
        snakelist.append(snakelistp[-1])
        print(snakelist)
        foodx = round(random.randint(0,screenWidth - size)/10)*10
        foody = round(random.randint(0,screenHeight - size)/10)*10

    #Display
    display.fill(black)
    for i in snakelist:
        pygame.draw.rect(display,white,[x,y,size,size])
    pygame.draw.rect(display,red,[foodx,foody,size,size])
    pygame.display.update()
    clock.tick(30) #Note that there are 1000 miliseconds in a second; the clock ticks in miliseconds in the parameter

print("You Lose!")
pygame.quit()
quit()
#Use a list as the snake, try to display this
#Start with a snake of three elements in the list
#Focus on the .tail and the .head
#When you move once, pop the tail
#When you eat food, keep the tail