import urllib
import cv2
import numpy as np
import os


def store_raw_images():
    # links to download images from

    # http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03822504
        # http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02885882
        # http://image-net.org/api/text/imagenet.synset.geturls?wnid=n10371330

    # current link
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03842156'
    # get all the links for images
    neg_image_urls = urllib.urlopen(neg_images_link).read().decode()
    pic_num = 3456  # update pic_num for files

    # create directory if it doesn't exist
    if not os.path.exists('neg2'):
        os.makedirs('neg2')

    # get images via link by splitting the links
    for i in neg_image_urls.split('\n'):
        try:
            print(i)  # print current link
            urllib.urlretrieve(i, "neg2/"+str(pic_num) +
                               ".jpg")  # download the image
            img = cv2.imread("neg2/"+str(pic_num)+".jpg",
                             cv2.IMREAD_GRAYSCALE)  # read in grayscale
            resized_image = cv2.resize(img, (100, 100))  # resize
            cv2.imwrite("neg2/"+str(pic_num)+".jpg",
                        resized_image)  # overwrite
            pic_num += 1  # update for new file

        except Exception as e:  # if anything above fails, throw an exception
            print(str(e))

store_raw_images()  # call the function
