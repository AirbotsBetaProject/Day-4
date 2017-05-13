import urllib
import cv2
import numpy as np
import os

def store_raw_images():
	#http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03822504
	#http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02885882
	#http://image-net.org/api/text/imagenet.synset.geturls?wnid=n10371330
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03842156'   
    neg_image_urls = urllib.urlopen(neg_images_link).read().decode()
    pic_num = 3456
    
    if not os.path.exists('neg2'):
        os.makedirs('neg2')
        
    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i, "neg2/"+str(pic_num)+".jpg")
            img = cv2.imread("neg2/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
    	    # should be larger than samples / pos pic (so we can place our image on it)	
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg2/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))

store_raw_images()  
