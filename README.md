# Project: Using a Pre-Trained Image Classifier

Having implemented argument parser for this project, there are a number of optional arguments that can be input through the command line so as to customise the program. See below:

•	**Change image directory:** '--dir', type = str, default = 'pet_images/', help = 'path to the folder of pet images'

•	**Change model CNN architecture:** '--arch', type = str, default = 'vgg', help = 'choice of CNN Model Architecture; 'resnet', 'alexnet' or'vgg''

•	**Change category names:** '--dogfile', type = str, default = 'dognames', help = 'text file with list of Dog Names to be referenced'

Program will print summary statistics to console regarding accuracy of each model arhitecture in making correct predicitions.
