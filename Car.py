#A Program to control Mobile Platform with four DC Motors
from time import sleep
import math
#import the DC Motor Module from the MotorModule Library
from MotorModule import DCMotor
#import keyboard module from the pynput library
from pynput import keyboard
#Import thread module from the threading library
from threading import Thread
#Import Event module from the threading Library Module
from threading import Event
#Import class TrackSensor from InfraredSensor Module
from InfraredSensor import TrackSensor

#Class of Autonomous Vehicle
class AutoVehicle:
    #Constructor Vehicle
    def __init__(self,title):
        self.__Title = title
        #Both Left Motors connected togther to M3
        #Both Right Motors connected togther to M4
        self.__MotorsLeft = 0 #Attribute to create DCMotor object representing left motors
        self.__MotorsRight = 0 #Attribute to create DCMotor object representing right motors
        self.__trackLeftSensor = 0 #Attribute to create Left TrackSensor Object
        self.__trackRightSensor = 0 #Atrribute to create Right TrackSensor Object
        self.__driveForward = 0 #Thread Attribute to create a thread to drive forward
       
        """Using the Attribute self.__MotorsLeft, instantiate
            a DC Motor object: Both left motors are connected to M3"""
        self.__MotorsLeft = DCMotor(3,'Left Motors')
       
        """Using the Attribute self.__MotorsRight, instantiate
            a DC Motor object: Both Right motors are connected to M4"""
        self.__MotorsRight = DCMotor(4,'Right Motors')
       
        """Using the Attribute self.__trackLeftSensor instaniate
            a TrackSensor object connected to GPIO 21"""
        self.__trackLeftSensor = TrackSensor(21)
       
        """Using the Attribute self.__trackLeftSensor instaniate
            a TrackSensor object connected to GPIO 17"""
        self.__trackRightSensor = TrackSensor(17)
       
        """Using the Attribute self.__DriveForward instaniate
            a thread object executing the method OnDrive. Do not
            start the thread"""
        self.__DriveForward = Thread(target = self.OnDrive)
       
        self.__VehicleSpeed = 0.6 #Initial Speed
        self.__FORWARD = False #Set to True when the drive thread is started
   
           
    #Method to drive the vehicle in Forward Direction at set Speed
    def OnDrive(self):
        print('Driving Forward')
        """Write code to drive the platform forward
            using the motor objects, the initial vehicle speed,
            and in the forward direction"""
        self.__MotorsLeft.Speed = self.__VehSpeed
        self.__MotorsRight.Speed = self.__VehSpeed

        """Write code to set the direction Forward (True) of both left and right
            motors using the property rotation of the DCMotor Object"""
        self.__MotorsLeft.rotation(True)
        self.__MotorsRight.rotation(True)
       
        while self.__FORWARD:
            """Write code (if and else statements to determine
                if any of the IR sensors is crossing the track
                and perform suitable steering. Also, write print statements
                to indicate which side of the sensor detetced the track"""
           
            detectLeft = self.__trackLeftSensor.Detect() # call detect method on left sensor object
            detectRight = self.__trackRightSensor.Detect() # call detect method on Right sensor object
            if detectLeft:
                # detectLeft equals true because Detect returned True, sensor is picking up a black color
                # this means it is going off the track to the right
                print('Left sensor detecting track')
                self.SteerLeft()
               
            elif detectRight:
                # detectRight equals true because Detect returned True, sensor is picking up a black color
                # this means it is going off the track to the left
                print('Right sensor detecting track')
                self.SteerRight()
               
            else:
                # detectLeft equals False because Detect returned False, sensor is picking up a white color
                # this means it is on track
                print('Track not detected')
           
            sleep(0.1)
                         
    #Method to Steer Right
    def SteerRight(self):
        #Write code to steer the platform right
        if self.__MotorsRight.Speed <= 1.0:
            #Write code to set the speed of the left and right motors
            self.__MotorsLeft.Speed = 0.5
            self.__MotorsRight.Speed = 0.5
            #Write code to set the left motors direction to reverse (False)
            self.__MotorsLeft.rotation(False)
            #Write code to set the right motors direction to forward (True)
            self.__MotorsRight.rotation(True)
    #Method to Steer Left
    def SteerLeft(self):
        #Write code to steer the platform left similar to SteerRight
        #Write code to set the speed of the left and right motors
            self.__MotorsLeft.Speed = 0.5
            self.__MotorsRight.Speed = 0.5
            #Write code to set the left motors direction to forward (True)
            self.__MotorsLeft.rotation(True)
            #Write code to set the right motors direction to reverse (False)
            self.__MotorsRight.rotation(False)
       
    #Method to stop the vehicle  
    def StopVehicle(self):
        if self.__FORWARD:
            self.__FORWARD = not self.__FORWARD
            self.__driveForward.join()

        self.__MotorsLeft.Stop()
        self.__MotorsRight.Stop()
    '''
    #Method to create the Drive Forward Thread object with the DriveForward Method
    def DriveForward(self):
        #Set the Attribute self.__FORWARD to True
        self.__FORWARD = True
        #Start the thread using the attribute self.__driveForward
        ...

   '''
    #A Method to respond to the keyboard event
    def Control(self,key):
        if key.char == 'd' or key.char == 'D': #Key d or D
            #Method to drive forward
            self.DriveForward()
        if key.char == 's' or key.char == 'S': #Key s or S
            if self.__FORWARD:
                #Method to Stop the vehicle
                self.StopVehicle()
                print('Autonomous Vehicle - Turned Off')
                return False
            else:
                print('Autonomous Vehicle - Not Started')
                return False
                               
if __name__ == '__main__':
    tesla = AutoVehicle('Tesla') #Instantiate a Vehicle Object
    try:
        print('Press d to Drive and s to Stop')
        listener = keyboard.Listener(on_press = tesla.Control)
        listener.start()
        listener.join()
        print('Exiting')
       
    except KeyboardInterrupt:
        tesla.StopVehicle()
        print('Exiting')
