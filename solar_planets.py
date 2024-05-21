import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (40, 200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mercury", (110, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Venus", (200, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Earth", (290, 255), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Mars", (390, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Jupiter", (570,390), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Saturn", (790, 320), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Uranus", (965, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
cv2.putText(img, "Neptune", (1110, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.imwrite("Solar_systemwithname.jpg", img)
cv2.imshow("output", img)
cv2.waitKey(0)
