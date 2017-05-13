import urllib
import cv2
import numpy as np
import os
# specify name of text file here and open as read
text = open('links2.txt', 'r')
# 'list' of all the links
data = text.readlines()
# update to suitable number
pic_num = 3456
for i in range(0, len(data)):
    try:
        print data[i]  # print the current link to be accessed
        # download the image
        urllib.urlretrieve(data[i], "neg2/"+str(pic_num)+".jpg")
        img = cv2.imread("neg2/"+str(pic_num)+".jpg",
                         cv2.IMREAD_GRAYSCALE)  # read as grayscale
        resized_image = cv2.resize(img, (100, 100))  # reszie
        cv2.imwrite("neg2/"+str(pic_num)+".jpg", resized_image)  # overwrite
        pic_num += 1  # update pic_num for new file

    except Exception as e:  # if anything above fails, throw an exception
        print(str(e))
text.close()  # close the text file
