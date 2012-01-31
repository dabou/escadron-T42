'''
   niveau.py is part of Escadron-T42.
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

from random import randint
from math import log, trunc
from kivy.core.window import Window

class NiveauAction:
    def __init__(self):
        self.id = 1
        self.time = 0
        self.type = 'nothing'
        self.object = None
        self.size = 0, 0
        self.position = 0,0
        self.movement = 0,0,0
        self.isDeco = True
        self.isBack = True
        
        
class Niveau:
  
    def __init__(self, difficulty):
        self.name = 'niveau 0'
        self.image = None
        self.music = None
        self.id = '0'
        self.typeOfNiveau = 'space'
        self.difficulty = difficulty
        self.actions = {}
   
    def load(self):
        pass
        
    def generate(self):
        pass
    
        
class NiveauGenerated(Niveau):
    def load(self):
        self.setImage()
        self.setMusic()
                
    def setImage(self):
        i = randint(0, 20)
        if i == 0:
            self.image = 'images/eso0915a.jpg'
        elif i == 1:
            self.image = 'images/eso0515c.jpg'
        elif i == 2:
            self.image = 'images/eso0526b.jpg'
        elif i == 3:
            self.image = 'images/eso0629a.jpg'
        elif i == 4:
            self.image = 'images/eso0638a.jpg'
        elif i == 5:
            self.image = 'images/eso0718a.jpg'
        elif i == 6:
            self.image = 'images/eso0722b.jpg'
        elif i == 7:
            self.image = 'images/eso0828a.jpg'
        elif i == 8:
            self.image = 'images/eso0917a.jpg'
        elif i == 9:
            self.image = 'images/eso0927a.jpg'
        elif i == 10:
            self.image = 'images/eso0939a.jpg'
        elif i == 11:
            self.image = 'images/eso0942a.jpg'
        elif i == 12:
            self.image = 'images/eso0946a.jpg'
        elif i == 13:
            self.image = 'images/eso1004a.jpg'
        elif i == 14:
            self.image = 'images/eso1015a.jpg'
        elif i == 15:
            self.image = 'images/eso1024b.jpg'
        elif i == 16:
            self.image = 'images/eso1049a.jpg'
        elif i == 17:
            self.image = 'images/eso1122a.jpg'
        elif i == 18:
            self.image = 'images/eso1134d.jpg'
        elif i == 19:
            self.image = 'images/eso1138a.jpg'
        else :
            self.image = 'images/eso0915a.jpg'
           
        if self.typeOfNiveau == 'nuage':
             self.image = 'images/eso1138a.jpg'
        elif self.typeOfNiveau == 'asteroid':
             self.image = 'images/eso1015a.jpg'
            
        
    def setMusic(self):
        i = randint(0, 11)
        if i == 0:
            self.music = '01-Adam CASTILLO-Thermonuclear Reaction.ogg'
        elif i == 1:
            self.music = '02-Adam CASTILLO-Here Is The Earth.ogg'
        elif i == 2:
            self.music = '03-Adam CASTILLO-Landing Part 1.ogg'
        elif i == 3:
            self.music = '04-Adam CASTILLO-Landing Part 2.ogg'
        elif i == 4:
            self.music = '05-Adam CASTILLO-Massacre Part 1.ogg'
        elif i == 5:
            self.music = '06-Adam CASTILLO-Massacre Part 2.ogg'
        elif i == 6:
            self.music = '07-Adam CASTILLO-Bone Spirit Part 1.ogg'
        elif i == 7:
            self.music = '08-Adam CASTILLO-Bone Spirit Part 2.ogg'
        elif i == 8:
            self.music = '09-Adam CASTILLO-The Nabis Project.ogg'
        elif i == 9:
            self.music = '10-Adam CASTILLO-Agony Part 1.ogg'
        elif i == 10:
            self.music = '11-Adam CASTILLO-Agony Part 2.ogg'
        elif i == 11:
            self.music = '12-Adam CASTILLO-Born To Die.ogg'
        else :
            self.music = '03-Adam CASTILLO-Landing Part 1.ogg'
        
    def setId(self, id):
        self.id = id
        
    def generate(self):
    
        self.typeOfNiveau = 'space'
        
        i = randint(0, 10)
        if i < 2 :
            self.typeOfNiveau = 'asteroid'
            
        elif i > 7 :
            self.typeOfNiveau = 'nuage'
    
        time = 0
        
        index = 0;
        
        if self.typeOfNiveau == 'asteroid' or self.typeOfNiveau == 'space':
        
            for i in range(10):
                index += 1
                
                act = NiveauAction()
                act.id = index
                act.time = time
                act.type = 'create'
                act.isDeco = True
                     
                act.position = randint(10,Window.width - 20), randint(100,Window.height - 50)
                
                act.object = 'AsteroidDeco'       
              
                size = randint(30, 70)
                act.size = size, size
                act.movement = randint(-50, -10),randint(-10, 10),randint(-90, 90)
                    
                self.actions[index] = act
                
        whatmin = trunc(0 + time/4 * self.difficulty )      
        whatmax = trunc(200*log(10*self.difficulty) - 50)
        
        for i in range(70 + (10 * self.difficulty)):
                        
            index += 1
            
            act = NiveauAction()
            act.id = index
            act.time = time
            act.type = 'create'
                 
            act.position = Window.width + 50,randint(100,Window.height - 50)
            
            whatmin = trunc(0 + (time/2) * self.difficulty    )   
            whatmax = trunc(200*log(10*self.difficulty) - 50)
            
            whatDifficult = randint(whatmin, whatmax)
            
            if whatDifficult <= 400:
                act.isDeco = False
                act.object = 'Asteroid'         
           
                size = randint(50, 100)
                act.size = size, size
                act.movement = randint(-100, -30),randint(-30, 30),randint(-180, 180)
                
            elif whatDifficult > 400 and whatDifficult <= 600:
                act.isDeco = False
                act.object = 'SpaceShipVx32'         
           
                act.size = 32, 32
             
            elif whatDifficult > 600 and whatDifficult <= 700:
                act.isDeco = False
                act.object = 'SpaceShipVx56'         
           
                act.size = 32, 32
             
            elif whatDifficult > 700 and whatDifficult <= 800:
                act.isDeco = False
                act.object = 'SpaceShipT34'         
           
                act.size = 32, 32
             
            elif whatDifficult > 800 :
                act.isDeco = False
                act.object = 'SpaceShipT48'         
           
                act.size = 64, 64
             
            self.actions[index] = act
            
            deco = randint(0, 10)
            if deco < 3 :
                index += 1
                
                act.id = index
                act.time = time
                act.type = 'create'
                act.isDeco = True
                     
                act.position = Window.width + 50,randint(100,Window.height - 50)
                
                act.object = 'AsteroidDeco'       
                size = randint(30, 70)
                act.size = size, size
                act.movement = randint(-50, -10),randint(-10, 10),randint(-180, 180)
                
                self.actions[index] = act
            
            #time += randint(50, 100) /100
            time += randint(1, 3) /10.0
            
         
               
        act = NiveauAction()
        act.id = index + 1
        act.time = time
        act.type = 'create'
             
        act.position = Window.width + 50, Window.height /2 + 100
        act.isDeco = False
        act.object = 'ItemTux'         
        act.size = 64, 64      
 
        #act = NiveauAction()
        #act.id = i+1
        #act.time = time
        #act.type = 'end'
        
        self.actions[act.id] = act
            
            
        