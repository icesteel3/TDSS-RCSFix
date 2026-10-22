  #why the fuck is you are use hashtag for comments
import getpixelcolor
import mouse
import time
import pydirectinput
#my variables yayayayayayay
correctRgbValue = (43, 235, 0)
x = 980
y = 215

#print(x)
#me being stupid and trying to remember syntax for python lollolol


mouse.click('left')
breakout = False
loopCounter = 0
while breakout == False:
    
    #gets the color of the pixel at the point of the ready button, then prints it out (debug)
    rgbValue = getpixelcolor.pixel(x, y)
    print(rgbValue)
    
    #if statement here checking if the RGB value on screen matches the RGB value of the ready button
    if rgbValue == correctRgbValue:
        print ("true")
        #testpos = mouse.get_position()
        #print(testpos)
        #roblox why aare you not treating the cursor like its over the right place even tho it is why why why whyhw hhwyhwhwhhwyhwhwhw i hate u roblox whyhwyhywhww
        mouse.click('left')
        #mouse.move(x, y, absolute=True, duration=0.0)
        mouse.click('left')
        time.sleep(5.6)
        pydirectinput.moveTo(x, y)
        
        #mouse.move(x+40, y+70, absolute=True, duration=0.2)
        time.sleep(0.1)
        pydirectinput.moveTo(x, y)
        mouse.click('left')
        mouse.click('left')
        #mouse.move(x, y, absolute=True, duration=0.2)
        mouse.click('left')
        breakout = True
    else:
        loopCounter+=1
        print ("false")
        print (loopCounter)
        time.sleep(0.05)
    if loopCounter >= 100:
        break
        #second condition to end the loop (basically a timer for 5 seconds)
        
        #also no ai used so yay i guess