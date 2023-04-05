import cv2
import matplotlib.pyplot as plt
import numpy as np
img = plt.imread("circles.gif")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_org = img

kernel2 = np.zeros((5,5), dtype=np.uint8)

img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel2, iterations=4)

print(kernel2)

fig, axes = plt.subplots(1, 2)
axes[0].imshow(img_org, cmap='gray')
axes[1].imshow(img, cmap='gray')
axes[0].axis('off')
axes[1].axis('off')
plt.show()