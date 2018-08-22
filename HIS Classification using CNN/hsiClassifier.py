from spectral import *
from keras.layers import Dense, Conv2D
from keras.models import Sequential, Model

img = open_image(r'C:\Users\user\Desktop\Abhilash\Imp\CEERI\NN\Hyperspectral Image Visualization\92AV3C.lan')

"""
img.shape
Out[2]: (145, 145, 220)

img
Out[3]: 
	Data Source:   'C:\Users\user\Desktop\Abhilash\Imp\CEERI\NN\Hyperspectral Image Visualization\92AV3C.lan'
	# Rows:            145
	# Samples:         145
	# Bands:           220
	Interleave:        BIL
	Quantization:  16 bits
	Data format:     int16
    
imshow(img)
Out[4]: 
ImageView object:
  Display bands       :  [0, 110, 219]
  Interpolation       :  <default>
  RGB data limits     :
    R: [2632.0, 4536.0]
    G: [1017.0, 1159.0]
    B: [980.0, 1034.0]
"""

