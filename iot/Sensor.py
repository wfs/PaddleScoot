from GPIOLibrary import GPIOProcessor
import time


class Sensor:
    def __init__(self):
        self.NameList = []


class UltrasonicHCSR04:
    """
    Sensor Class maps DragonBoard 410c GPIO pins for Debian to the HC-SR04 ultra-sonic sensor.

    Approximate Speed of Sound through Air at 20 degrees centigrade
    343 metres per second

    For "Shallow Water Sensor"
    Approximate Speed of Sound through Water at 15 degrees centigrade
    """

    def __init__(self):
        self.speed = 343  # metres per second (m/s) through Air
        # self.speed = 1464  # metres per second (m/s) through Water
        self.depth = 0

        """
        Trig (blue wire) : Pin 33 -> OpAmp Node 2 -> Ultra-sonic sensor Trig
        Echo (red wire) : Ultra-sonic sensor Echo -> Pin 32
        """
        self.gp = GPIOProcessor()

        self.trig = self.gp.getPin33()
        self.echo = self.gp.getPin32()

        self.trig.out()
        self.echo.input()

    def get_depth(self):
        return self.depth

    def set_depth(self, new_depth):
        self.depth = new_depth

    def activate(self):
        """
        Activate the sensor to send sound ping (Trig) and receive the echo (Echo) underwater,
        measuring the time interval and calculating and storing the value in depth.
        """
        try:
            self.trig.low()
            time.sleep(0.5)  # seconds
            self.trig.high()
            time.sleep(0.0001)
            self.trig.low()

            # defining variables
            pulse_start = time.time()
            pulse_end = time.time()

            # Wait for pulse to be sent, then
            # save start time
            while self.echo.getValue() == 0:
                pulse_start = time.time()

            while self.echo.getValue() == 1:
                pulse_end = time.time()

            # Calculate total pulse duration
            pulse_duration = pulse_end - pulse_start

            # Use pulse duration to calculate distance
            # Remember that the pulse has to go there and come back
            distance = round((pulse_duration * self.speed) / 2, 2)
            self.set_depth(distance)
            return True
        except KeyboardInterrupt():
            print "Keyboard interrupt received. Cleaning up ..."
            self.gp.cleanup()
            return False
