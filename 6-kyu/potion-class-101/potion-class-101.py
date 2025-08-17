import math
class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
        self.r = self.color[0]
        self.g = self.color[1]
        self.b = self.color[2]
    
    def mix(self, other):
        volume_sum = self.volume + other.volume
        red = math.ceil((self.r * self.volume + other.r * other.volume) / volume_sum)
        green = math.ceil((self.g * self.volume + other.g * other.volume) / volume_sum)
        blue = math.ceil((self.b * self.volume + other.b * other.volume) / volume_sum)
        return Potion((red, green, blue), volume_sum)