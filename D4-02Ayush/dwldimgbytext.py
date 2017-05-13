import urllib
import cv2
import numpy as np
import os

text = open('links2.txt','r')
data = text.readlines()
pic_num = 3456
for i in range(0,len(data)):
        try:
            print data[i]
            urllib.urlretrieve(data[i], "neg2/"+str(pic_num)+".jpg")
            img = cv2.imread("neg2/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
    	    # should be larger than samples / pos pic (so we can place our image on it)	
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg2/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))
text.close()
