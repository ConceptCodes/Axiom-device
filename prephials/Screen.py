from drivers.lcd import *
from time import sleep 

class Screen: 
    def __init__(self):
        self.lcd = LCD(baud = 21000000)
 
    def launch_screen(self):
        #make the background white                                                 
        sef.lcd.fillMonocolor(WHITE)                                                    
        #load the logo
        self.lcd.renderBmp('logo.bmp',pos=(75,61))
        #render the progress bar
        self._progress_bar(x=17, y=164, w=286, h=15, col1=PRIMARY, col2=SECONDARY)
        self.lcd.initCh(color=GREY).printLn('Perspectives', 125, 221)

    def home_screen(self):
        #get the current plant and 
        self.lcd.fillMonocolor(color=WHITE) #set background color to white
        #sidebar
        self.lcd.drawRect(0, 0, 144, 240, PRIMARY, border=0, infill=PRIMARY) 
        self.lcd.initCh(color=WHITE, scale=2).printLn('Plant Name', 5, 16)    
        self.lcd.initCh(color=SECONDARY).printLn('Plant Type', 5, 43) 
        self.lcd._render_bmp_image('basil.bmp', pos=(-34,119)) 
        #main
        self.lcd.initCh(color=PRIMARY).printLn('Day', 155, 43)
        self.lcd.initCh(color=BLACK, scale=2).printLn('21', 155, 58)
        #water
        self.lcd.initCh(color=SECONDARY).printLn('Water', 155, 119)
        self._progress_bar(x=155, y=124, w=156, h=7, col1=GREY, col2=SECONDARY)
        #light
        self.lcd.initCh(color=SECONDARY).printLn('Light', 155, 153)
        self._progress_bar(x=155, y=167, w=156, h=7, col1=GREY, col2=SECONDARY)
        #growth
        self.lcd.initCh(color=SECONDARY).printLn('Growth Cycle', 155, 186)
        self._progress_bar(x=155, y=200, w=156, h=7, col1=GREY, col2=SECONDARY)       
        #version
        self.lcd.initCh(color=GREY).printLn("v1.0", 298, 228)




    def _progress_bar(self, x, y, w, h, col1, col2):
        #should have the secondary color as background
        self.lcd.drawRect(17, 164, w, h, col1, border=0, infill = col1)
        #then inside bar will be primary color 
        for progress in range(0,100):
            self.lcd.drawRect(17, 164, 20, progress, col2, border = 0, infill = col2) 
            sleep(2) #sleep for 2 seconds
