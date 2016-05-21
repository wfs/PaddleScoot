"""
    Script to control the DCMotor based on the ShallowWaterSensor readings.
"""
import sys
import time

from GPIOLibrary import GPIOProcessor

from Sensor import UltrasonicHCSR04
from Motor import DC

gp = GPIOProcessor()

try:
    sws = UltrasonicHCSR04()
    print "Activating Shallow Water Sensor ..."

    # counter = 0
    # while counter <=10:
    #     sws.activate()
    #     print "Depth :", sws.get_depth()
    #     counter += 1

    prop = DC()
    if prop.start_motor():
        print "Motor running for 5 seconds ..."
        time.sleep(5)
        prop.stop_motor()
        gp.cleanup()
    else:
        print "Motor NOT running!"
except:
    print "Unexpected error:", sys.exc_info()[0]
    gp.cleanup()
