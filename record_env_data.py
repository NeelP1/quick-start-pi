from sense_hat import SenseHat
from datetime import datetime
import time
import os
import subprocess
import re

sense = SenseHat()
temp_correction = 8
cpu_temp = re.findall('\d+\.\d+', str(subprocess.check_output(["vcgencmd", "measure_temp"])))[0]
sensor_temp = str(sense.get_temperature() - temp_correction)

lines = [str(datetime.now()), 
			cpu_temp, 
			sensor_temp, 
			str(sense.get_humidity()),
			str(sense.get_pressure()),
			"\n"]
			
with open("data.txt", "a") as file:
	file.writelines("\n".join(lines))
	
#TODO: write values into a csv file instead of a text file

#while True:
#	temp = sense.get_temperature()
#	humidity = sense.get_humidity()
#	pressure = sense.get_pressure()
#	print(str(datetime.now()))
#	subprocess.call(["vcgencmd", "measure_temp"])
#	print("Temp: %s C" % round(temp,2))
#	print("Humidity: %s %%rH" % round(humidity,2))
#	print("Pressure: %s Millibars" % round(pressure,2))
#	time.sleep(2)
#	os.system('clear')
	#print data to a terminal
