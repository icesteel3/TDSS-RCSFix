  #why the is you are use hashtag for comments in python lol
import getpixelcolor
import mouse
import time
import pydirectinput
import tkinter as tk
#my variables yayayayayayay
correctRgbValue = (43, 235, 0)
x = 980
y = 215



def checkForReady():
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
    
#print(x)
#me being stupid and trying to remember syntax for python lollolol

#Stuff to make window, and formatting for that
root = tk.Tk()
#setup
root.title("RCS fix")
root.minsize(400,300)
root.resizable(False, False)


#on window elements and stuff
label = tk.Label(root, text="placeholder", anchor="center").grid(row=0, column=1)
#set coordinate related stuff
checkLabel = tk.Label(root, text="Set Coordinates", anchor="center").grid(row = 1, column = 0, padx=10, pady=10)
checkButton = tk.Button(root, text="Pick", anchor = "e").grid(row = 2, column = 0)
#delay related
delayLabel = tk.Label(root, text="Delay", anchor="center").grid(row = 1, column = 2)
defaultRadio = tk.Radiobutton(root, text="Default").grid(row = 2, column = 2)

start = tk.Button(root, text="start", command=checkForReady).grid(row = 3, column = 1)

root.mainloop()



        
        #also no ai used so yay i guess
        