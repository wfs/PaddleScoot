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
    #  ========================
    #  Just prop spinning, no Shallow Water Sensor
    #  ========================
    prop.stop_motor()
    prop.start_motor()
    print "prop spinning? : ", prop.isPropSpinning
    #  ========================
    #  Uncomment when ultrasonic sensor is fixed.
    #  ========================
    # isSwsActive = sws.activate()
    # print "sws active? :", isSwsActive
    #
    # if isSwsActive and not prop.isPropSpinning:
    #     print "Sensor activated successfully and motor stopped."
    #
    # counter = 1
    # while sws.activate():
    #     # while counter <= 10:
    #     print "======= Iteration :", counter
    #     latest_depth = sws.get_depth()
    #     print "Depth :", latest_depth
    #
    #     if (latest_depth < 0.3) and prop.isPropSpinning:
    #         prop.stop_motor()
    #         print "Obstacle detected. Motor stopped for 2 seconds."
    #         time.sleep(2)
    #     else:
    #         print "Starting motor ..."
    #         if not prop.isPropSpinning:
    #             prop.start_motor()
    #
    #     counter += 1
    #  ========================
    #  Individual component tests ...
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
