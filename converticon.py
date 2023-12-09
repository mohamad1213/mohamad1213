from PIL import Image

import numpy as np 
from PIL import Image, ImageDraw 



img = Image.open("C:\\Users\\LENOVO X1\\Downloads\\Portofolio\\hatami.github.io\\assets\\img\\Hatami.JPG").convert("RGB")
npImage=np.array(img)
h,w=img.size

# Create same size alpha layer with circle
alpha = Image.new('L', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0,0,h,w],0,360,fill=255, width=100)

# Convert alpha Image to numpy array
npAlpha=np.array(alpha)

# Add alpha layer to RGB
npImage=np.dstack((npImage,npAlpha))

# Save with alpha
Image.fromarray(npImage).save('result.png')