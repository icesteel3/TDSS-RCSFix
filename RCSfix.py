  #why the is you are use hashtag for comments in python lol
import getpixelcolor
import time
import pydirectinput
import tkinter as tk
from pynput import mouse
#my variables yayayayayayay
correctRgbValue = (43, 235, 0)
xpos = 980
ypos = 215
defaultDelayTime = 5.6
delayTime = 5.6

#ima be honest i imported this thing from the documenation and just did stuff til it worked still dont really get what it does lmao
def on_click(localx, localy, button, pressed):
    global xpos
    global ypos
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (localx, localy)))
    if pressed:
        xpos = localx
        ypos = localy
        # Stop listener
        return False
def setClickPos():

    listener=mouse.Listener(
        on_click=on_click)
    listener.start()
    listener.join()
    listener.stop()
    print(xpos)
    print(ypos)
    
    
    coordinateLabel.config(text='Coordinates: ({0}, {1})'.format(xpos, ypos))
def confirm():
    try:
        delayTime = delayVar.get()
    except tk.TclError:
        delayEntry.delete(0, tk.END)
        delayEntry.insert(0, "Only accepts numbers")
        
        
def defaultSelect():
    delayTime = defaultDelayTime
    delayEntry.grid_forget()
    delayConfirmButton.grid_forget()
def customSelect():
    delayEntry.grid(row = 4, column = 2)
    delayConfirmButton.grid(row = 5, column = 2)
    
def checkForReady():
    breakout = False
    loopCounter = 0
    while breakout == False:
        
        #gets the color of the pixel at the point of the ready button, then prints it out (debug)
        rgbValue = getpixelcolor.pixel(xpos, ypos)
        print(rgbValue)
        
        #if statement here checking if the RGB value on screen matches the RGB value of the ready button
        if rgbValue == correctRgbValue:
            print ("true")
            #testpos = mouse.get_position()
            #print(testpos)
            #roblox why aare you not treating the cursor like its over the right place even tho it is why why why whyhw hhwyhwhwhhwyhwhwhw i hate u roblox whyhwyhywhww
            pydirectinput.click()
            #mouse.move(x, y, absolute=True, duration=0.0)
            pydirectinput.click()
            time.sleep(delayTime - 0.1)
            pydirectinput.moveTo(xpos, ypos)
            
            #mouse.move(x+40, y+70, absolute=True, duration=0.2)
            time.sleep(0.1)
            pydirectinput.moveTo(xpos, ypos)
            pydirectinput.click()
            pydirectinput.click()
            #mouse.move(x, y, absolute=True, duration=0.2)
            pydirectinput.click()
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
#radiobutton group (needs to be here, apparently)
delayGroup_var = tk.StringVar()
delayVar = tk.DoubleVar()
#on window elements and stuff
label = tk.Label(root, text="placeholder", anchor="center").grid(row=0, column=1)
#set coordinate related stuff
checkLabel = tk.Label(root, text="Set Coordinates", anchor="center").grid(row = 1, column = 0, padx=10, pady=10)
checkButton = tk.Button(root, text="Pick", anchor = "e", command=setClickPos).grid(row = 2, column = 0)
coordinateLabel = tk.Label(root, text="Coordinates: N/A", anchor="w")
coordinateLabel.grid(row = 3, column = 0, padx=5, pady=5) #you may notice this is formatted different from the others. Thats cause it was throwing an error. stack overflow said do this, it magically worked, i hav absolutely no clue why it did but it did i guess
#delay related
delayLabel = tk.Label(root, text="Delay", anchor="w").grid(row = 1, column = 2)
delayGroup_1 = tk.Radiobutton(root, text="Default", variable = delayGroup_var, value=1, command=defaultSelect, anchor="w").grid(row = 2, column = 2)
delayGroup_2 = tk.Radiobutton(root, text="Custom", variable = delayGroup_var, value=2, command=customSelect, anchor="w").grid(row = 3, column = 2)
delayEntry = tk.Entry(root, textvariable=delayVar)
delayEntry.insert(0, "")
delayConfirmButton = tk.Button(root, text="Confirm", command=confirm)

start = tk.Button(root, text="start", command=checkForReady).grid(row = 6, column = 1, pady=15)
root.mainloop(
#yeyeyyeyeyeyeyeyye
)



        #literally every source i used ever in a completely random order: https://www.reddit.com/r/learnpython/comments/azgj89/using_mouse_left_click_to_trigger_event_instead/, https://pynput.readthedocs.io/en/latest/mouse.html#monitoring-the-mouse, https://www.w3schools.com/python/python_variables_global.asp, https://stackoverflow.com/questions/23231563/nonetype-object-has-no-attribute-config, 
        #also no ai written code so yay i guess