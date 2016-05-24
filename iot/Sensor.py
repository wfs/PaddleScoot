from GPIOLibrary import GPIOProcessor
import time


class Sensor:
    def __init__(self):
        self.NameList = []


class UltrasonicHCSR04:
    """
    Sensor Class maps DragonBoard 410c GPIO pins for Debian to the HC-SR04 ultra-sonic sensor.

    Approximate Speed of Sound through Air at 20 degrees centigrade
    343 metres per second.

    For "Shallow Water Sensor"
    Approximate Speed of Sound through Water at 15 degrees centigrade
    1464 metres per second.
    """

    def __init__(self):
        self.speed = 343  # metres per second (m/s) through Air
        # self.speed = 1464  # metres per second (m/s) through Water
        self.depth = 0

        """
        Trig (blue wire) : Pin 33 -> OpAmp Node 2 -> Ultra-sonic sensor Trig
        Echo (red wire) : Ultra-sonic sensor Echo -> Pin 30
        """
        self.gp = GPIOProcessor()

        self.trig = self.gp.getPin33()
        self.echo = self.gp.getPin34()

        self.trig.out()
        self.echo.input()

    def get_depth(self):
        return self.depth

    def set_depth(self, new_depth):
        self.depth = new_depth

    def check_depth(self):
        """
        Activate the sensor to send sound ping (Trig) and receive the echo (Echo) underwater,
        measuring the time interval and calculating and storing the value in depth.
        """
        try:
            print "Activating Shallow Water Sensor ..."
            self.trig.low()
            # time.sleep(0.000002)  # at least 2 micro-seconds
            time.sleep(0.5)  # At least 2 micro-seconds. 0.5 tested and working.
            self.trig.high()
            time.sleep(0.0001)  # At least 5 micro-seconds. 100 tested and working.
            self.trig.low()
            print "Pulse sent."

            # defining variables
            pulse_start = time.time()
            pulse_end = time.time()

            # Wait for pulse to be sent, then
            # save start time.
            # Note : Adding counter to break while loop due to weird glitch.
            counter = 10000
            while self.echo.getValue() == 0 and counter > 0:
                pulse_start = time.time()
                counter -= 1
                #  print "counter :", counter

            if self.echo.getValue() == 1:
                print "Received echo."
                while self.echo.getValue() == 1:
                    pulse_end = time.time()

            if counter == 0:
                print "No echo received for long period. Return to Manager and start again."
                self.set_depth(0)
                return False

            # Calculate total pulse duration
            # print "pulse_end time :", pulse_end
            # print "pulse_start time : ", pulse_start
            pulse_duration = pulse_end - pulse_start
            # print "pulse_duration time :", pulse_duration

            # Use pulse duration to calculate distance
            # Remember that the pulse has to go there and come back
            distance = round((pulse_duration * self.speed) / 2, 2)
            # print "distance :", distance
            self.set_depth(distance)
            return True
        except KeyboardInterrupt():
            print "Keyboard interrupt received. Cleaning up ..."
            self.gp.cleanup()
            return False
