from PIL import Image
from skimage.io import imread
import matplotlib.pyplot as plt


path = "tiger_cub.jpg"
img = imread(path) / 255.0 

img = Image.fromarray(img)
img= img.resize((224, 224), Image.BILINEAR) 
plt.imshow(img)
plt.show()

