from PIL import Image
from math import sqrt
import random
import wave 
import struct


# opening sound file nd reading the binary data
fname = "file_name.wav"
w = wave.open(fname, 'rb')
binary_data = w.readframes(w.getnframes())
#print(binary_data)
binary_data_len = len(binary_data)
#print(binary_data_len)
w.close()