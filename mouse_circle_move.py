import pygame
import sys
import random
import time
pygame.init()
screen_size=(400,400)
screen=pygame.display.set_mode(screen_size)
pygame.display.set_caption("Mouse Circle")
color=(255,0,0)

radius=25
width_cir=2
plus_size=10
color_line=(0,0,0)

color_rec=(0,255,0)
rect_color_collide = (255,0, 0) 
height=25
width=25


def starting_timer(seconds):
    while seconds >=0:
        print(f"Game starts in: {seconds} seconds",end='\r')
        time.sleep(1)
        seconds -= 1
    print()
    print("START!")
starting_timer(10)  

def dis_rand_rect():
    rec_x=random.randint(0,screen_size[0]-width)
    rec_y=random.randint(0,screen_size[1]-height)
    return pygame.Rect(rec_x,rec_y,width,height)
rect=dis_rand_rect()
font=pygame.font.SysFont(None,25)
score=0

timer_seconds = 30  # Set the timer duration here
start_ticks = pygame.time.get_ticks()

running=True
while running:
    screen.fill((200,255,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elapsed_ticks = pygame.time.get_ticks() - start_ticks
        remaining_time = max(0, timer_seconds - elapsed_ticks // 1000)
        position_x,position_y=pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if rect.collidepoint(position_x,position_y):
                score+=1
                rect=dis_rand_rect()
        if rect.collidepoint(position_x,position_y):
            current_rect_color = rect_color_collide  # Change color if collision
        else:
            current_rect_color = color_rec
 
        screen_txt1=font.render(f"Score - {score}",True,(0,0,0))
        screen_txt2=font.render("by Madhesh",True,(0,0,0))
        screen_txt3 = font.render(f"Time Left: {remaining_time}", True, (0, 0, 0))
        screen.blit(screen_txt1,(10,10))
        screen.blit(screen_txt2,(300,10))
        screen.blit(screen_txt3, (150, 10))
        pygame.draw.rect(screen,current_rect_color,rect)
        pygame.draw.circle(screen,color,(position_x,position_y),radius,width_cir)
        pygame.draw.line(screen,color_line,(position_x-plus_size,position_y),(position_x+plus_size,position_y))
        pygame.draw.line(screen,color_line,(position_x,position_y-plus_size),(position_x,position_y+plus_size))    
        
 
        pygame.display.update()
        if remaining_time == 0:
            print("Time's up!")
            running = False
            def ending_timer(seconds):
                while seconds >= 0:
                    print(f" fetching result in: {seconds} seconds",end='\r')
                    time.sleep(1)
                    seconds -= 1
            ending_timer(5)
print()           
print("CONGRATS,YOU HAVE SCORED: ",score)       

pygame.quit()
sys.exit()