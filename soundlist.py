'''
   soundlist.py is part of Escadron-T42.
   Copyright (C) 2012 dabou

   Escadron-T42 is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public
   License along with this program; if not, see <http://www.gnu.org/licenses/> 
   or write to the Free Software Foundation, Inc.,
   51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301 USA.
'''

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
    
