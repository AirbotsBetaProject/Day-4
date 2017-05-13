import urllib

import cv2

import numpy as np

import os


def store_raw_images():  # defining store raw images
    pos_rifle_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03695857'

    pos_rifle_image_urls = urllib.urlopen(
        pos_rifle_images_link).read().decode()  # read open and decode the url,reading

    if not os.path.exists('pos_rifl'):  # if folder dpes not exsist create
        os.makedirs('pos_rifl')
    pic_num = 1

    for i in pos_rifle_image_urls.split('\n'):  # open the url and store images
        try:
            print(i)
            urllib.urlretrieve(i, "pos_rifl/" + str(pic_num)+'.jpg')
            img = cv2.imread("pos_rifl/" + str(pic_num)+'.jpg',
                             cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("pos_rifl/" + str(pic_num)+'.jpg', resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

store_raw_images()
