import pygame, sys
import random
import time

class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("images/002-turtle.png")
        self.position = [x,y]
        self.name = "Tortuga"
    
    def avanzar(self):
        self.position[0] += random.randint(1,6)

class Game():
    runners = []
    __startLine = 5
    __finishLine = 620
    #Lista de disfraces
    customes = ("images/001-fish.png","images/002-turtle.png","images/003-octopus.png","images/004-prawn.png")
    #Lista de nombres
    nombres = ("Pez", "Tortu", "Pulpo", "Gamba")
    #lista de posiciones iniciales
    posiciones = ((__startLine, 160),(__startLine, 200),(__startLine, 240),(__startLine, 280))
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        #En lugar de un color de fondo ponemos una imagen
        #self.__screen.fill((0,255,0))
        self.background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        self.runners.append(Runner(self.__startLine, 240))
        
    def competir(self):
        x = 0
        gameOver = False
        while not gameOver:
            time.sleep(0.1)
            #Comprobacion de Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    pygame.quit()
                    sys.exit()
            
            self.runners[0].avanzar()
            #Ahora el renderizado (refresco de pantalla)
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runners[0].custome, (self.runners[0].position))
            #self.__screen.blit(self.runner, (x,240))
            pygame.display.flip()
            
            if self.runners[0].position[0] >= self.__finishLine:
                gameOver = True
                
        pygame.quit()
        sys.exit()
        
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()