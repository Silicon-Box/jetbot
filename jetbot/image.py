import enum
import cv2
from .jpeg_encoder import JpegEncoder


_ENCODER = JpegEncoder(width=3280, height=2464, fps=21)


def bgr8_to_jpeg_gst(value):
    return _ENCODER.encode(value)


def bgr8_to_jpeg(value, quality=75):
    return bytes(cv2.imencode('.jpg', value)[1])