import atexit
import time
from adafruit_servokit import ServoKit
import traitlets
from traitlets.config.configurable import Configurable


class Motor2(Configurable):

    value = traitlets.Float()
    
    # config
    alpha = traitlets.Float(default_value=1.0).tag(config=True)
    beta = traitlets.Float(default_value=0.0).tag(config=True)

    def __init__(self, channel, *args, **kwargs):
        super(Motor2, self).__init__(*args, **kwargs)  # initializes traitlets
        self._channel = channel
        self._kit = ServoKit(channels=16)

        atexit.register(self._release)
        
    @traitlets.observe('value')
    def _observe_value(self, change):
        self._write_value(change['new'])

    def _write_value(self, value):
        self._kit.continuous_servo[self._channel].throttle = value
        
    def _release(self):
        """Stops motor by releasing control"""
        self._motor.run(ServoKit.RELEASE)
