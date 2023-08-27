# Mini project in Bioinformatics - CNN melanoma classification

A final project that focuses on designing and implementing a convolutional neural network (CNN) model - (with maximum inclusions) for a melanoma image classification task, while taking meta-data into consideration.

## Workflow:

The image data Kaggle has was not organized into the classes 'benign' and 'malignant'. In addition, the dataset did not have a validation set - important for assessing model performance. We wanted to deal with these issues locally before uploading the data to a drive.

Locally (on a laptop), we used the code in [splitting to folders by target (locally)](https://github.com/miniProjectMelanoma/Melanoma-Classification/blob/main/splitting%20to%20folders%20by%20target%20(locally).py) to sort the downloaded image data. We created 4 folders:

- train files classified as 'Malignant'
- train files classified as 'Benign'
- 50 random train 'Malignant' files for validation
- 3000 random train 'Benign' files for validation

(the code is designed to be reusable across different folders containing image data. While the same code structure is used for various folders, the paths and lists used in it are adjusted as needed to adapt to the specific usage each time)

Writing this code, we learned about and used two modules for the first time: `os` and `shutil`. `os` is utilized for interacting with the operating system, while `shutil` is used for performing file operations.

After uploading the sorted data to the drive we moved to the classification. In [CNN Classification](https://github.com/miniProjectMelanoma/Melanoma-Classification/blob/main/CNN%20Classification.ipynb) we customized a DenseNet121 model, training it with the generators that emphasize augmentation during training, used class weights to adress the huge class imbalances we had, while incorporating monitoring callbacks, generating predictions for a subset of images and visualizing the outcomes. We also illustrated training and validation accuracy and loss trends through plotted graphs.

In [load model and prediction](https://github.com/miniProjectMelanoma/Melanoma-Classification/blob/main/load%20model%20and%20prediction.ipynb) we have 2 options for a model loading: 1. build a model architecture and load in it only pre-trained weights, or 2. load a whole saved model. After we have a loaded model, the code predicts the validation classification, then train the model again.

The prediction is complicated due to the absence of the test class labels. Once we successfully load the saved model, our prediction process will be guided by labeled results from [this web source](https://github.com/Masdevallia/3rd-place-kaggle-siim-isic-melanoma-classification).

For further expansion of our work, [ML Classification](https://github.com/miniProjectMelanoma/Melanoma-Classification/blob/main/ML%20Classification.ipynb) contains a code that organizes the tabular metadata and evaluates machine learning models such as Random Forest, AdaBoost and Decision Tree, as possible models for the final classification. When the loaded cnn model will provide better results, we could add the predictions as a feature to the metadata and see how it might improve the results of the  classification.


## Acknowledgements

[SIIM-ISIC Melanoma Classification - A kaggle competition](https://https://www.kaggle.com/competitions/siim-isic-melanoma-classification/overview) (Data Source)


## Authors

- [@orelcarmiel - Carmiel Orel](https://github.com/orelcarmiel)

- [@hollandhr - Holland Hila Rivka](https://github.com/hollandhr)
## Documentation

- [Documentation of train-validation](https://github.com/miniProjectMelanoma/Melanoma-Classification/blob/main/Documentation%20of%20train-validation.txt) contains documentation of the names of the images in the project in the following format:

Name of the image.jpg Name of the category

Name of the image.jpg Name of the category

Name of the image.jpg Name of the category

.

.

.

Because it will be possible to easily reproduce the results of our training.

- [Model in drive](https://colab.research.google.com/drive/1S_XOPa7pmD4qUnFAO4IV39-WE8XoMltj?usp=drive_link)
