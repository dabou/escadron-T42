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
        
        
        
        
        
        