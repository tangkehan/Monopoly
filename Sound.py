#Peiwen: create sounds class and initialize sounds in the class
import pygame

class Sound:
    
    def __init__(self, path):
        self.path = path
        self.name = pygame.mixer.Sound(path)

    def playSound(self):
        self.name.play()


 #load sounds
pygame.mixer.init()
surprise = Sound("sounds/sound_事件.wav")
click = Sound("sounds/sound_按键.wav")
update = Sound("sounds/sound_升级.wav")
fail = Sound("sounds/sound_失败.wav")
sucess = Sound("sounds/sound_胜利.wav")

