from PIL import Image
import numpy as np


img =Image.open("dummyaddharback.png")


img_array = np.array(img)

print(img_array)

print(type(img_array))
print(img_array.shapeclear)