
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('../data/sammy_face.jpg')
plt.imshow(img)
plt.show()


edges = cv2.Canny(image=img, threshold1=127, threshold2=127)
plt.imshow(edges)
plt.show()


med_val = np.median(img)
print(med_val)

# Lower threshold to either 0 or 70% of the median whichever is greater
lower = int(max(0, 0.7*med_val))

# Upper threshold to either 130% of the median or the max 255, whichever is smaller
upper = int(min(255, 1.3*med_val))

edges = cv2.Canny(image=img, threshold1=lower, threshold2=upper)
plt.imshow(edges)
plt.show()

blurred_img = cv2.blur(img, ksize=(5, 5))

edges = cv2.Canny(image=blurred_img, threshold1=lower, threshold2=upper)
plt.imshow(edges)
plt.show()
