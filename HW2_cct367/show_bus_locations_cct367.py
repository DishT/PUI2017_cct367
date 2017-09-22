# Author: ChunChieh,Tsai(蔡俊傑), NYU, September 2017
##############################
# Code written to demonstrate to pass arguments to a python script
# for HW2_1 of PUI2017
##############################
# put <MTA_KEY> <BUS_LINE> as input 2 arguments:
# i.e. run the code as
#      python show_bus_locations.py <MTA_KEY> <BUS_LINE>
#      python3 show_bus_locations.py <MTA_KEY> <BUS_LINE>
# notice that <MTA_KEY> <BUS_LINE> should be 2 words with space(only the first line argument is read)

# the next line import packages that change the python 2 print function
# so that it require the same syntax as python 3
# thus the code will work both in python 2 and python 3
from __future__ import print_function
import sys
import requests
import json
import pandas as pd



# STEP1. Make sure the argument correct
if not len(sys.argv) == 3:
    print("Invailid number of argument. Run as: python.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

# STEP2. Get the Arguments from command line

key = sys.argv[1]
bus_line_code = sys.argv[2]
#key = "60109463-c9b9-459b-af8f-521f47b0e763"
#bus_line_code = "B52"

# STEP3. Download the Json from the MTA API
re = requests.get('http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={0}&VehicleMonitoringDetailLevel=calls&LineRef={1}'.format(key,bus_line_code))
#print (type(re))
#print (type(re.text))
js = json.loads(re.text)
# STEP4. If the bus line not exist, jump out of the program
try:
    bus = js["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    bus_line = bus[0]["MonitoredVehicleJourney"]["LineRef"].split("_")[1]
    print ("Bus Line: ", bus_line)
    print("Number of Active Buses :",len(bus) )

    for i in range(len(bus)):
        longtitude = bus[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
        lat = bus[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
    
        print("Bus",i,"is at latitude",lat,"and longitude",longtitude)
except:
    print("No such route: MTA_{}".format(bus_line_code), "Please type again !")


#print (len(bus))