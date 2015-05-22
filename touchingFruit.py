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


drumKit1 = pygame.mixer.Sound('samples/drumKit/d1.wav')
drumKit2 = pygame.mixer.Sound('samples/drumKit/d2.wav')
drumKit3 = pygame.mixer.Sound('samples/drumKit/d3.wav')
drumKit4 = pygame.mixer.Sound('samples/drumKit/d4.wav')
drumKit5 = pygame.mixer.Sound('samples/drumKit/d5.wav')
drumKit6 = pygame.mixer.Sound('samples/drumKit/d6.wav')
drumKit7 = pygame.mixer.Sound('samples/drumKit/d7.wav')
drumKit8 = pygame.mixer.Sound('samples/drumKit/d8.wav')
drumKit9 = pygame.mixer.Sound('samples/drumKit/d9.wav')


drumKit.append(drumKit1)
drumKit.append(drumKit1)
drumKit.append(drumKit2)
drumKit.append(drumKit3)
drumKit.append(drumKit4)
drumKit.append(drumKit5)
drumKit.append(drumKit6)
drumKit.append(drumKit7)
drumKit.append(drumKit8)
drumKit.append(drumKit9)

for sample in drumKit:
    sample.set_volume(.65)


#Define Sounds for piano
piano = []

piano1 = pygame.mixer.Sound('samples/piano/p1.wav')
piano2 = pygame.mixer.Sound('samples/piano/p2.wav')
piano3 = pygame.mixer.Sound('samples/piano/p3.wav')
piano4 = pygame.mixer.Sound('samples/piano/p4.wav')
piano5 = pygame.mixer.Sound('samples/piano/p5.wav')
piano6 = pygame.mixer.Sound('samples/piano/p6.wav')
piano7 = pygame.mixer.Sound('samples/piano/p7.wav')
piano8 = pygame.mixer.Sound('samples/piano/p8.wav')
piano9 = pygame.mixer.Sound('samples/piano/p9.wav')


piano.append(piano1)
piano.append(piano1)
piano.append(piano2)
piano.append(piano3)
piano.append(piano4)
piano.append(piano5)
piano.append(piano6)
piano.append(piano7)
piano.append(piano8)
piano.append(piano9)


for sample in piano:
    sample.set_volume(.65)

# Track touches
touches = [0,0,0,0,0,0,0,0,0,0];
interrupted = False

#Run main loop
while interrupted == False:
        try:
        #Detect input
                if (GPIO.input(7)): # Interupt pin is high
                        pass
                else: # Interupt pin is low
                        touchData = mpr121.readData(0x5a) #Take data from SDA Line
                        for i in range(10): #Checks each touch value
                                if (touchData & (1<<i)):
                                        
                                        if (touches[i] == 0):
                                                print( 'Pin ' + str(i) + ' was just touched') #Track changes, can be commented out
                                                if touches[0] == 1:
                                                    piano[i].play()
                                                    print('Piano Mode')
                                                else:
                                                    drumKit[i].play()	
                                        touches[i] = 1;
                                else:
                                        if (touches[i] == 1):
                                                print( 'Pin ' + str(i) + ' was just released')
                                        touches[i] = 0;
	except KeyboardInterrupt:
        	print "Thank you for using Touching Fruit!!!"
		interrupted = True




