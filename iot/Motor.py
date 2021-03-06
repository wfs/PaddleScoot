from GPIOLibrary import GPIOProcessor


class Motor:
    def __init__(self):
        self.NameList = []


class DC:
    def __init__(self):

        """
        DC maps DragonBoard 410c GPIO pins for Debian to the L293N H-Bridge I/C, ready to receive control
        messages from Manager.py.

        Green wire : Pin 23 -> OpAmp Node 1 -> L298N h-bridge Input 2
        White wire : Pin 24 -> OpAmp Node 4 -> L298N h-bridge Enable A
        Yellow wire : Pin 26 -> OpAmp Node 3 -> L298N h-bridge Input 1

        Set Input 2 to Low, Input 1 to High for clockwise spin.
        """

        self.gp = GPIOProcessor()

        # h-bridge
        self.green = self.gp.getPin23()
        self.white = self.gp.getPin24()
        self.yellow = self.gp.getPin26()

        self.green.out()
        self.white.out()
        self.yellow.out()

        # clockwise
        self.green.low()  # Input 2
        self.yellow.high()  # Input 1

        self.isPropSpinning = False

    def start_motor(self):
        """
        Set Enable A to High to start motor.
        :rtype: Boolean
        :return: True if motor started, False if failed.
        """
        try:
            self.white.low()
            self.white.high()
            self.isPropSpinning = True
            return True
        except KeyboardInterrupt():
            print "Keyboard interrupt received. Cleaning up ..."
            self.gp.cleanup()
            return False

    def stop_motor(self):
        """
        Set Enable A to Low to stop motor.
        :rtype: Boolean
        :return: True if motor stopped, False if failed.
        """
        try:
            self.white.low()
            self.isPropSpinning = False
            return True
        except KeyboardInterrupt():
            print "Keyboard interrupt received. Cleaning up ..."
            self.gp.cleanup()
