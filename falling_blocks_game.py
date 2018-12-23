import pygame
import sys
import random
import math
import time

pygame.init()
#create screen
width = 800
hieght = 600
screen = pygame.display.set_mode((width, hieght))

gameOver=False

RED = (255,0,0)
BLUE = (0,0,225)
Background_color = (0,0,0)

player_size = 40
player_speed = 50

enemy_size = 50
enemy_speed = .5

random_Xcor = random.randint(0,width-enemy_size)
enemy_position = [random_Xcor,0]
enemy_list = [enemy_position]
playerPosition = [width/2, hieght-2*player_size]

score = 0
myFont = pygame.font.SysFont("monospace", 35)

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list)<13 and delay <0.01:
        x_pos  = random.randint(0, width - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemy(enemy_list):
    for enemy_position in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_position[0], enemy_position[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
    for indx, enemy_position in enumerate(enemy_list):
        if enemy_position[1]<hieght and enemy_position[1] >=0:
            enemy_position[1] +=enemy_speed 
        else:
            enemy_list.pop(indx)
            score += 1            
    return score

def pre_check_collision(enemy_list, player_size):
    for enemy_position in enemy_list:
        if check_colition(enemy_position, playerPosition):
            return True
    return False


#checks for colitoin, could shorted variable names
def check_colition(enemy_position, playerPosition):
    p_x = playerPosition[0]
    p_y = playerPosition[1]
    e_x = enemy_position[0]
    e_y = enemy_position[1]

    if (e_x >= p_x and e_x <(p_x+player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):            
            draw_enemy(enemy_list)
            pygame.draw.rect(screen, RED, (playerPosition[0],playerPosition[1],player_size,player_size)) #Xcor, Ycor, hieght, width            
            pygame.display.update()            
            return True
        return False    

while not gameOver:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        #listen for events n
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerPosition[0] -= player_speed
            elif event.key == pygame.K_RIGHT:
                playerPosition[0] += player_speed
    screen.fill(Background_color)    

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)   
    
    if pre_check_collision(enemy_list, playerPosition):
        gameOver = True        
        draw_enemy(enemy_list)
        pygame.draw.rect(screen, RED, (playerPosition[0],playerPosition[1],player_size,player_size)) #Xcor, Ycor, hieght, width
        text = "Game Over" 
        label = myFont.render(text, 1, (255,255,255))
        screen.blit(label, ((width/2)-100, hieght/2))
        text = "Score:" + str(score)
        label = myFont.render(text, 1, (255,255,255))
        screen.blit(label, (width-200, hieght-40))
        pygame.display.update()
        time.sleep(2)        
        break
    draw_enemy(enemy_list)    
        
    pygame.draw.rect(screen, RED, (playerPosition[0],playerPosition[1],player_size,player_size)) #Xcor, Ycor, hieght, width
     #display score
    text = "Score:" + str(score)
    label = myFont.render(text, 1, (255,255,255))
    screen.blit(label, (width-200, hieght-40))
    #update screen    
    pygame.display.update()




