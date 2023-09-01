import pygame
from network import Network
from player import Player

width = 500
height =500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Client")
adsf
"""clientNumber = 0


def read_pos(str):#want a (45,423)
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])
"""

def redrawWindow(win,player, player2):
    
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    #connecting to the server
    n = Network()
    """startPos = n.getPos()# arguments comes in as a tuple
    p = Player(startPos[0],startPos[1],100,100,(0,255,0))
    p2 = Player(0,0,100,100,(255,255,0))"""
    p = n.getP()
    
    clock = pygame.time.Clock()
    
    while run:
        clock.tick(60)
        
        p2 = n.send(p)#constantly be looking for where player 2 is
        """p2Pos =n.send((p.x,p.y))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()"""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win,p,p2)

main()