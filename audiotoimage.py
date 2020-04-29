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
print(binary_data_len)
w.close()


# couning pixel and determining dimensions
total_pxl = int(binary_data_len / 4)
xpxl = int(sqrt(total_pxl))
ypxl = xpxl
print('x:', xpxl, '\n', 'y:', ypxl) 


# converting values from binary to integer
int_data = struct.unpack(str(binary_data_len) + 'B', binary_data)
int_data_len = len(int_data)
print(int_data_len)
print("********Preparing**********")