import random


class MObject:
    def __init__(self):
        pass


class Image:
    def __init__(self, w, h, texture):
        print("Constructor called")
        self.m_width = w
        self.m_height = h
        self.m_colorChannels = 3  # Assume we support RGB channels only.
        self.m_Pixels = [random.randint(0, 255) for _ in range(w * h * self.m_colorChannels)]
        self.texture = texture

    """
    def __del__(self):
        # https://docs.python.org/3/reference/datamodel.html#object.__del__
    """

    def getWidth(self):
        return self.m_width

    def getHeight(self):
        return self.m_height
    
    def get_texture(self):
        return self.texture

    def getPixelColorR(self, x, y):
        return self.m_Pixels[self.m_width * self.m_colorChannels * y + x]

    def getPixels(self):
        return self.m_Pixels

    def setPixelsToRandomValue(self):
        value = random.randint(0, 255)
        # Set the entire list to one color in one function call
        self.m_Pixels = [value] * (self.m_width * self.m_height * self.m_colorChannels)


class Texture():
    def __init__(self, texture):
        self.texture = texture
    
    def get_it(self):
        return self.texture


def main():
    random.seed()

    # texture object
    texture1 = Texture('smooth')
    texture2 = Texture('rough')

    # Create a first image
    image1 = Image(100, 200, texture1)
    # Create a second image
    image2 = Image(image1.getWidth(), image1.getHeight(), texture2)

    print(f"image1: {image1.getWidth()}, {image1.getHeight()}")
    print(f"image1 red color at (0, 0): {image1.getPixelColorR(0, 0)}")
    print(f"image2: {image2.getWidth()}, {image2.getHeight()}")
    print(f"image2 red color at (0, 0): {image2.getPixelColorR(0, 0)}")

    print(image1.get_texture().get_it())
    print(image2.get_texture().get_it())

if __name__ == "__main__":
    main()
