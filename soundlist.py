import os
from os import chdir

from kivy.core.audio import SoundLoader

class GestionSon:
    def __init__(self):
        self.m_oSpaceSoundList = {}
        self.m_oMusic = None
    
    def loadMusic(self, music):
        
        if self.m_oMusic:
            self.m_oMusic.stop()
    
        currentPathTmp = os.getcwd()
        chdir(os.path.dirname( __file__))
        
        sound = SoundLoader.load(filename='sons/musiques/' + music)
        if sound:
            self.m_oMusic = sound
            
        chdir(currentPathTmp)
            
    def playMusic(self):
        if self.m_oMusic:
            self.m_oMusic.play()   
            
    def stopMusic(self):
        if self.m_oMusic:
            self.m_oMusic.stop() 
            
    def musicIsStop(self):
        if not self.m_oMusic or self.m_oMusic.status == 'stop':
            return True
        else:
            return False

    def loopMusic(self):
        if self.m_oMusic:
            if self.m_oMusic.status == 'stop':
               #print 'loop playMusic'
               self.playMusic()
            
        
    
    def loadAllSound(self):
        currentPathTmp = os.getcwd()
        chdir(os.path.dirname( __file__))
        
        soundlaser = SoundLoader.load(filename='sons/aust-paul__possiblelazer.wav')
        if soundlaser:
            self.m_oSpaceSoundList['laser'] = soundlaser
            
        soundlaser2 = SoundLoader.load(filename='sons/49695__ejfortin__energy-whip-2.wav')
        if soundlaser2:
            self.m_oSpaceSoundList['laser2'] = soundlaser2
            
        soundlaser3 = SoundLoader.load(filename='sons/49695__ejfortin__energy-whip-2.wav')
        if soundlaser3:
            self.m_oSpaceSoundList['laser3'] = soundlaser3
            
        
        soundastero_explosion = SoundLoader.load(filename='sons/boom4-2.wav')
        if soundastero_explosion:
            self.m_oSpaceSoundList['astero_explosion'] = soundastero_explosion
            
        
        soundlaser_explosion = SoundLoader.load(filename='sons/28917__junggle__btn107.wav')
        if soundlaser_explosion:
            self.m_oSpaceSoundList['laser_explosion'] = soundlaser_explosion
            
            
        
        soundspaceship_explosion = SoundLoader.load(filename='sons/boom1.wav')
        if soundspaceship_explosion:
            self.m_oSpaceSoundList['spaceship_explosion'] = soundspaceship_explosion
            
            
        
        sounddrone_explosion = SoundLoader.load(filename='sons/boom1.wav')
        if sounddrone_explosion:
            self.m_oSpaceSoundList['drone_explosion'] = sounddrone_explosion
            
            
        
        soundgetitem = SoundLoader.load(filename='sons/34232__hardpcm__chip116.wav')
        if soundgetitem:
            soundgetitem.volume = 0.2
            self.m_oSpaceSoundList['getitem'] = soundgetitem
            
            
    
        chdir(currentPathTmp)
        
    def playLaser(self):
        if 'laser' in self.m_oSpaceSoundList:
            #print 'playLaser'
            self.m_oSpaceSoundList['laser'].play()    
            
    def playLaser2(self):
        if 'laser2' in self.m_oSpaceSoundList:
            #print 'playLaser2'
            self.m_oSpaceSoundList['laser2'].play()    
            
    def playLaser3(self):
        if 'laser3' in self.m_oSpaceSoundList:
            #print 'playLaser3'
            self.m_oSpaceSoundList['laser3'].play()    
        
    def playLaserExplosion(self):
        if 'laser_explosion' in self.m_oSpaceSoundList:
            #print 'playLaserExplosion'
            self.m_oSpaceSoundList['laser_explosion'].play()  
        
    def playAsteroidExplosion(self):
        if 'astero_explosion' in self.m_oSpaceSoundList:
            #print 'playAsteroidExplosion'
            self.m_oSpaceSoundList['astero_explosion'].play()  
        
    def playSpaceShipExplosion(self):
        if 'spaceship_explosion' in self.m_oSpaceSoundList:
            #print 'playSpaceShipExplosion'
            self.m_oSpaceSoundList['spaceship_explosion'].play()  
        
    def playDroneExplosion(self):
        if 'drone_explosion' in self.m_oSpaceSoundList:
            #print 'playDroneExplosion'
            self.m_oSpaceSoundList['drone_explosion'].play()  
        
    def playGetItem(self):
        if 'getitem' in self.m_oSpaceSoundList:
            #print 'playGetItem'
            self.m_oSpaceSoundList['getitem'].play() 
        
        
    
    

class SoundList:
    pass
    
