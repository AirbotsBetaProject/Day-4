import urllib

import cv2

import numpy as np

import os


def store_raw_images():  # defining store raw images
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    #'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n10678937' #assigning link
    neg_image_urls = urllib.urlopen(neg_images_link).read(
    ).decode()  # openinf the url,reading 

    if not os.path.exists('neg'):#if folder dpes not exsist create 
        os.makedirs('neg')

    pic_num = 1

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i, "neg/"+str(pic_num)+'.jpg')#open the url and store images 
            img = cv2.imread("neg/"+str(pic_num)+'.jpg',
                             cv2.IMREAD_GRAYSCALE)#read the image and convert into grey scale 
            resized_image = cv2.resize(img, (100, 100))#resize in 100x100 
            cv2.imwrite("neg/"+str(pic_num)+'.jpg', resized_image)#number the resized image 
            pic_num += 1

        except Exception as e:
            print(str(e))

store_raw_images()
