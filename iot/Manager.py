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
    print "Paddle Scoot starting up ..."
    isSwsActive = sws.activate()
    print "sws active? :", isSwsActive
    isPropStopped = prop.stop_motor()
    print "prop stopped? : ", isPropStopped

    if isSwsActive and isPropStopped:
        print "Sensor activated successfully and motor stopped."

    counter = 1
    while sws.activate():
    #while counter <= 10:
        print "======= Iteration :", counter
        latest_depth = sws.get_depth()
        print "Depth :", latest_depth

        if latest_depth < 0.3:
            prop.stop_motor()
            print "Obstacle detected. Motor stopped for 3 seconds."
            time.sleep(3)
        else:
            prop.start_motor()

        counter += 1
        #time.sleep(1)
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
