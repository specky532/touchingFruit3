#!/usr/bin/env python

import pygame
import RPi.GPIO as GPIO
import mpr121 #References all headings and connections for the mpr121

# Use GPIO Interrupt Pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else
mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

# User pygame for sounds
pygame.mixer.pre_init(44100, -16, 12, 512) #(Frequency, size, channels, buffer)
pygame.init()

#Define Sounds for Drum Kit
drumKit = []

drumKit0 = pygame.mixer.Sound('samples/drumKit/d0.wav') #Blank Sound
drumKit1 = pygame.mixer.Sound('samples/drumKit/d1.wav')
drumKit2 = pygame.mixer.Sound('samples/drumKit/d2.wav')
drumKit3 = pygame.mixer.Sound('samples/drumKit/d3.wav')
drumKit4 = pygame.mixer.Sound('samples/drumKit/d4.wav')
drumKit5 = pygame.mixer.Sound('samples/drumKit/d5.wav')
drumKit6 = pygame.mixer.Sound('samples/drumKit/d6.wav')
drumKit7 = pygame.mixer.Sound('samples/drumKit/d7.wav')

#Add sounds to list
drumKit.append(drumKit0)
drumKit.append(drumKit1)
drumKit.append(drumKit2)
drumKit.append(drumKit3)
drumKit.append(drumKit4)
drumKit.append(drumKit5)
drumKit.append(drumKit6)
drumKit.append(drumKit7)

for sample in drumKit:
    sample.set_volume(.65)


#Define Sounds for piano
piano = []

piano0 = pygame.mixer.Sound('samples/piano/p0.wav') #Blank wav file (Used to switch sample pack)
piano1 = pygame.mixer.Sound('samples/piano/p1.wav')
piano2 = pygame.mixer.Sound('samples/piano/p2.wav')
piano3 = pygame.mixer.Sound('samples/piano/p3.wav')
piano4 = pygame.mixer.Sound('samples/piano/p4.wav')
piano5 = pygame.mixer.Sound('samples/piano/p5.wav')
piano6 = pygame.mixer.Sound('samples/piano/p6.wav')
piano7 = pygame.mixer.Sound('samples/piano/p7.wav')

#Add sounds to list
piano.append(piano0)
piano.append(piano1)
piano.append(piano2)
piano.append(piano3)
piano.append(piano4)
piano.append(piano5)
piano.append(piano6)
piano.append(piano7)


for sample in piano:
    sample.set_volume(.65)

#Define Sounds for Madeon Samples
madeon = []

madeon0 = pygame.mixer.Sound('samples/madeon/m0.wav')
madeon1 = pygame.mixer.Sound('samples/madeon/m1.wav')
madeon2 = pygame.mixer.Sound('samples/madeon/m2.wav')
madeon3 = pygame.mixer.Sound('samples/madeon/m3.wav')
madeon4 = pygame.mixer.Sound('samples/madeon/m4.wav')
madeon5 = pygame.mixer.Sound('samples/madeon/m5.wav')
madeon6 = pygame.mixer.Sound('samples/madeon/m6.wav')
madeon7 = pygame.mixer.Sound('samples/madeon/m7.wav')

#Add sounds to list
madeon.append(madeon0)
madeon.append(madeon1)
madeon.append(madeon2)
madeon.append(madeon3)
madeon.append(madeon4)
madeon.append(madeon5)
madeon.append(madeon6)
madeon.append(madeon7)

for sample in madeon:
    sample.set_volume(.65)

madeonMode = 2

madeonMode = int(raw_input("Do you want to run in Madeon Mode? 1 = Yes, 0 = No"))

while madeonMode != 0 and madeonMode != 1: #Checks user has given correct input
        print "Please enter a 1 or 0"
        madeonMode = int(raw_input("Do you want to run in Madeon Mode? 1 = Yes, 0 = No"   ))

if madeonMode == 1:
    print "Madeon Mode Selected"
else:
    print "Normal Mode Selected"

# Track touches
touches = [0,0,0,0,0,0,0,0];
interrupted = False

#Run main loop
while interrupted == False:
        try:
                #Detect input
                if (GPIO.input(7)): # Interupt pin is high
                        pass
                else: # Interupt pin is low
                        touchData = mpr121.readData(0x5a) #Take data from SDA Line
                        for i in range(8): #Checks each touch value
                                if (touchData & (1<<i)):
                                        if (touches[i] == 0):
                                                print( 'Pin ' + str(i) + ' was just touched') #Track changes and give feedback to user
						if madeonMode == 0:
							if touches[0] == 1: #Check if sample switch is being touched, if so play from piano samples
								piano[i].play()
								print 'Piano Mode'
							else:
								drumKit[i].play()
								print 'Drum Mode'
						else:
							madeon[i].play()
						touches[i] = 1;
                                else:
                                        if (touches[i] == 1): #Check if pin has been released
                                                print( 'Pin ' + str(i) + ' was just released')
                                        touches[i] = 0;
	except KeyboardInterrupt: #Allows program to be stopped
                print
        	print "Thank you for using Touching Fruit!!!"
        	print
        	print "Please run touchingFruit.py to start again."
		interrupted = True
