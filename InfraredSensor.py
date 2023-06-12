"""A Program to detect white and black surfaces
    using the Infrared Sensor KY-033"""
#Import the GPIO library from the RPi module
import RPi.GPIO as io
#Import sleep from the time module
from time import sleep

#Define a class to instantiate a KY-033 Sensor Object
class TrackSensor:
    #Constructor Method
    def __init__(self,pin):
        io.setmode(io.BCM)
        """Initialize the attribute TrackPin with the GPIO Pin
            connected to the Signal(S) Pin on the KY-033 Sensor"""
        self.__TrackPin = pin
        #Set up the TrackPin to be an input pin
        io.setup(self.__TrackPin,io.IN,pull_up_down = io.PUD_UP)
   
    #Method to detect reflected infrared
    def Detect(self):
        #Detect whether the TrackPin is high or low
        if io.input(self.__TrackPin) == io.LOW: #Infrared reflection is detected
            return False #Indicates White Color
        else:
            return True #Indicates Black Color
