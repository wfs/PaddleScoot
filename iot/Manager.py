"""
    Script to control the DCMotor based on the ShallowWaterSensor readings.
"""
import time

from GPIOLibrary import GPIOProcessor

from Sensor import UltrasonicHCSR04
from Motor import DC

gp = GPIOProcessor()
sws = UltrasonicHCSR04()  # Shallow Water Sensor
prop = DC()  # propeller

try:
    isSwsActive = sws.activate()
    isPropStarted = prop.start_motor()

    counter = 1
    while isSwsActive and isPropStarted:
    #while counter <= 10:
        print "======= Iteration :", counter
        sws.activate()
        print "Depth :", sws.get_depth()

        if sws.get_depth() < 0.5:
            prop.stop_motor()
            print "Obstacle detected. Motor stopped for 3 seconds."
            time.sleep(3)

        counter += 1

    gp.cleanup()

    #  ======================
    # print "Testing Shallow Water Sensor now ..."
    # counter = 0
    # while counter <= 10:
    #     sws.activate()
    #     print "Depth :", sws.get_depth()
    #     counter += 1
    # gp.cleanup()

    #  =======================
    # if prop.start_motor():
    #     print "Testing motor by running for 5 seconds ..."
    #     time.sleep(5)
    #     prop.stop_motor()
    #     gp.cleanup()
    # else:
    #     print "Motor NOT running! Test failed."
    #  ========================

except KeyboardInterrupt():
    print "Keyboard interrupt received. Cleaning up ..."
    gp.cleanup()
