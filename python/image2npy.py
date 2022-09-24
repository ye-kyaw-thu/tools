import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Written by Ye Kyaw Thu, Affiliate Professor, IDRI, CADT, Cambodia
# Extract features from images of each class folder
# Last updated: 24 Sept 2022
# How to run:
# $ python ./image2npy.py
# reference: https://medium.com/analytics-vidhya/create-your-own-real-image-dataset-with-python-deep-learning-b2576b63da1e

#setting the path to the directory containing class folders
path = '/media/ye/project1/cadt/student/internship/demo/image/data/'
subfolders = [ f.path for f in os.scandir(path) if f.is_dir() ]

for foldername in list(subfolders):
#appending the images to the training data list
   training_data = []
   for img in os.listdir(foldername):
      pic = cv2.imread(os.path.join(foldername,img))
      pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
      pic = cv2.resize(pic,(80,80))
      training_data.append([pic])

   #converting the list to numpy array and saving it to a file
   np.save(os.path.join(foldername,'features'),np.array(training_data))

   #Confirmation, loading the saved file once again
   saved = np.load(os.path.join(foldername,'features.npy'))
   # just using one image filename of index 0 (i.e. saved[0])
   plt.imshow(saved[0].reshape(80,80,3))
   plt.imshow(np.array(training_data[0]).reshape(80,80,3))
   plt.show()

