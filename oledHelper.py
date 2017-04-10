import os
from OmegaExpansion import oledExp

# initialze the OLED Expansion and set it up for use with the program
def init(dirName):
	oledExp.setVerbosity(-1)
	status  = oledExp.driverInit()
	if status != 0:
		print 'ERROR initializing OLED Expansion'

	## setup the display
	# draw the plant image to the screen
	imgFile = dirName + "/thermometer.oled"
	if os.path.exists(imgFile):
		status = oledExp.drawFromFile(imgFile)

	## write the default text
	# write the first word on the second line and the right side of the screen
	oledExp.setTextColumns()
	oledExp.setCursor(1,12)
	oledExp.write('Temp:')

# write out the soil moisture value
def writeMeasurements(value):
	# set the cursor the fifth line and the right side of the screen
	oledExp.setTextColumns()
	oledExp.setCursor(3,12)
	# write out the text
	oledExp.write( str(value)  + " C" )

# clear the screen, write a message indicating no new measurements are coming in
def setDoneScreen():
	# clear the screen
	oledExp.clear()

	# set the cursor the middle line
	oledExp.setTextColumns()
	oledExp.setCursor(3,0)
	# write out the text
	oledExp.write( "TEMP SENSOR OFFLINE" )
