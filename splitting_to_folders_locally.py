#the image data we got from kaggle was not divided to the classes 'benign' and 'malignant', and did not have a validation set.
#we used this notebook to separate the classes locally and creating a random validation set, before uploading the data to the drive.
#this version of the notebook is for sorting the data in one folder. we used the same notebook for different folders, only changing the paths as needed.
#writing this code, we used the `os` and `shutil` modules for the first time, learning they are used for interacting with the operating system and performing file operations.
import os
import shutil
import pandas as pd

#loading the files names to a dataframe for easy sorting
train_df = pd.(
    'C:/Users/Orel Carmiel/Desktop/Courses with a pathway in English/Fourth year/Mini project in bioinformatics/project/50_random_benign.txt')
print(train_df.head())

#seperating the files names by class (target) into 2 lists
#in the 'target' column 'benign' is 0, 'malignant' is 1
benign = train_df.loc[train_df.target == 0, 'image_name']
benign = list(benign)
malignant = train_df.loc[train_df.target == 1, 'image_name']
malignant = list(malignant)

#the path of the downloaded images
path = 'C:/Users/Orel Carmiel/Desktop/Courses with a pathway in English/Fourth year/Mini project in bioinformatics/project/jpeg/train'

#if not existing, creating a folder for each class
if not (os.path.exists(path + '/' + "benign")):
    os.makedirs(path + '/' + "benign")
if not (os.path.exists(path + '/' + "malignant")):
    os.makedirs(path + '/' + "malignant")

#going through the list of 'benign' image files
#for each, if the file name is in the folder of all the downloaded image files - move it to the previously created 'benign' folder
for file_ in benign:
    file_ += ".jpg"
    shutil.move(path + '/' + file_, path + '/' + "benign")

#we check manually that the transfer was done as needed
