import pygame, sys
import random
import time

class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("images/002-turtle.png")
        self.position = [x,y]
        self.name = ""    
    def avanzar(self):
        self.position[0] += random.randint(1,10)

class Game():
    runners = []
    __startLine = 5
    __finishLine = 620
    #Lista de disfraces
    __customes = ("images/001-fish.png","images/002-turtle.png","images/003-octopus.png","images/004-prawn.png")
    #Lista de nombres
    __nombres = ("Pez", "Tortu", "Pulpo", "Gamba")
    #lista de posiciones iniciales
    __posiciones = ((__startLine, 160),(__startLine, 200),(__startLine, 240),(__startLine, 280))
    
    def posiciones(self):
        return self.__posiciones
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        #En lugar de un color de fondo ponemos una imagen
        #self.__screen.fill((0,255,0))
        self.background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        #Creamos los 4 animales de la carrera
        for i in range(4):
            mirunner = Runner(self.__posiciones[i][0],self.__posiciones[i][1])
            mirunner.custome = pygame.image.load(self.__customes[i])
            mirunner.name = self.__nombres[i]
            self.runners.append(mirunner)
        
    def competir(self):
        x = 0
        gameOver = False
        while not gameOver:
            
            #Comprobacion de Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    pygame.quit()
                    sys.exit()
            for runner in self.runners:
                time.sleep(0.01)
                runner.avanzar()
                if runner.position[0] >= self.__finishLine:
                    print("El ganador es : {}".format(runner.name))
                    gameOver = True            
            
            self.__screen.blit(self.background, (0,0))
            
            for runner in self.runners:                
                self.__screen.blit(runner.custome, (runner.position))                
            
            pygame.display.flip()
        
        #Para que no se cierre nada mas llegar a la meta y se quede esperando a que presione cerrar
        while True:       
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
