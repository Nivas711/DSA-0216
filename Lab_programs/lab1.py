from google.colab import files
import cv2
from google.colab.patches import cv2_imshow

uploaded = files.upload()
filename = list(uploaded.keys())[0]

img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2_imshow(img)
cv2_imshow(gray)
