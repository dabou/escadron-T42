'''
   main.py is part of Escadron-T42.
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

import kivy
kivy.require('1.0.9')

from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty, ReferenceListProperty
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from random import random
from kivy.clock import Clock 
from functools import partial
from kivy.utils import *
from kivy.graphics import *
from kivy.vector import Vector

from kivy.config import Config
        
from kivy.factory import Factory
import math
from math import sqrt
import pickle 
import os
from os import chdir
from kivy.gesture import Gesture, GestureDatabase
from my_gestures import vertical, ligne, lance
from niveau import Niveau, NiveauAction, NiveauGenerated
from textureanime import TextureAnime
from soundlist import GestionSon

import time




class Game(Widget):

    space = ObjectProperty(None)
    tableau = ObjectProperty(None)
    
    def __init__(self):
        Widget.__init__(self)
        
        self.heart = 3
        self.star = 0
        self.tux = 0
        self.laserType = 1
        self.niveauNbr = 0
    
    def quitGame(self):
        self.oEscadronT42.quitGame()
        
    def isGameOver(self):
        self.showEcranGameOver()
        
    def init(self):
        self.heart = 3
        self.tableau.heartLbl.text = str(self.heart)
        self.star = 0
        self.tableau.starLbl.text = str(self.star)
        self.tux = 0
        self.laserType = 1
        self.niveauNbr = 0
        self.addDrone()
        self.addDrone()
        self.addDrone()
        self.addDrone()
    
    def build(self, p_oEscadronT42):
    
        self.oEscadronT42 = p_oEscadronT42
        self.gestionSon = GestionSon()
        self.gestionSon.loadAllSound()
        
        self.isOnPause = True
        
        self.m_oSpaceObjectList = []
        self.m_oSpaceDecorationObjectList = []
        
                
        self.m_oRegion1_1ObjectList = []
        self.m_oRegion1_2ObjectList = []
        self.m_oRegion1_3ObjectList = []
        self.m_oRegion1_4ObjectList = []
        self.m_oRegion2_1ObjectList = []
        self.m_oRegion2_2ObjectList = []
        self.m_oRegion2_3ObjectList = []
        self.m_oRegion2_4ObjectList = []
        self.m_oRegion3_1ObjectList = []
        self.m_oRegion3_2ObjectList = []
        self.m_oRegion3_3ObjectList = []
        self.m_oRegion3_4ObjectList = []
                      
        self.space.build(self)
        
        self.tableau.build(self)
        self.ecranFormation = None
        self.ecranAccueil = None
        self.ecranNiveaux = None
        self.ecranPause = None
        self.ecranStat = None
        self.ecranGameOver = None
        self.ecranCredit = None
        self.ecranNiveauName = None
                
        self.m_oNiveau = GestionNiveau(self)
        
        self.m_oSpaceShip = SpaceShip(50,350)
        self.m_oSpaceShip.setGame(self)
        self.m_oDrone1 = Drone(1, self.m_oSpaceShip)
        self.m_oDrone1.setGame(self)
        self.m_oDrone2 = Drone(2, self.m_oSpaceShip)
        self.m_oDrone2.setGame(self)
        self.m_oDrone3 = Drone(3, self.m_oSpaceShip)
        self.m_oDrone3.setGame(self)
        self.m_oDrone4 = Drone(4, self.m_oSpaceShip)
        self.m_oDrone4.setGame(self)
                        
    def nextNiveaux(self):
        self.pause()
        #self.loadNiveaux()
        self.showEcranStat()       
   
     
    def loadNiveaux(self):
        
        canAddDrone1 = False
        canAddDrone2 = False
        canAddDrone3 = False
        canAddDrone4 = False
    
        if self.m_oDrone1 in self.m_oSpaceObjectList or self.niveauNbr == 1:
            canAddDrone1 = True
         
        if self.m_oDrone2 in self.m_oSpaceObjectList or self.niveauNbr == 1:
            canAddDrone2 = True
         
        if self.m_oDrone3 in self.m_oSpaceObjectList or self.niveauNbr == 1:
            canAddDrone3 = True
         
        if self.m_oDrone4 in self.m_oSpaceObjectList or self.niveauNbr == 1:
            canAddDrone4 = True
            
           
        self.space.background.clear_widgets()    
        self.space.foreground.clear_widgets()    
        self.space.spacegame.clear_widgets()   
        self.tableau.scanview.clear_widgets()   
        
        del(self.m_oSpaceObjectList[:])
        del(self.m_oSpaceDecorationObjectList[:])
                 
        
        #self.m_oNiveau.loadNiveau(p_sNivId)
        #self.m_oNiveau.loadFromFile('1-x33b')
        #self.m_oNiveau.loadFromFile('2-zooz')
        
        self.niveauNbr += 1
        
        self.m_oNiveau.setNiveau(NiveauGenerated(self.niveauNbr))
        #self.m_oNiveau.saveToFile()
        
        self.m_oSpaceShip.pos = 50,350     
        self.m_oSpaceShip.moveTo(50, 350)
        
        self.addSpaceObject(self.m_oSpaceShip)
        if canAddDrone1:
            self.m_oDrone1.pos = 50,350
            self.addSpaceObject(self.m_oDrone1)
        if canAddDrone2:
            self.m_oDrone2.pos = 50,350
            self.addSpaceObject(self.m_oDrone2)
        if canAddDrone3:
            self.m_oDrone3.pos = 50,350
            self.addSpaceObject(self.m_oDrone3)
        if canAddDrone4:
            self.m_oDrone4.pos = 50,350
            self.addSpaceObject(self.m_oDrone4)
        
        
        self.showEcranNiveauName()
        
        Clock.schedule_once(self.runOnce, 1)
        
        
    def runOnce(self,dt):    
        self.run()
                
      
    def run(self):
        self.isOnPause = False
        self.gestionSon.playMusic()
        self.spaceDecorationObjectListIndex = 0
        #self.spaceObjectListIndex = 0
        Clock.schedule_interval(self.loop, 0.02)
        
       
        
    def addSpaceObject(self, p_oSpaceObject):
        self.m_oSpaceObjectList.append(p_oSpaceObject)
        self.space.spacegame.add_widget(p_oSpaceObject)
            
        if p_oSpaceObject.canScanIt:
            self.tableau.scanview.add_widget(ScanObject(p_oSpaceObject, self))
        
        
    def removeSpaceObject(self, p_oSpaceObject):
        self.m_oSpaceObjectList.remove(p_oSpaceObject)
        self.space.spacegame.remove_widget(p_oSpaceObject)
        if p_oSpaceObject.canScanIt:        
            self.tableau.scanview.remove_widget(p_oSpaceObject.scanObject)
        
        
    def addSpaceDecorationObject(self, p_oSpaceDecoObject):
        self.m_oSpaceDecorationObjectList.append(p_oSpaceDecoObject)
        if p_oSpaceDecoObject.isBack:
            self.space.background.add_widget(p_oSpaceDecoObject)
        else:
            self.space.foreground.add_widget(p_oSpaceDecoObject)
    
    def removeSpaceDecorationObject(self, p_oSpaceDecoObject):
        self.m_oSpaceDecorationObjectList.remove(p_oSpaceDecoObject)
        if p_oSpaceDecoObject.isBack:
            self.space.background.remove_widget(p_oSpaceDecoObject)
        else:
            self.space.foreground.remove_widget(p_oSpaceDecoObject)
        
    def shoot(self):
        
        if self.laserType == 1:
            unLaser = Laser()
            unLaser.build(self.m_oSpaceShip, game=self)
            self.addSpaceObject(unLaser)
            
            if self.m_oDrone1 in self.m_oSpaceObjectList:
                laserDrone1 = Laser()
                laserDrone1.build(self.m_oDrone1, game=self)
                self.addSpaceObject(laserDrone1)
            
            if self.m_oDrone2 in self.m_oSpaceObjectList:
                laserDrone2 = Laser()
                laserDrone2.build(self.m_oDrone2, game=self)
                self.addSpaceObject(laserDrone2)
            
            if self.m_oDrone3 in self.m_oSpaceObjectList:
                laserDrone3 = Laser()
                laserDrone3.build(self.m_oDrone3, game=self)
                self.addSpaceObject(laserDrone3)
            
            if self.m_oDrone4 in self.m_oSpaceObjectList:
                laserDrone4 = Laser()
                laserDrone4.build(self.m_oDrone4, game=self)
                self.addSpaceObject(laserDrone4)
                
        elif self.laserType == 2:
            laser1 = Laser()
            laser1.build(self.m_oSpaceShip, game=self)
            laser1.initPos(self.m_oSpaceShip.x + (self.m_oSpaceShip.width / 1.3), self.m_oSpaceShip.y + (self.m_oSpaceShip.height/2) + 10)
            self.addSpaceObject(laser1)
            
            laser2 = Laser()
            laser2.build(self.m_oSpaceShip, game=self)
            laser2.initPos(self.m_oSpaceShip.x + (self.m_oSpaceShip.width / 1.3), self.m_oSpaceShip.y + (self.m_oSpaceShip.height/2) - 10)
            self.addSpaceObject(laser2)
            
            if self.m_oDrone1 in self.m_oSpaceObjectList:
                laser1 = Laser()
                laser1.build(self.m_oDrone1, game=self)
                laser1.initPos(self.m_oDrone1.x + (self.m_oDrone1.width / 1.3), self.m_oDrone1.y + (self.m_oDrone1.height/2) + 10)
                self.addSpaceObject(laser1)
                
                laser2 = Laser()
                laser2.build(self.m_oDrone1, game=self)
                laser2.initPos(self.m_oDrone1.x + (self.m_oDrone1.width / 1.3), self.m_oDrone1.y + (self.m_oDrone1.height/2) - 10)
                self.addSpaceObject(laser2)
            
            if self.m_oDrone2 in self.m_oSpaceObjectList:
                laser1 = Laser()
                laser1.build(self.m_oDrone2, game=self)
                laser1.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2) + 10)
                self.addSpaceObject(laser1)
                
                laser2 = Laser()
                laser2.build(self.m_oDrone2, game=self)
                laser2.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2) - 10)
                self.addSpaceObject(laser2)
            
            if self.m_oDrone3 in self.m_oSpaceObjectList:
                laser1 = Laser()
                laser1.build(self.m_oDrone3, game=self)
                laser1.initPos(self.m_oDrone3.x + (self.m_oDrone3.width / 1.3), self.m_oDrone3.y + (self.m_oDrone3.height/2) + 10)
                self.addSpaceObject(laser1)
                
                laser2 = Laser()
                laser2.build(self.m_oDrone3, game=self)
                laser2.initPos(self.m_oDrone3.x + (self.m_oDrone3.width / 1.3), self.m_oDrone3.y + (self.m_oDrone3.height/2) - 10)
                self.addSpaceObject(laser2)
            
            if self.m_oDrone4 in self.m_oSpaceObjectList:
                laser2 = Laser()
                laser2.build(self.m_oDrone4, game=self)
                laser2.initPos(self.m_oDrone4.x + (self.m_oDrone4.width / 1.3), self.m_oDrone4.y + (self.m_oDrone4.height/2) - 10)
                self.addSpaceObject(laser2)
            
            
        elif self.laserType == 3:
            laser1 = Laser()
            laser1.build(self.m_oSpaceShip, game=self)
            laser1.initPos(self.m_oSpaceShip.x + (self.m_oSpaceShip.width / 1.3), self.m_oSpaceShip.y + (self.m_oSpaceShip.height/2) + 20)
            self.addSpaceObject(laser1)
            
            laser2 = Laser()
            laser2.build(self.m_oSpaceShip, game=self)
            laser2.initPos(self.m_oSpaceShip.x + (self.m_oSpaceShip.width / 1.3), self.m_oSpaceShip.y + (self.m_oSpaceShip.height/2) - 20)
            self.addSpaceObject(laser2)
            
            laser3 = Laser()
            laser3.build(self.m_oSpaceShip, game=self)
            laser3.initPos(self.m_oSpaceShip.x + (self.m_oSpaceShip.width / 1.3), self.m_oSpaceShip.y + (self.m_oSpaceShip.height/2))
            self.addSpaceObject(laser3)
            
            if self.m_oDrone1 in self.m_oSpaceObjectList:
                laser1 = Laser()
                laser1.build(self.m_oDrone1, game=self)
                laser1.initPos(self.m_oDrone1.x + (self.m_oDrone1.width / 1.3), self.m_oDrone1.y + (self.m_oDrone1.height/2) + 20)
                self.addSpaceObject(laser1)
                
                laser2 = Laser()
                laser2.build(self.m_oDrone1, game=self)
                laser2.initPos(self.m_oDrone1.x + (self.m_oDrone1.width / 1.3), self.m_oDrone1.y + (self.m_oDrone1.height/2) - 20)
                self.addSpaceObject(laser2)
                
                laser3 = Laser()
                laser3.build(self.m_oDrone1, game=self)
                laser3.initPos(self.m_oDrone1.x + (self.m_oDrone1.width / 1.3), self.m_oDrone1.y + (self.m_oDrone1.height/2))
                self.addSpaceObject(laser3)
            
            if self.m_oDrone2 in self.m_oSpaceObjectList:
                laser1 = Laser()
                laser1.build(self.m_oDrone2, game=self)
                laser1.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2) + 20)
                self.addSpaceObject(laser1)
                
                laser2 = Laser()
                laser2.build(self.m_oDrone2, game=self)
                laser2.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2) - 20)
                self.addSpaceObject(laser2)
                
                laser3 = Laser()
                laser3.build(self.m_oDrone2, game=self)
                laser3.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2))
                self.addSpaceObject(laser3)
            
            if self.m_oDrone3 in self.m_oSpaceObjectList:
                laser1 = Laser()
                laser1.build(self.m_oDrone2, game=self)
                laser1.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2) + 20)
                self.addSpaceObject(laser1)
                
                laser2 = Laser()
                laser2.build(self.m_oDrone2, game=self)
                laser2.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2) - 20)
                self.addSpaceObject(laser2)
                
                laser3 = Laser()
                laser3.build(self.m_oDrone2, game=self)
                laser3.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2))
                self.addSpaceObject(laser3)
            
            if self.m_oDrone4 in self.m_oSpaceObjectList:
                laser1 = Laser()
                laser1.build(self.m_oDrone4, game=self)
                laser1.initPos(self.m_oDrone4.x + (self.m_oDrone4.width / 1.3), self.m_oDrone4.y + (self.m_oDrone4.height/2) + 20)
                self.addSpaceObject(laser1)
                
                laser2 = Laser()
                laser2.build(self.m_oDrone4, game=self)
                laser2.initPos(self.m_oDrone4.x + (self.m_oDrone4.width / 1.3), self.m_oDrone4.y + (self.m_oDrone4.height/2) - 20)
                self.addSpaceObject(laser2)
                
                laser3 = Laser()
                laser3.build(self.m_oDrone4, game=self)
                laser3.initPos(self.m_oDrone4.x + (self.m_oDrone4.width / 1.3), self.m_oDrone4.y + (self.m_oDrone4.height/2))
                self.addSpaceObject(laser3)
            
        elif self.laserType == 4:
            unLaser = Laser2()
            unLaser.build(self.m_oSpaceShip, game=self)
            self.addSpaceObject(unLaser)
            
            if self.m_oDrone1 in self.m_oSpaceObjectList:
                laserDrone1 = Laser2()
                laserDrone1.build(self.m_oDrone1, game=self)
                self.addSpaceObject(laserDrone1)
            
            if self.m_oDrone2 in self.m_oSpaceObjectList:
                laserDrone2 = Laser2()
                laserDrone2.build(self.m_oDrone2, game=self)
                self.addSpaceObject(laserDrone2)
            
            if self.m_oDrone3 in self.m_oSpaceObjectList:
                laserDrone3 = Laser2()
                laserDrone3.build(self.m_oDrone3, game=self)
                self.addSpaceObject(laserDrone3)
            
            if self.m_oDrone4 in self.m_oSpaceObjectList:
                laserDrone4 = Laser2()
                laserDrone4.build(self.m_oDrone4, game=self)
                self.addSpaceObject(laserDrone4)
        
        elif self.laserType == 5:
            laser1 = Laser2()
            laser1.build(self.m_oSpaceShip, game=self)
            laser1.initPos(self.m_oSpaceShip.x + (self.m_oSpaceShip.width / 1.3), self.m_oSpaceShip.y + (self.m_oSpaceShip.height/2) + 10)
            self.addSpaceObject(laser1)
            
            laser2 = Laser2()
            laser2.build(self.m_oSpaceShip, game=self)
            laser2.initPos(self.m_oSpaceShip.x + (self.m_oSpaceShip.width / 1.3), self.m_oSpaceShip.y + (self.m_oSpaceShip.height/2) - 10)
            self.addSpaceObject(laser2)
            
            if self.m_oDrone1 in self.m_oSpaceObjectList:
                laser1 = Laser2()
                laser1.build(self.m_oDrone1, game=self)
                laser1.initPos(self.m_oDrone1.x + (self.m_oDrone1.width / 1.3), self.m_oDrone1.y + (self.m_oDrone1.height/2) + 10)
                self.addSpaceObject(laser1)
                
                laser2 = Laser2()
                laser2.build(self.m_oDrone1, game=self)
                laser2.initPos(self.m_oDrone1.x + (self.m_oDrone1.width / 1.3), self.m_oDrone1.y + (self.m_oDrone1.height/2) - 10)
                self.addSpaceObject(laser2)
            
            if self.m_oDrone2 in self.m_oSpaceObjectList:
                laser1 = Laser2()
                laser1.build(self.m_oDrone2, game=self)
                laser1.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2) + 10)
                self.addSpaceObject(laser1)
                
                laser2 = Laser2()
                laser2.build(self.m_oDrone2, game=self)
                laser2.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2) - 10)
                self.addSpaceObject(laser2)
            
            if self.m_oDrone3 in self.m_oSpaceObjectList:
                laser1 = Laser2()
                laser1.build(self.m_oDrone3, game=self)
                laser1.initPos(self.m_oDrone3.x + (self.m_oDrone3.width / 1.3), self.m_oDrone3.y + (self.m_oDrone3.height/2) + 10)
                self.addSpaceObject(laser1)
                
                laser2 = Laser2()
                laser2.build(self.m_oDrone3, game=self)
                laser2.initPos(self.m_oDrone3.x + (self.m_oDrone3.width / 1.3), self.m_oDrone3.y + (self.m_oDrone3.height/2) - 10)
                self.addSpaceObject(laser2)
            
            if self.m_oDrone4 in self.m_oSpaceObjectList:
                laser2 = Laser2()
                laser2.build(self.m_oDrone4, game=self)
                laser2.initPos(self.m_oDrone4.x + (self.m_oDrone4.width / 1.3), self.m_oDrone4.y + (self.m_oDrone4.height/2) - 10)
                self.addSpaceObject(laser2)
                
        elif self.laserType == 6:
            unLaser = Laser3()
            unLaser.build(self.m_oSpaceShip, game=self)
            self.addSpaceObject(unLaser)
            
            if self.m_oDrone1 in self.m_oSpaceObjectList:
                laserDrone1 = Laser3()
                laserDrone1.build(self.m_oDrone1, game=self)
                self.addSpaceObject(laserDrone1)
            
            if self.m_oDrone2 in self.m_oSpaceObjectList:
                laserDrone2 = Laser3()
                laserDrone2.build(self.m_oDrone2, game=self)
                self.addSpaceObject(laserDrone2)
            
            if self.m_oDrone3 in self.m_oSpaceObjectList:
                laserDrone3 = Laser3()
                laserDrone3.build(self.m_oDrone3, game=self)
                self.addSpaceObject(laserDrone3)
            
            if self.m_oDrone4 in self.m_oSpaceObjectList:
                laserDrone4 = Laser3()
                laserDrone4.build(self.m_oDrone4, game=self)
                self.addSpaceObject(laserDrone4)
        
        elif self.laserType >= 7:
            laser1 = Laser3()
            laser1.build(self.m_oSpaceShip, game=self)
            laser1.initPos(self.m_oSpaceShip.x + (self.m_oSpaceShip.width / 1.3), self.m_oSpaceShip.y + (self.m_oSpaceShip.height/2) + 10)
            self.addSpaceObject(laser1)
            
            laser2 = Laser3()
            laser2.build(self.m_oSpaceShip, game=self)
            laser2.initPos(self.m_oSpaceShip.x + (self.m_oSpaceShip.width / 1.3), self.m_oSpaceShip.y + (self.m_oSpaceShip.height/2) - 10)
            self.addSpaceObject(laser2)
            
            if self.m_oDrone1 in self.m_oSpaceObjectList:
                laser1 = Laser3()
                laser1.build(self.m_oDrone1, game=self)
                laser1.initPos(self.m_oDrone1.x + (self.m_oDrone1.width / 1.3), self.m_oDrone1.y + (self.m_oDrone1.height/2) + 10)
                self.addSpaceObject(laser1)
                
                laser2 = Laser3()
                laser2.build(self.m_oDrone1, game=self)
                laser2.initPos(self.m_oDrone1.x + (self.m_oDrone1.width / 1.3), self.m_oDrone1.y + (self.m_oDrone1.height/2) - 10)
                self.addSpaceObject(laser2)
            
            if self.m_oDrone2 in self.m_oSpaceObjectList:
                laser1 = Laser3()
                laser1.build(self.m_oDrone2, game=self)
                laser1.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2) + 10)
                self.addSpaceObject(laser1)
                
                laser2 = Laser3()
                laser2.build(self.m_oDrone2, game=self)
                laser2.initPos(self.m_oDrone2.x + (self.m_oDrone2.width / 1.3), self.m_oDrone2.y + (self.m_oDrone2.height/2) - 10)
                self.addSpaceObject(laser2)
            
            if self.m_oDrone3 in self.m_oSpaceObjectList:
                laser1 = Laser3()
                laser1.build(self.m_oDrone3, game=self)
                laser1.initPos(self.m_oDrone3.x + (self.m_oDrone3.width / 1.3), self.m_oDrone3.y + (self.m_oDrone3.height/2) + 10)
                self.addSpaceObject(laser1)
                
                laser2 = Laser3()
                laser2.build(self.m_oDrone3, game=self)
                laser2.initPos(self.m_oDrone3.x + (self.m_oDrone3.width / 1.3), self.m_oDrone3.y + (self.m_oDrone3.height/2) - 10)
                self.addSpaceObject(laser2)
            
            if self.m_oDrone4 in self.m_oSpaceObjectList:
                laser2 = Laser3()
                laser2.build(self.m_oDrone4, game=self)
                laser2.initPos(self.m_oDrone4.x + (self.m_oDrone4.width / 1.3), self.m_oDrone4.y + (self.m_oDrone4.height/2) - 10)
                self.addSpaceObject(laser2)
    
    def addDrone(self): 
        if self.m_oDrone1 not in self.m_oSpaceObjectList:
            self.m_oDrone1.m_deleteMe = False
            self.m_oDrone1.isTouched = False
            self.m_oDrone1.pos = 0, self.m_oSpaceShip.y
            self.addSpaceObject(self.m_oDrone1)
        elif self.m_oDrone2 not in self.m_oSpaceObjectList:
            self.m_oDrone2.m_deleteMe = False
            self.m_oDrone2.isTouched = False
            self.m_oDrone2.pos = 0, self.m_oSpaceShip.y
            self.addSpaceObject(self.m_oDrone2)
        elif self.m_oDrone3 not in self.m_oSpaceObjectList:
            self.m_oDrone3.m_deleteMe = False
            self.m_oDrone3.isTouched = False
            self.m_oDrone3.pos = 0, self.m_oSpaceShip.y
            self.addSpaceObject(self.m_oDrone3)
        elif self.m_oDrone4 not in self.m_oSpaceObjectList:
            self.m_oDrone4.m_deleteMe = False
            self.m_oDrone4.isTouched = False
            self.m_oDrone4.pos = 0, self.m_oSpaceShip.y
            self.addSpaceObject(self.m_oDrone4)
    
    
    def addHeart(self):    
        self.heart += 1
        self.tableau.heartLbl.text = str(self.heart)
        
    def deleteHeart(self):    
        self.heart -= 1
        self.tableau.heartLbl.text = str(self.heart)
        
        if self.heart == 0:
            self.isGameOver()   
    
    def addStar(self, add = 1):    
        self.star += add
        self.tableau.starLbl.text = str(self.star)
    
    def touchItemTux(self):    
        self.nextNiveaux()
          
        
    def addExplosion(self, x, y):
        explosion = Explose()
        explosion.setPosition(x, y)
        self.addSpaceDecorationObject(explosion)
        
    def addLaserExplosion(self, x, y):
        explosion = LaserExplose()
        explosion.setPosition(x, y)
        self.addSpaceDecorationObject(explosion)
        
    def addItem(self, x, y):
        item = None
        i = randint(0, 100)
        if i <= 5 :
            item = ItemLaserUp()
        elif i > 5 and i <= 10:
            item = ItemHeart()
        elif i > 10 and i <= 20:
            item = ItemDrone()
        elif i > 20 and i <= 40:
            item = ItemStar()        
          
        if item:
            item.build(x, y, self)
            self.addSpaceObject(item)
        
    def addItemTux(self, x, y):
        item = ItemTux()        
        item.build(x, y, self)
        self.addSpaceObject(item)
        
        
    def pause(self):
        self.isOnPause = True
            
    def loop(self, dt):
        
        self.gestionSon.loopMusic()
    
        if self.isOnPause:
            return False
            
        
        tps1 = time.clock()
        
               
               
        if self.spaceDecorationObjectListIndex >= len(self.m_oSpaceDecorationObjectList):
            self.spaceDecorationObjectListIndex = 0        
            
        while self.spaceDecorationObjectListIndex < len(self.m_oSpaceDecorationObjectList):
            oSpaceDecoObject = self.m_oSpaceDecorationObjectList[self.spaceDecorationObjectListIndex]
            if isinstance(oSpaceDecoObject, SpaceObject):
                if not oSpaceDecoObject.isDeleted():
                    oSpaceDecoObject.move(dt)
                    oSpaceDecoObject.anime(dt)
                else:
                    self.removeSpaceDecorationObject(oSpaceDecoObject)
            self.spaceDecorationObjectListIndex += 1                           
            if time.clock() - tps1 > 0.01:
                break;
        
        #for i in range(len(self.m_oSpaceDecorationObjectList)):
            
        # Decoupage en region pour 150 objets:
        # 1 region :  150*150 => 22500 cycles de collision
        # 4 regions : 50*50 + 30*30 + 20*20 + 50*50 => 6300 cycles => bien mieux
        # 6 regions : 25*25 + 30*30 +20*20 +10*10 +25*25 + 40*40 => 4250 cycles
        
                
        del(self.m_oRegion1_1ObjectList[:])
        del(self.m_oRegion1_2ObjectList[:])
        del(self.m_oRegion1_3ObjectList[:])
        del(self.m_oRegion1_4ObjectList[:])
        del(self.m_oRegion2_1ObjectList[:])
        del(self.m_oRegion2_2ObjectList[:])
        del(self.m_oRegion2_3ObjectList[:])
        del(self.m_oRegion2_4ObjectList[:])
        del(self.m_oRegion3_1ObjectList[:])
        del(self.m_oRegion3_2ObjectList[:])
        del(self.m_oRegion3_3ObjectList[:])
        del(self.m_oRegion3_4ObjectList[:])
        
        oRegionLimitVertical1 = self.space.size[0]/4
        oRegionLimitVertical2 = self.space.size[0]/2
        oRegionLimitVertical3 = self.space.size[0]*3/4
        
        oRegionLimitHorizontal1 = self.space.size[1]/3
        oRegionLimitHorizontal2 = self.space.size[1]*2/3
        
       
        
        for oSpaceObject in self.m_oSpaceObjectList:
             if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    #Logger.info("Pos: "+ str())
                    
                    #Region 1-1
                    if oSpaceObject.pos[0] <= oRegionLimitVertical1 and oSpaceObject.pos[1] <= oRegionLimitHorizontal1:
                        self.m_oRegion1_1ObjectList.append(oSpaceObject)                        
                    #Region 2-1
                    elif oSpaceObject.pos[0] <= oRegionLimitVertical1 and oSpaceObject.pos[1] > oRegionLimitHorizontal1 and oSpaceObject.pos[1] <= oRegionLimitHorizontal2:
                         self.m_oRegion2_1ObjectList.append(oSpaceObject)
                    #Region 3-1
                    elif oSpaceObject.pos[0] <= oRegionLimitVertical1 and oSpaceObject.pos[1] > oRegionLimitHorizontal2:
                         self.m_oRegion3_1ObjectList.append(oSpaceObject)
                         
                    #Region 1-2
                    if oSpaceObject.pos[0] > oRegionLimitVertical1 and oSpaceObject.pos[0] <= oRegionLimitVertical2 and oSpaceObject.pos[1] <= oRegionLimitHorizontal1:
                        self.m_oRegion1_2ObjectList.append(oSpaceObject)                        
                    #Region 2-2
                    elif oSpaceObject.pos[0] > oRegionLimitVertical1 and oSpaceObject.pos[0] <= oRegionLimitVertical2 and oSpaceObject.pos[1] > oRegionLimitHorizontal1 and oSpaceObject.pos[1] <= oRegionLimitHorizontal2:
                         self.m_oRegion2_2ObjectList.append(oSpaceObject)
                    #Region 3-2
                    elif oSpaceObject.pos[0] > oRegionLimitVertical1 and oSpaceObject.pos[0] <= oRegionLimitVertical2 and oSpaceObject.pos[1] > oRegionLimitHorizontal2:
                         self.m_oRegion3_2ObjectList.append(oSpaceObject)
                         
                    #Region 1-3
                    if oSpaceObject.pos[0] > oRegionLimitVertical2 and oSpaceObject.pos[0] <= oRegionLimitVertical3 and oSpaceObject.pos[1] <= oRegionLimitHorizontal1:
                        self.m_oRegion1_3ObjectList.append(oSpaceObject)                        
                    #Region 2-3
                    elif oSpaceObject.pos[0] > oRegionLimitVertical2 and oSpaceObject.pos[0] <= oRegionLimitVertical3 and oSpaceObject.pos[1] > oRegionLimitHorizontal1 and oSpaceObject.pos[1] <= oRegionLimitHorizontal2:
                         self.m_oRegion2_3ObjectList.append(oSpaceObject)
                    #Region 3-3
                    elif oSpaceObject.pos[0] > oRegionLimitVertical2 and oSpaceObject.pos[0] <= oRegionLimitVertical3 and oSpaceObject.pos[1] > oRegionLimitHorizontal2:
                         self.m_oRegion3_3ObjectList.append(oSpaceObject)
                         
                    #Region 1-4
                    if oSpaceObject.pos[0] > oRegionLimitVertical3 and oSpaceObject.pos[1] <= oRegionLimitHorizontal1:
                        self.m_oRegion1_4ObjectList.append(oSpaceObject)                        
                    #Region 2-4
                    elif oSpaceObject.pos[0] > oRegionLimitVertical3 and oSpaceObject.pos[1] > oRegionLimitHorizontal1 and oSpaceObject.pos[1] <= oRegionLimitHorizontal2:
                         self.m_oRegion2_4ObjectList.append(oSpaceObject)
                    #Region 3-4
                    elif oSpaceObject.pos[0] > oRegionLimitVertical3 and oSpaceObject.pos[1] > oRegionLimitHorizontal2:
                         self.m_oRegion3_4ObjectList.append(oSpaceObject)
                else:
                    self.removeSpaceObject(oSpaceObject)
        
        # boucle pour region 1-1
        i=0
        while i < len(self.m_oRegion1_1ObjectList):
            oSpaceObject = self.m_oRegion1_1ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion1_1ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion1_1ObjectList)))
            #    break;
        
        # boucle pour region 2-1
        i=0
        while i < len(self.m_oRegion2_1ObjectList):
            oSpaceObject = self.m_oRegion2_1ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion2_1ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion2_1ObjectList)))
            #    break;
            
        
        # boucle pour region 3-1
        i=0
        while i < len(self.m_oRegion3_1ObjectList):
            oSpaceObject = self.m_oRegion3_1ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion3_1ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion3_1ObjectList)))
            #    break;
            
        
        # boucle pour region 1-2
        i=0
        while i < len(self.m_oRegion1_2ObjectList):
            oSpaceObject = self.m_oRegion1_2ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion1_2ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion1_2ObjectList)))
            #    break;
            
        
        # boucle pour region 2-2
        i=0
        while i < len(self.m_oRegion2_2ObjectList):
            oSpaceObject = self.m_oRegion2_2ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion2_2ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion2_2ObjectList)))
            #    break;
            
        
        # boucle pour region 3-2
        i=0
        while i < len(self.m_oRegion3_2ObjectList):
            oSpaceObject = self.m_oRegion3_2ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion3_2ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion3_2ObjectList)))
            #    break;
            
        
        # boucle pour region 1-3
        i=0
        while i < len(self.m_oRegion1_3ObjectList):
            oSpaceObject = self.m_oRegion1_3ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion1_3ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion1_3ObjectList)))
            #    break;
            
        
        # boucle pour region 2-3
        i=0
        while i < len(self.m_oRegion2_3ObjectList):
            oSpaceObject = self.m_oRegion2_3ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion2_3ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion2_3ObjectList)))
            #    break;
            
        
        # boucle pour region 3-3
        i=0
        while i < len(self.m_oRegion3_3ObjectList):
            oSpaceObject = self.m_oRegion3_3ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion3_3ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion3_3ObjectList)))
            #    break;
            
        
        # boucle pour region 1-4
        i=0
        while i < len(self.m_oRegion1_4ObjectList):
            oSpaceObject = self.m_oRegion1_4ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion1_4ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion1_4ObjectList)))
            #    break;
         
        # boucle pour region 2-4
        i=0
        while i < len(self.m_oRegion2_4ObjectList):
            oSpaceObject = self.m_oRegion2_4ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion2_4ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion2_4ObjectList)))
            #    break;
         
        # boucle pour region 3-4
        i=0
        while i < len(self.m_oRegion3_4ObjectList):
            oSpaceObject = self.m_oRegion3_4ObjectList[i]
            if isinstance(oSpaceObject, SpaceObject):
                if not oSpaceObject.isDeleted():
                    oSpaceObject.move(dt)
                    oSpaceObject.anime(dt)
                    if oSpaceObject.canCollision():
                       for oOtherSpaceObject in self.m_oRegion3_4ObjectList:
                           if oOtherSpaceObject != oSpaceObject and oOtherSpaceObject.canCollision() and oSpaceObject.collide_widget(oOtherSpaceObject) :
                                   oSpaceObject.collision(oOtherSpaceObject) 
            i += 1 
            #if time.clock() - tps1 > 0.01:
            #    Logger.info("SO: "+str(i)+" | len: "+str(len(self.m_oRegion3_4ObjectList)))
            #    break;
               
        
                
        # Logger.info("object: "+str(len(self.m_oSpaceObjectList))+" | tps: "+str(time.clock() - tps1))
        # Logger.info("########### THE END  ###########")
              
        self.m_oNiveau.whatHappens()
    
    
    def showEcranFormation(self): 
        self.pause()
        self.ecranFormation = EcranFormation()
        self.ecranFormation.build(self)
        self.ecranFormation.size = self.size
        self.add_widget(self.ecranFormation)
        
    def cacherEcranFormation(self, dt): 
        self.remove_widget(self.ecranFormation)
        self.ecranFormation = None
        self.run()
        
    def showEcranAccueil(self): 
        self.ecranAccueil = EcranAccueil()
        self.ecranAccueil.build(self)
        self.ecranAccueil.size = self.size
        self.add_widget(self.ecranAccueil)
        
    def cacherEcranAccueil(self, dt): 
        self.remove_widget(self.ecranAccueil)
        self.ecranAccueil = None
       
        
    def showEcranNiveaux(self): 
        self.pause()
        self.m_oNiveau.niveau = None
        self.ecranNiveaux = EcranNiveaux()
        self.ecranNiveaux.build(self)
        self.ecranNiveaux.size = self.size
        self.add_widget(self.ecranNiveaux)
        
    def cacherEcranNiveaux(self, dt): 
        self.remove_widget(self.ecranNiveaux)
        self.ecranNiveaux = None
        
    def showEcranPause(self): 
        self.pause()
        self.ecranPause = EcranPause()
        self.ecranPause.build(self)
        self.ecranPause.size = self.size
        self.add_widget(self.ecranPause)
        
    def cacherEcranPause(self, dt): 
        self.remove_widget(self.ecranPause)
        self.ecranPause = None
        
    def showEcranStat(self): 
        self.pause()
        self.ecranStat = EcranStat()
        self.ecranStat.build(self)
        self.ecranStat.size = self.size
        self.add_widget(self.ecranStat)
        
    def cacherEcranStat(self, dt): 
        self.remove_widget(self.ecranStat)
        self.ecranStat = None
        
    def showEcranGameOver(self): 
        self.pause()
        self.ecranGameOver = EcranGameOver()
        self.ecranGameOver.build(self)
        self.ecranGameOver.size = self.size
        self.add_widget(self.ecranGameOver)
        
    def cacherEcranGameOver(self, dt): 
        self.remove_widget(self.ecranGameOver)
        self.ecranGameOver = None
        
    def showEcranCredit(self): 
        self.ecranCredit = EcranCredit()
        self.ecranCredit.build(self)
        self.ecranCredit.size = self.size
        self.add_widget(self.ecranCredit)
        
    def cacherEcranCredit(self, dt): 
        self.remove_widget(self.ecranCredit)
        self.ecranCredit = None
        
    def showEcranNiveauName(self): 
        self.ecranNiveauName = EcranNiveauName()
        self.ecranNiveauName.build(self)
        self.ecranNiveauName.size = self.size
        self.add_widget(self.ecranNiveauName)
        
    def cacherEcranNiveauName(self, dt): 
        self.remove_widget(self.ecranNiveauName)
        self.ecranNiveauName = None
             
    

class SpaceGame(Widget):  
    pass
    
class SpaceForeground(Widget):  
    pass
            
class SpaceBackground(Widget):    
    source = StringProperty(None)
    
        
class SpaceScreen(Widget):
    game = ObjectProperty(None)
    background = ObjectProperty(None)
    foreground = ObjectProperty(None)
    spacegame = ObjectProperty(None)
    
    def build(self, p_oGame):
        self.game = p_oGame
        self.background.source = 'images/eso0927a.jpg'
    
    def touch(self, x, y):
        self.game.m_oSpaceShip.moveTo(x, y)
        
        
class Scan(Widget):
    game = ObjectProperty(None)
            
    def pause(self):
        self.game.showEcranPause()

class TableauScreen(Widget):
    shootBtn = ObjectProperty(None)
    formatBtn = ObjectProperty(None)
    game = ObjectProperty(None)
    scanview = ObjectProperty(None)
    heartLbl = ObjectProperty(None)
    starLbl = ObjectProperty(None) 
    
    def build(self, p_oGame):
        self.game = p_oGame
        self.shootBtn.game = self.game
        self.formatBtn.game = self.game
        self.scanview.game = self.game
        self.heartLbl.text = str(self.game.heart)
        self.starLbl.text = str(self.game.star)
               

class SpaceObject:
    
    def __init__(self, p_oGame=None):
        self.m_pxPerSecond = 0
        self.m_degreePerSecond = 0
        self.m_name = 'Inconnu'
        self.m_deleteMe = False
        self.isTouched = False
        self.canMove = True
        self.equipe = 'aucune'
        self.game = p_oGame
        self.isBack = False
        self.canScanIt = False
        self.vie = 1   
            
    def move(self, dt):
        pass
        
    def anime(self, dt): 
        pass
        
    def collision(self, p_oOtherSpaceObject):
        pass
        
    def delete(self, dt=0):
        self.m_deleteMe = True
        
    def isDeleted(self):
        return self.m_deleteMe
        
    def canCollision(self):
        return not self.isTouched   

    def setSize(self, width, height):
        pass
        
    def setPosition(self, x, y):
        pass
        
    def setMovement(self, velx, vely, rot):
        pass
        
    def setGame(self, p_oGame):
        self.game = p_oGame
    
    def setScanObject(self, p_oScanObject):
        self.scanObject = p_oScanObject

    
class ScanObject(Scatter):

    def __init__(self, p_oSpaceObject, p_oGame):
        Scatter.__init__(self)
        self.oSpaceObject = p_oSpaceObject
        self.game = p_oGame
        p_oSpaceObject.setScanObject(self)
       
        self.size = 5, 5
        
        self.setPosition(p_oSpaceObject)
        
        
    def setPosition(self, p_oSpaceObject):
        testPosX =  p_oSpaceObject.x *  self.game.tableau.scanview.width / self.game.width
        testPosY =  p_oSpaceObject.y * self.game.tableau.scanview.height/ self.game.height 
        
        scanPos = self.game.tableau.scanview.to_parent(testPosX, testPosY, relative=True)

        if scanPos[0] >= self.game.tableau.scanview.x and scanPos[0] <= (self.game.tableau.scanview.x + self.game.tableau.scanview.width) and scanPos[1] >= self.game.tableau.scanview.y and scanPos[1] <= (self.game.tableau.scanview.y + self.game.tableau.scanview.height):
         
            self.pos = scanPos
           
        else:
            self.pos = -50, -50
        
    
            
class Explose(Scatter,SpaceObject):

    #imageTexture = ObjectProperty(None)

    def __init__(self):
        Scatter.__init__(self)
        SpaceObject.__init__(self)
        
        #self.textureAnime = TextureAnime(texture=self.imageTexture,loop=False)
        
        #self.imageTexture = self.textureAnime.first()
        
        
    def setPosition(self, x, y):
        self.pos = x, y
        
    def anime(self, dt): 
    #    texture = self.textureAnime.getAt()
    #    if texture:
    #        self.imageTexture = texture
    #        
    #        if self.textureAnime.getLoopCount() > 0:
    #            self.textureAnime = None
    #            self.imageTexture = None
        self.delete()
        
class LaserExplose(Scatter,SpaceObject):
    
    def __init__(self):
        Scatter.__init__(self)
        SpaceObject.__init__(self)     
        
    def setPosition(self, x, y):
        self.pos = x, y  
        
    def anime(self, dt): 
        self.delete()   
     
    
class AsteroidDeco(Scatter, SpaceObject):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    touchCount = NumericProperty(0)
    
    def __init__(self):
        Scatter.__init__(self)
        SpaceObject.__init__(self)
        
        self.pos = 0, 0
        self.size = 0, 0
        self.isBack = True

    def setSize(self, widht, height):
        self.size = widht, height
        
    def setPosition(self, x, y):
        self.pos = x, y
        
    def setMovement(self, velx, vely, rot):
        self.velocity_x = velx
        self.velocity_y = vely
        self.m_degreePerSecond = rot
    
    def move(self, dt): 
                
        self.pos = Vector(*self.velocity)*dt + self.pos
        self.rotation = self.rotation + self.m_degreePerSecond*dt
      
        if self.x < (0 - self.width):
            self.delete()
            
    
            
class Asteroid(Scatter, SpaceObject):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def __init__(self):
        Scatter.__init__(self)
        SpaceObject.__init__(self)
        
        self.pos = 0, 0
        self.size = 0, 0
        self.canScanIt = True
        self.touchCount = 0
        self.vie = 8

    def setSize(self, widht, height):
        self.size = widht, height
        
    def setPosition(self, x, y):
        self.pos = x, y
        
    def setMovement(self, velx, vely, rot):
        self.velocity_x = velx
        self.velocity_y = vely
        self.m_degreePerSecond = rot
        
    def move(self, dt): 
                
        self.pos = Vector(*self.velocity)*dt + self.pos
        self.rotation = self.rotation + self.m_degreePerSecond*dt
        
        self.scanObject.setPosition(self)
      
        if self.x < (0 - self.width):
            self.delete()
            
    def setTouch(self, p_touch): 
        self.isTouched = p_touch    
    
    def collision(self, p_oOtherSpaceObject):  
    
        if not isinstance(p_oOtherSpaceObject, Asteroid) and not isinstance(p_oOtherSpaceObject, Item):
                        
            puissance = 1
            if isinstance(p_oOtherSpaceObject, Laser):
                puissance = p_oOtherSpaceObject.puissance
            elif isinstance(p_oOtherSpaceObject, SpaceShip):    
                puissance = self.vie
            
            self.vie -= puissance
            
                    
            if self.vie <= 0 :
                self.game.addExplosion(self.x, self.y)
                self.game.gestionSon.playAsteroidExplosion()
                self.isTouched = True
                
                self.game.addItem(self.x, self.y)
                
                self.delete()
        
        
class SpaceShip(Scatter, SpaceObject):

    posx = NumericProperty(0)
    posy = NumericProperty(0)
    
    velocity_x = NumericProperty(500)
    velocity_y = NumericProperty(500)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def __init__(self, x=0, y=0):
        Scatter.__init__(self)
        SpaceObject.__init__(self)
        self.canScanIt = True
        
        self.equipe = 'joueur1'
        
        self.pos = x, y
        self.posx = x
        self.posy = y
                
    def moveTo(self, x, y):
        self.posx = x - self.width / 2
        self.posy = y - self.height / 2
        
    def move(self, dt):        
        if self.canMove :
            
            newposx = self.x
            if self.posx <> self.x:
                nbrpx = self.velocity_x * dt
                
                if self.posx < self.x:
                    nbrpx *= -1
                                    
                if abs(self.posx - self.x) < abs(nbrpx):
                    newposx = self.posx
                else:
                    newposx =  newposx + nbrpx
                
            newposy = self.y
            if self.posy <> self.y:
                nbrpx = self.velocity_y * dt
                
                if self.posy < self.y:
                    nbrpx *= -1
                                    
                if abs(self.posy - self.y) < abs(nbrpx):
                    newposy = self.posy
                else:
                    newposy =  newposy + nbrpx    
                
               
            self.pos = newposx, newposy
                  
            self.scanObject.setPosition(self)
        
    def getItem(self, p_oItem):
        if isinstance(p_oItem, ItemLaserUp):
            self.game.laserType += 1
        elif isinstance(p_oItem, ItemHeart):
            self.game.addHeart()
        elif isinstance(p_oItem, ItemDrone):
            self.game.addDrone()
        elif isinstance(p_oItem, ItemStar):
            self.game.addStar()
        elif isinstance(p_oItem, ItemTux):
            self.game.touchItemTux()
        
    def enableTouch(self, dt):
        self.isTouched = False
        
    def collision(self, p_oOtherSpaceObject):
        if  not isinstance(p_oOtherSpaceObject, Drone) and not isinstance(p_oOtherSpaceObject, Item) and self.equipe != p_oOtherSpaceObject.equipe:
            self.isTouched = True
            self.game.deleteHeart()
            self.explose()
            if  not isinstance(p_oOtherSpaceObject, Laser):
                p_oOtherSpaceObject.collision(self)
            Clock.schedule_once(self.enableTouch, 1)
            
        elif isinstance(p_oOtherSpaceObject, Item):
            self.getItem(p_oOtherSpaceObject)
        
        
    def explose(self):  
        self.game.addExplosion(self.x, self.y)
        self.game.gestionSon.playSpaceShipExplosion()
      
      
class Drone(Scatter, SpaceObject):
    
    velocity_x = NumericProperty(300)
    velocity_y = NumericProperty(300)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
        
    def __init__(self, p_nId, p_oSpaceShip):
        Scatter.__init__(self)
        SpaceObject.__init__(self)
        
        self.equipe = p_oSpaceShip.equipe
        self.droneId = p_nId
        self.oSpaceShip = p_oSpaceShip
        self.oFormation = Formation(self.oSpaceShip)
        self.canScanIt = True
        
        self.anim_x = 0
        self.anim_y = 0
        
    def move(self, dt): 
        posx, posy = self.oFormation.getPosition(self.droneId)
        posx += self.anim_x
        posy += self.anim_y
        
        if self.canMove :
            
            newposx = self.x
            if posx <> self.x:
                nbrpx = self.velocity_x * dt
                
                if posx < self.x:
                    nbrpx *= -1
                    
                                    
                if abs(posx - self.x) < abs(nbrpx):
                    newposx = posx
                else:
                    newposx =  newposx + nbrpx 
                
                
            newposy = self.y
            if posy <> self.y:
                nbrpx = self.velocity_y * dt
                
                if posy < self.y:
                    nbrpx *= -1 
                                    
                if abs(posy - self.y) < abs(nbrpx):
                    newposy = posy
                else:
                    newposy =  newposy + nbrpx 
                
                
               
            self.pos = newposx, newposy
            self.scanObject.setPosition(self)
            
            
    def anime(self, dt): 
        i = randint(0,20)
        if i==1:
            self.anim_y = randint(-20, 20)            
        
    def collision(self, p_oOtherSpaceObject):
        if not isinstance(p_oOtherSpaceObject, SpaceShip) and not isinstance(p_oOtherSpaceObject, Drone) and not isinstance(p_oOtherSpaceObject, Item) and self.equipe != p_oOtherSpaceObject.equipe:
            self.explose()
            self.isTouched = True
            self.delete()
            
        elif isinstance(p_oOtherSpaceObject, Item):
            self.oSpaceShip.getItem(p_oOtherSpaceObject)
        
    def explose(self):  
        self.game.addExplosion(self.x, self.y)
        self.game.gestionSon.playDroneExplosion()
        
        
        
class SpaceShipVx32(Scatter, SpaceObject):

    posx = NumericProperty(0)
    posy = NumericProperty(0)
    
    velocity_x = NumericProperty(100)
    velocity_y = NumericProperty(100)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def __init__(self, x=0, y=0):
        Scatter.__init__(self)
        SpaceObject.__init__(self)
        
        self.equipe = 'zhooss'
        
        self.pos = x, y
        self.posx = x
        self.posy = y
        self.canScanIt = True
        self.vie = 5
        
    def setPosition(self, x, y):
        self.pos = x, y
        
        self.moveTo(-100, self.y)
                
    def moveTo(self, x, y):
        self.posx = x 
        self.posy = y 
        
    def move(self, dt): 
    
        if self.x < (0 - self.width):
           self.delete()
           
        i = randint(0, 100)
        if i==0:
            unLaser = Laser()
            unLaser.build(self, directionx=-1,directiony=0, game=self.game)
            self.game.addSpaceObject(unLaser) 
        
        if self.canMove : 
            newposx = self.x
            if self.posx <> self.x:
                nbrpx = self.velocity_x * dt
                
                if self.posx < self.x:
                    nbrpx *= -1
                                    
                if abs(self.posx - self.x) < abs(nbrpx):
                    newposx = self.posx
                else:
                    newposx =  newposx + nbrpx
                    
            newposy = self.y
            if self.posy <> self.y:
                nbrpx = self.velocity_y * dt
                
                if self.posy < self.y:
                    nbrpx *= -1
                                    
                if abs(self.posy - self.y) < abs(nbrpx):
                    newposy = self.posy
                else:
                    newposy =  newposy + nbrpx    
               
            self.pos = newposx, newposy
            self.scanObject.setPosition(self)        
        
    def collision(self, p_oOtherSpaceObject):
        if self.equipe != p_oOtherSpaceObject.equipe:
            
            puissance = 1
            if isinstance(p_oOtherSpaceObject, Laser):
                puissance = p_oOtherSpaceObject.puissance
            elif isinstance(p_oOtherSpaceObject, SpaceShip):    
                puissance = self.vie
            
            self.vie -= puissance
                    
            if self.vie <= 0 :
                self.explose()
                self.isTouched = True
                self.delete()
        
    def explose(self):  
        self.game.addExplosion(self.x, self.y)
        self.game.gestionSon.playSpaceShipExplosion()
        
        
class SpaceShipVx56(SpaceShipVx32):
    def __init__(self):
        SpaceShipVx32.__init__(self)
        self.velocity_x = 200
        self.vie = 10
     
    def move(self, dt): 

        if self.x < (0 - self.width):
           self.delete()
           
        i = randint(0, 50)   
        if i==0:
            self.moveTo(-100, self.game.m_oSpaceShip.y + randint(-50, 50))
           
        i = randint(0, 10)
        if i==0:
            unLaser = Laser2()
            unLaser.build(self, directionx=-1,directiony=0, game=self.game)
            self.game.addSpaceObject(unLaser)
        
        if self.canMove :
            
            newposx = self.x
            if self.posx <> self.x:
                nbrpx = self.velocity_x * dt
                
                if self.posx < self.x:
                    nbrpx *= -1
                                    
                if abs(self.posx - self.x) < abs(nbrpx):
                    newposx = self.posx
                else:
                    newposx =  newposx + nbrpx
                
            newposy = self.y
            if self.posy <> self.y:
                nbrpx = self.velocity_y * dt
                
                if self.posy < self.y:
                    nbrpx *= -1
                                    
                if abs(self.posy - self.y) < abs(nbrpx):
                    newposy = self.posy
                else:
                    newposy =  newposy + nbrpx    
               
            self.pos = newposx, newposy
            self.scanObject.setPosition(self) 
            
        
class SpaceShipT34(SpaceShipVx32):
    def __init__(self):
        SpaceShipVx32.__init__(self)
        self.velocity_x = 200
        self.velocity_y = 200
        self.vie = 15
        
    def move(self, dt): 

        if self.x < (0 - self.width):
           self.delete()
           
        i = randint(0, 30)   
        if i==0:
            self.moveTo(randint(50,1000), self.game.m_oSpaceShip.y + randint(-200, 200))
           
        i = randint(0, 10)
        if i==0:
            unLaser = Laser2()
            unLaser.build(self, directionx=-1,directiony=0, game=self.game)
            self.game.addSpaceObject(unLaser)
        
        if self.canMove :
            
            newposx = self.x
            if self.posx <> self.x:
                nbrpx = self.velocity_x * dt
                
                if self.posx < self.x:
                    nbrpx *= -1
                                    
                if abs(self.posx - self.x) < abs(nbrpx):
                    newposx = self.posx
                else:
                    newposx =  newposx + nbrpx
                
            newposy = self.y
            if self.posy <> self.y:
                nbrpx = self.velocity_y * dt
                
                if self.posy < self.y:
                    nbrpx *= -1
                                    
                if abs(self.posy - self.y) < abs(nbrpx):
                    newposy = self.posy
                else:
                    newposy =  newposy + nbrpx    
               
            self.pos = newposx, newposy
            self.scanObject.setPosition(self)   
            
        
class SpaceShipT48(SpaceShipVx32):
    def __init__(self):
        SpaceShipVx32.__init__(self)
        self.velocity_x = 300
        self.velocity_y = 300
        self.vie = 30
    
    def move(self, dt): 

        if self.x < (0 - self.width):
           self.delete()
           
        i = randint(0, 20)   
        if i==0:
            self.moveTo(self.game.m_oSpaceShip.x + randint(50,200), self.game.m_oSpaceShip.y + randint(-100, 100))
           
        i = randint(0, 10)
        if i==0 or self.game.m_oSpaceShip.y == self.y:
            unLaser = Laser2()
            unLaser.build(self, directionx=-1,directiony=0, game=self.game)
            self.game.addSpaceObject(unLaser)
        
        if self.canMove :
            
            newposx = self.x
            if self.posx <> self.x:
                nbrpx = self.velocity_x * dt
                
                if self.posx < self.x:
                    nbrpx *= -1
                                    
                if abs(self.posx - self.x) < abs(nbrpx):
                    newposx = self.posx
                else:
                    newposx =  newposx + nbrpx
                
            newposy = self.y
            if self.posy <> self.y:
                nbrpx = self.velocity_y * dt
                
                if self.posy < self.y:
                    nbrpx *= -1
                                    
                if abs(self.posy - self.y) < abs(nbrpx):
                    newposy = self.posy
                else:
                    newposy =  newposy + nbrpx    
              
            self.pos = newposx, newposy
            self.scanObject.setPosition(self)
        
        
class Item(Scatter, SpaceObject):
           
    def __init__(self):
        Scatter.__init__(self)
        SpaceObject.__init__(self)
        self.canMove = True
        self.m_pxPerSecond = 10
    
    def build(self, x, y, game=None):
        self.m_name = 'Item'
        self.game = game
        
        self.pos = x,y
        
    def setPosition(self, x, y):
        self.pos = x, y
                
    
    def move(self, dt):  
        newposx =  self.x + self.m_pxPerSecond * dt  * -1  
                        
        if self.x < (0 - self.width) or self.x > Window.width + self.width or self.y < 0 or self.y > Window.height + self.height:
            self.delete()
            
        self.pos = newposx , self.y
        
    def collision(self, p_oOtherSpaceObject):
        
        if isinstance(p_oOtherSpaceObject, SpaceShip) or isinstance(p_oOtherSpaceObject, Drone):
            self.isTouched = True
            self.game.gestionSon.playGetItem()
            
        if not isinstance(p_oOtherSpaceObject, Asteroid) and not isinstance(p_oOtherSpaceObject, Laser):
            self.delete()
            
            
class ItemStar(Item):
    def __init__(self):
        Item.__init__(self)
        
class ItemDrone(Item):
    def __init__(self):
        Item.__init__(self)
        
class ItemLaserUp(Item):
    def __init__(self):
        Item.__init__(self)
        
class ItemHeart(Item):
    def __init__(self):
        Item.__init__(self)
        
class ItemTux(Item):
    def __init__(self):
        Item.__init__(self)
        self.m_pxPerSecond = 50
        
    def move(self, dt):  
        newposx =  self.x + self.m_pxPerSecond * dt  * -1  
                        
        if self.x > Window.width /2:
            self.pos = newposx , self.y
                        
    def collision(self, p_oOtherSpaceObject):
        pass
            
   
class Laser(Scatter, SpaceObject):
        
    def __init__(self):
        Scatter.__init__(self)
        SpaceObject.__init__(self)
        self.canMove = True
        self.m_pxPerSecond = 500
        self.puissance = 1
    
    def build(self, oSniperSpaceObject, directionx=1,directiony=0, game=None):
        self.m_name = 'Laser'
        self.equipe = oSniperSpaceObject.equipe
        self.oSniperSpaceObject = oSniperSpaceObject
        self.game = game
        
        self.direction = directionx, directiony
        
        self.initPos(oSniperSpaceObject.x + (oSniperSpaceObject.width / 1.3), oSniperSpaceObject.y + (oSniperSpaceObject.height/2))
        
        self.playLaserSound()

    def playLaserSound(self):
        if not isinstance(self.oSniperSpaceObject, Drone):
            self.game.gestionSon.playLaser()
    
    def initPos(self, x, y):
        self.pos = x,y
        
    
    def move(self, dt):  
        if self.canMove:
            newposx =  self.x + self.m_pxPerSecond * dt  * self.direction[0]   
            newposy =  self.y + self.m_pxPerSecond * dt  * self.direction[1]              
            self.pos = newposx , newposy
                        
        if self.x < (0 - self.width) or self.x > Window.width + self.width or self.y < 0 or self.y > Window.height:
            self.delete()
        
    def collision(self, p_oOtherSpaceObject):  
        if p_oOtherSpaceObject != self.oSniperSpaceObject and not isinstance(p_oOtherSpaceObject, Laser) and self.oSniperSpaceObject.equipe != p_oOtherSpaceObject.equipe:
            self.game.addLaserExplosion(self.x, self.y)
            self.game.gestionSon.playLaserExplosion()
            self.canMove = False
            self.isTouched = True
            p_oOtherSpaceObject.collision(self)
            self.delete()
            
  
class Laser2(Laser):
    def __init__(self):
        Laser.__init__(self)
        self.m_pxPerSecond = 300
        self.puissance = 5
        
    def playLaserSound(self):
        if not isinstance(self.oSniperSpaceObject, Drone):
            self.game.gestionSon.playLaser2()
            
class Laser3(Laser):
    def __init__(self):
        Laser.__init__(self)
        self.m_pxPerSecond = 500
        self.puissance = 8
        
    def playLaserSound(self):
        if not isinstance(self.oSniperSpaceObject, Drone):
            self.game.gestionSon.playLaser3()
            
             
            
class LaserButton(Widget):

    game = ObjectProperty(None)
            
    def shoot(self):  
        self.game.shoot()
        
        
class FormationButton(Widget):

    game = ObjectProperty(None)
            
    def changeFormation(self):  
       
        self.game.showEcranFormation()
    
    
class Formation():

    def __init__(self, p_oSpaceObjectReference):
        self.formationId = 3
        self.oSpaceObjectReference = p_oSpaceObjectReference
        
    def changeFormation(self, p_nFormationId=0):
        if p_nFormationId <> 0:
            self.formationId = p_nFormationId
        else:
            self.formationId = (self.formationId %4) + 1
           
            
    
    def changeFormationTo(self, p_sFormation):        
        if p_sFormation == "ligne":
            self.formationId = 1
        elif p_sFormation == "vertical":
            self.formationId = 2
        elif p_sFormation == "lance":
            self.formationId = 3
        elif p_sFormation == "protection":
            self.formationId = 4
                
    def formation1(self, p_oSpaceObjectId):
    
        posx = self.oSpaceObjectReference.x - p_oSpaceObjectId * 50
        posy = self.oSpaceObjectReference.y
    
        return posx, posy
        
    def formation2(self, p_oSpaceObjectId):
    
        posx = self.oSpaceObjectReference.x
        
        if p_oSpaceObjectId == 1:
            posy = self.oSpaceObjectReference.y + 50 
        elif p_oSpaceObjectId == 2:
            posy = self.oSpaceObjectReference.y - 50 
        elif p_oSpaceObjectId == 3:
            posy = self.oSpaceObjectReference.y + 100 
        elif p_oSpaceObjectId == 4:
            posy = self.oSpaceObjectReference.y - 100 
          
        return posx + 10, posy 
        
    def formation3(self, p_oSpaceObjectId):
            
        if p_oSpaceObjectId == 1:
            posx = self.oSpaceObjectReference.x - 50
            posy = self.oSpaceObjectReference.y + 30 
        elif p_oSpaceObjectId == 2:
            posx = self.oSpaceObjectReference.x - 50
            posy = self.oSpaceObjectReference.y - 30 
        elif p_oSpaceObjectId == 3:
            posx = self.oSpaceObjectReference.x - 100
            posy = self.oSpaceObjectReference.y + 60 
        elif p_oSpaceObjectId == 4:
            posx = self.oSpaceObjectReference.x - 100
            posy = self.oSpaceObjectReference.y - 60 
          
        return posx, posy 
        
    def formation4(self, p_oSpaceObjectId):
            
        if p_oSpaceObjectId == 1:
            posx = self.oSpaceObjectReference.x + 80
            posy = self.oSpaceObjectReference.y + 30 
        elif p_oSpaceObjectId == 2:
            posx = self.oSpaceObjectReference.x + 80
            posy = self.oSpaceObjectReference.y - 30 
        elif p_oSpaceObjectId == 3:
            posx = self.oSpaceObjectReference.x + 100
            posy = self.oSpaceObjectReference.y + 10 
        elif p_oSpaceObjectId == 4:
            posx = self.oSpaceObjectReference.x + 100
            posy = self.oSpaceObjectReference.y - 10 
          
        return posx, posy 
    
    def getPosition(self, p_oSpaceObjectId):  
        newPosition = 0,0
        
        if self.formationId == 1:
            newPosition = self.formation1(p_oSpaceObjectId)
            
        elif self.formationId == 2:
            newPosition = self.formation2(p_oSpaceObjectId)
            
        elif self.formationId == 3:
            newPosition = self.formation3(p_oSpaceObjectId)
            
        elif self.formationId == 4:
            newPosition = self.formation4(p_oSpaceObjectId)
            
        return newPosition
        
        
class EcranFormation(Widget):
    game = ObjectProperty(None)
    
    def build(self, p_oGame):
        self.game = p_oGame
        self.gdb = GestureDatabase()

        self.gdb.add_gesture(ligne)
        self.gdb.add_gesture(lance)
        self.gdb.add_gesture(vertical)
     
    def on_touch_down(self, touch):
        userdata = touch.ud
        with self.canvas:
            Color(0.5, 1, 1)
            Point(points=(touch.x, touch.y), source='particle.png', pointsize=5)
            userdata['line'] = Line(points=(touch.x, touch.y))
               
        return True

    def on_touch_move(self, touch):
        try:                 
                     
            ud = touch.ud
            ud['line'].points += [touch.x, touch.y]
            points= ud['line'].points
            oldx, oldy = points[len(points)-4], points[len(points)-3]
            pointsTmp = self.calculate_points(oldx, oldy, touch.x, touch.y, steps=1)
            if pointsTmp:
                try:
                    for idx in xrange(0, len(pointsTmp), 2):
                        self.canvas.add(Point(points=(pointsTmp[idx], pointsTmp[idx+1]), source='particle.png', pointsize=5))
                except GraphicException:
                    pass
                
            return True
        except (KeyError), e:
            pass
 
     
    def on_touch_up(self, touch):
        
        g = self.simplegesture(
                '',
                zip(touch.ud['line'].points[::2], touch.ud['line'].points[1::2])
                )
        
        #Logger.info("gesture representation: "+ self.gdb.gesture_to_str(g))

        g2 = self.gdb.find(g, minscore=0.85)

        formation = "None"
        
        if g2:
            if g2[1] == ligne: formation = "ligne"
            elif g2[1] == lance: formation = "lance"
            elif g2[1] == vertical: formation = "vertical"
                
        #if formation <> "None":     
        #    self.add_widget(Label(text='ok', center_x= self.game.width / 2, center_y= self.game.height / 2))
        
        self.changeFormation(formation)
        
        Clock.schedule_once(self.game.cacherEcranFormation, 1)
        
    def calculate_points(self, x1, y1, x2, y2, steps=5):
        dx = x2 - x1
        dy = y2 - y1
        dist = sqrt(dx * dx + dy * dy)
        if dist < steps:
            return None
        o = []
        m = dist / steps
        for i in xrange(1, int(m)):
            mi = i / m
            lastx = x1 + dx * mi
            lasty = y1 + dy * mi
            o.extend([lastx, lasty])
        return o
        
    def simplegesture(self, name, point_list):
        g = Gesture()
        g.add_stroke(point_list)
        g.normalize()
        g.name = name
        return g
        
    def changeFormation(self, formation):  
        self.game.m_oDrone1.oFormation.changeFormationTo(formation)
        self.game.m_oDrone2.oFormation.changeFormationTo(formation)
        self.game.m_oDrone3.oFormation.changeFormationTo(formation)
        self.game.m_oDrone4.oFormation.changeFormationTo(formation)
         
        
        
class GestionNiveau:
  
    def __init__(self, p_oGame):
        self.niveau = None
        self.game = p_oGame
        self.lastAction = 0
        self.niveauTime = 0 
               
 
    def load(self):  
        self.niveau.load()
        self.game.space.background.source = self.niveau.image
        self.game.gestionSon.loadMusic(self.niveau.music)
        self.lastAction = 0
        self.niveauTime = 0 
        
    def setNiveau(self, p_oNiveau):  
        self.niveau = p_oNiveau
        self.niveau.generate()
        self.load()
        
    def loadNiveau(self,niveauId):  
        self.loadFromFile(niveauId)
        
    def loadFromFile(self,niveauId):  
        currentPathTmp = os.getcwd()
        chdir(os.path.dirname( __file__))
                
        file_niv = open('niveaux/niveau-'+niveauId+'.niv', 'r') 
        self.niveau = None
        self.lastAction = 0
        self.niveau = pickle.load(file_niv)
        
        chdir(currentPathTmp)
                
        self.load()
            
    def saveToFile(self):
        currentPathTmp = os.getcwd()
        chdir(os.path.dirname( __file__))
        
        file_niv = open('niveaux/niveau-'+self.niveau.id+'.niv', 'w') 
        pickle.dump(self.niveau, file_niv) 
      
        chdir(currentPathTmp)
                
    def whatHappens(self):
        self.niveauTime += 0.01 
        doAction = True
        while doAction:
            newAct = self.lastAction + 1
            if newAct in self.niveau.actions:
                act = self.niveau.actions[newAct]
                if act.time < self.niveauTime:
                    
                    if act.type == 'create':
                    
                        if act.object == 'ItemTux': 
                            self.game.addItemTux( act.position[0], act.position[1])
                        else:     
                            spaceObject = eval(act.object+'()')
                            
                            spaceObject.setGame(self.game)
                            
                            spaceObject.setSize(act.size[0], act.size[1])
                            spaceObject.setPosition( act.position[0], act.position[1])
                            spaceObject.setMovement(act.movement[0], act.movement[1], act.movement[2])
                                                 
                            if act.isDeco:
                                self.isBack = True
                                self.game.addSpaceDecorationObject(spaceObject)
                            else:
                                self.game.addSpaceObject(spaceObject)
                            
                        self.lastAction = newAct
                        
                    elif act.type == 'end':    
                        doAction = False
                        self.lastAction = newAct
                        self.game.nextNiveaux()
                        
                else:
                    doAction = False
            else:
                doAction = False
        
   
   
class EcranAccueil(Widget):
    game = ObjectProperty(None)
    
    def build(self, p_oGame):
        self.game = p_oGame
        if self.game.gestionSon.musicIsStop():
            self.game.gestionSon.loadMusic('05-Adam CASTILLO-Massacre Part 1.ogg')
            self.game.gestionSon.playMusic()
        
    def next(self):
        self.game.cacherEcranAccueil(None)
        self.game.init()
        self.game.loadNiveaux()
        
    def credit(self):
        self.game.cacherEcranAccueil(None)
        self.game.showEcranCredit()
        
    def quit(self):
        self.game.cacherEcranAccueil(None)
        self.game.quitGame()
        
               
class EcranNiveaux(Widget):
    game = ObjectProperty(None)
    
    def build(self, p_oGame):
        self.game = p_oGame
        if self.game.gestionSon.musicIsStop():
            self.game.gestionSon.loadMusic('05-Adam CASTILLO-Massacre Part 1.ogg')
            self.game.gestionSon.playMusic()
     
    def start(self, sNiveauId):
        self.game.cacherEcranNiveaux(None)
        
        self.game.loadNiveaux()
        
    def accueil(self):
        self.game.cacherEcranNiveaux(None)
        self.game.showEcranAccueil()
        
class EcranStat(Widget):
    game = ObjectProperty(None)
    
    def build(self, p_oGame):
        self.game = p_oGame
       
    def next(self):
        self.game.cacherEcranStat(None) 
        self.game.loadNiveaux()
        
class EcranGameOver(Widget):
    game = ObjectProperty(None)
    tuxLbl = ObjectProperty(None)
    starLbl = ObjectProperty(None)
    
    def build(self, p_oGame):
        self.game = p_oGame    
        
        self.tuxLbl.text = str(self.game.niveauNbr - 1)
        self.starLbl.text = str(self.game.star)
        
        self.game.gestionSon.loadMusic('05-Adam CASTILLO-Massacre Part 1.ogg')
        self.game.gestionSon.playMusic()
     
    def next(self):
        self.game.cacherEcranGameOver(None)
        self.game.showEcranAccueil()
        
        
class EcranCredit(Widget):
    game = ObjectProperty(None)
    
    def build(self, p_oGame):
        self.game = p_oGame
        
        currentPathTmp = os.getcwd()
        chdir(os.path.dirname( __file__))
        
        f=open("credits",'r')
        
        chdir(currentPathTmp)
        
        layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        
        while 1:
            txt = f.readline().rstrip('\n\r')
            
            if txt =='':
                break
             
            c=Label(text=txt,color=( 1,0,0,1), size_hint_y=None, height=40)    
            layout.add_widget(c)
        
        scroll = ScrollView(size_hint=(None, None), size=(800, 400), pos=(100,50))
        scroll.add_widget(layout)
        
        self.add_widget(scroll)
        
        f.close()
     
    def back(self):
        self.game.cacherEcranCredit(None)
        self.game.showEcranAccueil()
        
        
class EcranPause(Widget):
    game = ObjectProperty(None)
    
    def build(self, p_oGame):
        self.game = p_oGame
     
    def run(self):
        self.game.cacherEcranPause(None)
        self.game.run()
        
    def quit(self):
        self.game.cacherEcranPause(None)
        self.game.gestionSon.stopMusic()
        self.game.showEcranAccueil()
        
class EcranNiveauName(Widget):
    game = ObjectProperty(None)
    niveauLbl = ObjectProperty(None)
    
    def build(self, p_oGame):
        self.game = p_oGame
        self.niveauLbl.text = 'Niveau ' + str(self.game.niveauNbr)
        Clock.schedule_once(self.game.cacherEcranNiveauName, 2)
     

Factory.register("SpaceBackground", SpaceBackground)
Factory.register("SpaceForeground", SpaceForeground)
Factory.register("SpaceGame", SpaceGame)
Factory.register("SpaceScreen", SpaceScreen)
Factory.register("TableauScreen", TableauScreen)
Factory.register("Game", Game)    
Factory.register("LaserButton", LaserButton) 
Factory.register("FormationButton", FormationButton)   
Factory.register("Scan", Scan) 

        
class EscadronT42App(App):
    title = 'Escadron T-42'
    icon = 'escadront42.png'
    
    def build_config(self, config):
        Config.set('graphics', 'show_cursor', 1)
        Config.set('graphics', 'fullscreen', '0')
        Config.set('graphics', 'width', 1024)
        Config.set('graphics', 'height', 600)
        # Config.set('graphics', 'show_cursor', 0)
        # Config.set('graphics', 'fullscreen', '1')
        # Config.set('graphics', 'width', 1920)
        # Config.set('graphics', 'height', 1080)
        Config.write()
    
    def build(self):
        self.game = Game()  
        self.game.build(self)
        
        self.game.showEcranAccueil()
                
        return self.game
        
    def quitGame(self): 
        self.stop()
    
        

if __name__ in ('__main__', '__android__'):
    EscadronT42App().run()

