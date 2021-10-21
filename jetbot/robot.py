import time
import traitlets
from traitlets.config.configurable import SingletonConfigurable
# from Adafruit_MotorHAT import Adafruit_MotorHAT
#from .motor import Motor
from .motor import Motor2


class Robot(SingletonConfigurable):
    
    left_front_motor = traitlets.Instance(Motor2)
    right_front_motor = traitlets.Instance(Motor2)
    left_rear_motor = traitlets.Instance(Motor2)
    right_rear_motor = traitlets.Instance(Motor2)

    # config
    # lf 1
    # lr 2
    # rf 3
    # rr 4
    i2c_bus = traitlets.Integer(default_value=1).tag(config=True)
    left_front_motor_channel = traitlets.Integer(default_value=1).tag(config=True)
    left_rear_motor_channel = traitlets.Integer(default_value=2).tag(config=True)
    left_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    right_front_motor_channel = traitlets.Integer(default_value=3).tag(config=True)
    right_rear_motor_channel = traitlets.Integer(default_value=4).tag(config=True)
    right_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    
    def __init__(self, *args, **kwargs):
        super(Robot, self).__init__(*args, **kwargs)
        self.left_front_motor = Motor2(channel=self.left_front_motor_channel, alpha=self.left_motor_alpha)
        self.right_front_motor = Motor2(channel=self.right_front_motor_channel, alpha=self.right_motor_alpha)
        self.left_rear_motor = Motor2(channel=self.left_rear_motor_channel, alpha=self.left_motor_alpha)
        self.right_rear_motor = Motor2(channel=self.right_rear_motor_channel, alpha=self.right_motor_alpha)
        
    def set_motors(self, left_speed, right_speed):
        self.left_front_motor.value = left_speed
        self.right_front_motor.value = right_speed
        self.left_rear_motor.value = left_speed
        self.right_rear_motor.value = right_speed
        
    def forward(self, speed=1.0, duration=None):
        self.left_front_motor.value = speed
        self.right_front_motor.value = speed
        self.left_rear_motor.value = speed
        self.right_rear_motor.value = speed

    def backward(self, speed=1.0):
        self.left_front_motor.value = -speed
        self.right_front_motor.value = -speed
        self.left_rear_motor.value = -speed
        self.right_rear_motor.value = -speed

    def left(self, speed=1.0):
        self.left_front_motor.value = -speed
        self.left_rear_motor.value = -speed
        
        self.right_front_motor.value = speed
        self.right_rear_motor.value = speed

    def right(self, speed=1.0):
        self.left_front_motor.value = speed
        self.left_rear_motor.value = speed
        self.right_front_motor.value = -speed
        self.right_rear_motor.value = -speed

    def stop(self):
        self.left_front_motor.value = 0
        self.right_front_motor.value = 0
        self.left_rear_motor.value = 0
        self.right_rear_motor.value = 0
        