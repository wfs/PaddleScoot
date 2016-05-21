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
    sws.activate()

    prop = DC()
    prop.start_motor()
    time.sleep(5)
    prop.stop_motor()

    gp.cleanup()

except:
    print "Unexpected error:", sys.exc_info()[0]
    gp.cleanup()