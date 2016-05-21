from GPIOLibrary import GPIOProcessor


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
        # speed = 343  # metres per second (m/s) through Air
        self.speed = 1464  # metres per second (m/s) through Water
        self.depth = 0

        """
        Trig (blue wire) : Pin 33 -> OpAmp Node 2 -> Ultra-sonic sensor Trig
        Echo (red wire) : Ultra-sonic sensor Echo -> Pin 32
        """
        gp = GPIOProcessor()

        self.trig = gp.getPin33()
        self.echo = gp.getPin32()

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
        import time

        self.trig.low()

        # time.sleep(0.5)
        time.sleep(1.0)
        # time.sleep(1.5)  # 1.5 seconds

        self.trig.high()

        # time.sleep(0.00001)
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
        distance = (pulse_duration * self.speed) / 2

        distance = round(distance, 2)
        # print "distance : ",distance

        if distance <= 0.5:
            # print "Object too close! Stopping propeller for 3 seconds."
            time.sleep(3.0)  # aka insert signal to stop motor here.
        # else:
        #     #print "Unknown value. Sleeping for 3 seconds"
        #     time.sleep(3.0)

        # continue

        # print "Distance", distance, "metres"
        self.set_depth(distance)
