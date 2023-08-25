
# Mini project in Bioinformatics - CNN melanoma classification

A final project that focuses on designing and implementing a convolutional neural network (CNN) model - (with maximum inclusions) for a melanoma image classification task, while taking meta-data into consideration.

The files:

## CNN_Melanoma_Classification

This notebook contains code that:
- Preprocesses image data to be the training and validation set for a cnn model.
- Sets up data generators for training and validation, with a focus on augmentation during training.
- Sets class weights for balanced training, vital for addressing class imbalances.
- Loads a pre-trained DenseNet121 model and customizes it as needed.
- Trains the model using data generators, adding class weights and callbacks for monitoring.
- Generates predictions on a subset of images and displays their outcomes.
- Illustrates training and validation accuracy and loss trends through plots.

## ML_csv

This notebook contains code that:
- Explores data to comprehend its characteristics.
- Preprocesses data by engineering features and addressing missing values.
- Trains and evaluates machine learning models (such as Random Forest, AdaBoost, Decision Tree) for binary classification.
- Visualizes decision trees to understand their decision paths.
- Investigates feature importance with AdaBoost and evaluates its classification performance.
- Conducts K-means clustering to uncover patterns among data points.
- Visualizes feature correlations through a heatmap.

***
 The image data Kaggle has was not organized into the classes 'benign' and 'malignant'. In addition, the dataset did not have a validation set - important for assessing model performance.

 The goal was to deal with these issues locally before uploading the data to a drive / in the drive. To sort the image files into the classes and creating folders for a random validation set.

## splitting_to_folders_locally

 The code is designed to be reusable across different folders containing image data. While the same code structure is used for various folders, the paths and lists used in it are adjusted as needed to adapt to the specific usage each time.

 Writing this code, we learned about and used two modules: `os` and `shutil`. `os` is utilized for interacting with the operating system, while `shutil` is employed for performing file operations.
This highlights a learning experience in using these modules for the first time.

The code:
- Loads image file names and associated class labels into a dataframe, and separates the file names based on their class labels into 'benign' and 'malignant' lists.
- Defines a path to the directory containing the downloaded image files.
- If subfolders named 'benign' and 'malignant' do not exist within the path - the code creates them.
- The image files (relevant for the current use) are iterated through in the list, for each listed image, the code checks if it exists in the main image directory and if found - the file is moved from the main directory to the relevant subfolder.

## splitting_target_data

File organization.

The code in this notebook:
   - Loads "train.csv" and "test.csv" files into dataframes named.
   - Creates a "yes" column in `train_df` based on conditions related to `'benign_malignant'` and `'target'`.
   - Lists all files and directories in a specified directory.
   - Iterates through each item, extracting file name and extension. If the item is a directory, skips to the next iteration. For items with extensions, checks for existing directories with that name.
   - Moves files to existing directories or creates new directories and moves files there.

## load_model_and_testing

The code in this notebook:
  - Initializes a DenseNet121 model with pre-trained weights from ImageNet, excluding its top layers.
  - Constructs a custom classification model by adding layers like global average pooling, dense, and softmax.
  - Loads pre-trained weights for the `model` from a specified path.
  - Prints a detailed summary of the `model` architecture, including layer specifics and parameters.
  - Enters a loop for two categories. For each category, it loads images, converts them to arrays, and preprocesses them.
  - Displays the loaded image using `matplotlib`.
  - Uses the trained `model` to predict the image's category and prints prediction results, showing predicted probabilities for each class.
## Acknowledgements

 - [SIIM-ISIC Melanoma Classification - A kaggle competition](https://https://www.kaggle.com/competitions/siim-isic-melanoma-classification/overview)

## Authors

- [@orelcarmiel - Carmiel Orel](https://github.com/orelcarmiel)
- [@hollandhr - Holland Hila Rivka](https://github.com/hollandhr)
