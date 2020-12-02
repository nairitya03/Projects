import pygame
from pygame import display,image
import game_config as gc
from animal import Animal
from time import sleep

pygame.init()

def Find_index(x,y):
    row = y //gc.IMAGE_SIZE
    col = x// gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index
    
display.set_caption('MY Game')
screen = display.set_mode ((512,512))
matched =image.load('assets/matched.png')

running =True
tiles =[Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]

current_images = []
TOTAL_SKIP = 0

while running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            index = Find_index(mouse_x,mouse_y)
            if index not in current_images:
                
                current_images.append(index)
            if len (current_images) > 2:
                current_images = current_images[1:]
            
    screen.fill((255, 255, 255))
        
    for _,tile in enumerate(tiles):
        non_image = tile.image if tile.index in current_images else tile.box
        if not tile.skip:
            screen.blit(non_image,(tile.col * gc.IMAGE_SIZE + gc.MARGIN,
                                tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            TOTAL_SKIP =+1
            
    if len(current_images)==2:
        idx1,idx2 = current_images
        
        if( tiles[idx1].name == tiles[idx2].name ):
            
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            sleep(0.3)
            screen.blit(matched,(0,0))
            display.flip()
            sleep(0.3)
            current_images =[]
    if( TOTAL_SKIP == len (tiles)):
        screen.blit(matched,(0,0))
        display.flip()
        running == False
        
    display.update()

print("GoodBye")