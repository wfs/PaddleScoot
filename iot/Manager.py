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

    print "Testing Shallow Water Sensor now ..."
    counter = 0
    while counter <= 10:
        sws.activate()
        print "Depth :", sws.get_depth()
        counter += 1
    gp.cleanup()

    #  prop = DC()  # propulsion
    # if prop.start_motor():
    #     print "Testing motor by running for 5 seconds ..."
    #     time.sleep(5)
    #     prop.stop_motor()
    #     gp.cleanup()
    # else:
    #     print "Motor NOT running! Test failed."
except KeyboardInterrupt():
    print "Keyboard interrupt received. Cleaning up ..."
    gp.cleanup()
