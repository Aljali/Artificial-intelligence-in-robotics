import cv2

img =cv2.imread('Davide.width-1200.jpg')
px = img[100,100]
print(px)
cv2.imshow('img',img)
(B,G,R)=img[100,50]
print("R={} , G={} ,B={}".format(R,G,B))

print("Shape :",img.shape)
print("size :",img.size)
print("Type :",img.dtype)
