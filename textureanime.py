'''
   textureanime.py is part of Escadron-T42.
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

from kivy.clock import Clock 

class TextureAnime:

    def __init__(self, texture, delay = 0.05, loop = True, spriteSizeX = 64, spriteSizeY = 64):
        self.textureIndex = 1
        self.last = Clock.get_boottime()
        self.delay = delay
        self.loop = loop
        self.loopCount = 0
                
        self.textures = {}
        
        nbrSpriteL = texture.width / spriteSizeX
        nbrSpriteH = texture.height / spriteSizeY
        
        index = 1
                        
        for i in range(nbrSpriteH):
            for j in range(nbrSpriteL):
                x = spriteSizeX*(j)
                y = texture.height - (spriteSizeY*(i+1))
                self.textures[index] = texture.get_region(x, y, spriteSizeX, spriteSizeY)
                
                index += 1
        
    def first(self):
        self.textureIndex = 1
        return self.textures[self.textureIndex]
        
    def next(self):
        retourTexture = None
        if self.loop:
            oldIndex = self.textureIndex
            self.textureIndex = (self.textureIndex) % len(self.textures) + 1
            retourTexture = self.textures[self.textureIndex]
            if self.textureIndex < oldIndex:
                self.loopCount += 1
        elif self.textureIndex < len(self.textures):
            self.textureIndex = self.textureIndex + 1
            retourTexture = self.textures[self.textureIndex]
            
        return retourTexture
        
    def getAt(self):
        retourTexture = None
        bootTime = Clock.get_boottime()
        if bootTime - self.last >=  self.delay:
            self.last = bootTime
            retourTexture =  self.next()
        
        return retourTexture
        
    def getLoopCount(self):
        return self.loopCount
        
        
        
        
        
        