import os
import shutil
import pandas as pd

train_df = pd.(
    'C:/Users/Orel Carmiel/Desktop/Courses with a pathway in English/Fourth year/Mini project in bioinformatics/project/50_random_benign.txt')
print(train_df.head())

benign = train_df.loc[train_df.target == 0, 'image_name']
benign = list(benign)
malignant = train_df.loc[train_df.target == 1, 'image_name']
malignant = list(malignant)

path = 'C:/Users/Orel Carmiel/Desktop/Courses with a pathway in English/Fourth year/Mini project in bioinformatics/project/jpeg/train'

# list_ = os.listdir(path)

if not (os.path.exists(path + '/' + "benign")):
    os.makedirs(path + '/' + "benign")
if not (os.path.exists(path + '/' + "malignant")):
    os.makedirs(path + '/' + "malignant")

# for file_ in malignant:
# 	file_+=".jpg"
# 	shutil.move(path + '/' + file_, path + '/' + "malignant")

for file_ in benign:
    file_ += ".jpg"
    shutil.move(path + '/' + file_, path + '/' + "benign")

print()
