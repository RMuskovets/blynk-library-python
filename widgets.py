# The MIT License (MIT)
#
# Copyright (c) 2018 Kenny Hora
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Controls the LCD Widget in the Blynk App
class WidgetLCD():
    # Constructor
    # Constructor for the Blynk LCD Widget
    # Parameters:
    #     blynk - Blynk object
    #     vPin  - The Virtual pin the LCD is connected to
    def __init__(self, blynk, vPin):
        self.__blynk = blynk
        self.__vPin = vPin

    # clear()
    # Clears the LCD widget
    # Parameters: None
    def clear(self):
        self.__blynk.virtual_write(self.__vPin, 'clr')

    # write(x, y, s)
    # Prints a message to the LCD
    # Parameters:
    #     x - x-position of the lcd cursor | range [0, 15]
    #     y - y-position of the lcd cursor | range [0, 1]
    #     s - messages to print to the LCD
    def write(self, x, y, s):
        self.__blynk.virtual_write(self.__vPin, '\0'.join(map(str, ('p', x, y, s))))

class WidgetImage():
    # Constructor for the Blynk Image Widget
    # Parameters:
    #     blynk - Blynk object
    #     vPin - the virtual pin the image is connected to
    def __init__(self, blynk, vPin):
        self.__blynk = blynk
        self.__vPin = vPin
    
    # setImages(imgs)
    # Sets the images of the widget
    # Parameters:
    #     imgs - List of images' urls
    def setImages(self, imgs):
        self.__blynk.set_property(self.__vPin, "urls", *imgs)
    
    # setImage(img, index)
    # Sets the image with given index
    # Parameters:
    #     img - The URL of image replacing with
    #     index - The image's index
    def setImage(self, img, index):
        self.__blynk.set_property(self.__vPin, "url", index, img)
    
    # setOpacity(percent)
    # Sets the opacity of all image gallery
    # Parameters:
    #     percent - The % of opacity
    def setOpacity(self, percent):
        self.__blynk.set_property(self.__vPin, "opacity", percent)
    
    # setScale(percent):
    # Sets the scale of image gallery
    # Parameters:
    #     percent - The % of scale
    def setScale(self, percent):
        self.__blynk.set_property(self.__vPin, "scale", percent)
    
    # setRotation(deg)
    # Sets the rotation of gallery (in degrees)
    # Parameters:
    #     deg - The degrees to rotate
    def setRotation(deg):
        self.__blynk.set_property(self.__vPin, "rotation", deg)
    
    # setIndexingStart(i)
    # Sets the start number of indexes (see setImage)
    # Parameters:
    #     i - The start index
    def setIndexingStart(i):
        self.__blynk.virtual_write(self.__vPin, i)

class WidgetTable():
    
    # Constructor of the Table widget
    # Parameters:
    #     blynk - The Blynk object
    #     vPin - The virtual pin the table is assigned to
    def __init__(self, blynk, vPin):
        self.__blynk = blynk
        self.__vPin = vPin
    
    # addRow(id, name, val)
    # Adds a row to the table
    # Parameters:
    #     id - The row's ID
    #     name - The row's name
    #     val - The row's value
    def addRow(self, id, name, val):
        self.__blynk.virtual_write(self.__vPin, "add", id, name, val)
    
    # updRow(id, name, val)
    # Updates the row with given ID
    # Parameters:
    #     id - The row's ID
    #     name - The row's name
    #     val - The row's value
    def updRow(self, id, name, val):
        self.__blynk.virtual_write(self.__vPin, "update", id, name, val)
    
    # pickRow(id)
    # Picks the row
    # Parameters:
    #     id - The row's ID
    def pickRow(self, id):
        self.__blynk.virtual_write(self.__vPin, "pick", id)
    
    # clear()
    # Clears the table
    def clear(self):
        self.__blynk.virtual_write(self.__vPin, "clr")
    
    # selectRow(id)
    # Selects the row
    # Parameters:
    #     id - The row's ID
    def selectRow(self, id):
        self.__blynk.virtual_write(self.__vPin, "select", id)
    
    # deselectRow(id)
    # Deselects the row
    # Parameters:
    #     id - The row's ID
    def deselectRow(self, id):
        self.__blynk.virtual_write(self.__vPin, "deselect", id)
