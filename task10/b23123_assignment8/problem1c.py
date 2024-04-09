from matplotlib import pyplot as plt
# plt.rcParams.update({'font.size': 22})
# importing Image and ImageOps from PIL
from PIL import Image, ImageOps

# creating image object:
imInp = Image.open('problem1cInput.jpg')

# converting imInp to grayscale:
imGrayscale = ImageOps.grayscale(imInp)

# converting image to numpy array
import numpy as np
pixels2D = np.array(imGrayscale)
length1=pixels2D.shape[0]
length2=pixels2D.shape[1]
# showing/saving image  
imGrayscale.save('problem1cOutput.jpg')
# Write code for finding histogram here:
# plt.subplot(1,2,1)
# plt.title("Image")
# plt.imshow(pixels2D,interpolation="bilinear",cmap="gray")
# plt.subplot(1,2,2)
# plt.xlim(0,255)
# plt.title("Grayscale Histogram")
# plt.xlabel("Pixels")
# plt.ylabel("Frequency")
# plt.hist(pixels2D.flatten(),bins=65,color='#0504aa',alpha=0.7, rwidth=0.6, align='mid', density=True)
# plt.tight_layout()
# #resizing figure for maximized window
# # get current figure
# figure = plt.gcf() 
# figure.set_size_inches(16, 12)    
# plt.savefig("problem1ci.png",bbox_inches='tight')

# Write code for finding histogram of difference of pixel's intensity with its left neighbour here:
npixels2D=pixels2D.astype(np.int16)
arr=[]
for i in range(1):
    temp=[]
    for j in range(1,length2):
        temp.append(abs(npixels2D[i][j]-npixels2D[i][j-1]))
    arr.append(temp)
arr=np.array(arr)
plt.xlim(0,255)
plt.title("Grayscale Histogram",fontsize=30)
plt.xlabel("Pixels difference",fontsize=20)
plt.ylabel("Frequency",fontsize=20)
plt.hist(arr.flatten(),bins=65,color='#0504aa',alpha=0.7, rwidth=0.6, align='mid', density=True)
plt.tight_layout()
# resizing figure for maximized window
figure = plt.gcf() # get current figure
figure.set_size_inches(16, 12)
plt.savefig("problem1cii.png",bbox_inches='tight')



