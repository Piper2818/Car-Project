#A Program to control DC Motor using Object-Oriented Programming
#Demonstrate use of Motor HAT from Adafruit
#import board module to access I2C interface
import board
#import MotorKit library from the Adafruit MotorKit Module
from adafruit_motorkit import MotorKit
from time import sleep

#Define a class to simulate a DC Motor
class DCMotor:
    #Instantiate the MotorKit Object as a static attribute
    __motorKit = MotorKit(i2c = board.I2C())
    def __init__(self,MotorId,Location):
        self.__motor = 0
        self.__Position = Location
        self.__Id = MotorId
        self.__speed = 0.0
        self.__Forward = True
       
        if(self.__Id == 1):
            self.__motor = DCMotor.__motorKit.motor1
        if(self.__Id == 2):
            self.__motor = DCMotor.__motorKit.motor2
        if(self.__Id == 3):
            self.__motor = DCMotor.__motorKit.motor3
        if(self.__Id == 4):
            self.__motor = DCMotor.__motorKit.motor4
   
    #A get Property Method to read the Motor Position
    @property
    def Position(self):
        return self.__Position
           
    #A get Property Method to read the current motor speed
    @property
    def Speed(self):
        return self.__speed
   
    #A set Property method to set a desired motor speed
    @Speed.setter
    def Speed(self,value):
        self.__speed = value
        self.__motor.throttle = self.__speed
       
    #A get Property Method to read the current motor rotation direction
    @property
    def rotation(self):
        return self.__Forward
   
    #A set Property method to set the desired direction
    @rotation.setter
    def rotation(self,value):
        if value == True:
            self.__motor.throttle = self.__speed
            self.__Forward = True
        else:
            self.__motor.throttle = -self.__speed
            self.__Forward = False
   
    #A Method to stop the motor
    def Stop(self):
        print('Stopping Motor: ',self.__Position)
        self.__motor.throttle = 0
        sleep(0.1)
