
import urllib

import cv2

import numpy as np

import os

text = open('imagenet2.synset.txt','r')
data = text.readlines()
pic_num = 83
for i in range(0,len(data)):
        try:
            print data[i]
            urllib.urlretrieve(data[i], "pos_gun/"+str(pic_num)+".jpg")
            img = cv2.imread("pos_gun/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)    
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("pos_gun/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))
text.close()
